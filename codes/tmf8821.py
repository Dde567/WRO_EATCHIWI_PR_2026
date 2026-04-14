from machine import I2C, Pin
import time
ADDR = 0x41
class TMF8821:
    def __init__(self, i2c=None):
        # Use provided I2C or create default one for RP2350 (pins 16 & 17)
        if i2c is None:
            self.i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
        else:
            self.i2c = i2c
        # Quick scan to confirm device is present
        if ADDR not in self.i2c.scan():
            raise RuntimeError("TMF8821 not found at address 0x{:02X}".format(ADDR))
        # ENABLE register (0xE0): Controls device power state and boot selection. Writing 0x21 sets pon=1 (power on) and powerup_select=1 (start bootloader without entering sleep). Expect the device to transition to enabled state.
        self._write_reg(0xE0, 0x21)
        for _ in range(100):
            # Read ENABLE register (0xE0): Check device mode and readiness. Mask with 0xCF ignores bits 4-5. Expect value 0x41 indicating CPU ready (bit7=0 potentially) and specific boot state.
            mode = self._read_reg(0xE0) & 0xCF
            if mode == 0x41:
                break
            time.sleep_ms(1)
        else:
            raise RuntimeError("Failed to enable TMF8821 (mode = 0x{:02X})".format(mode))
        # APPID register (0x00): Identifies current application mode. Expect 0x80 for bootloader or 0x03 for measurement application.
        if self._read_reg(0x00) == 0x80:
            self._load_firmware()
        # Configure for 4×4 mode (16 zones – best square mode for TMF8821)
        self._configure_4x4()
        self.temperature = 0
        
        
    def _write_reg(self, reg, value):
        self.i2c.writeto(ADDR, bytes([reg, value]))
    def _read_reg(self, reg, n=1):
        self.i2c.writeto(ADDR, bytes([reg]))
        buf = self.i2c.readfrom(ADDR, n)
        if n == 1:
            return buf[0]
        return buf
    def _send_command(self, cmd):
        # CMD_STAT register (0x08): Write command to initiate actions (e.g., 0x16 to load config page). In bootloader mode, it's BL_CMD_STAT.
        self._write_reg(0x08, cmd)
        for _ in range(100):
            # Read CMD_STAT register (0x08): Check command status. Values 0x00-0x0F indicate completion (0x00 success). Higher values mean processing.
            status = self._read_reg(0x08)
            if status < 0x10:
                break
            time.sleep_ms(1)
        else:
            raise RuntimeError("Command 0x{:02X} timeout".format(cmd))
        if status > 0x01:
            raise RuntimeError("Command 0x{:02X} failed (status=0x{:02X})".format(cmd, status))
    def _load_firmware(self):
        with open("firmware.bin", "rb") as f:
            fw = f.read()
        # BL_CMD_STAT (0x08 in bootloader): Send DOWNLOAD_INIT command (0x14) with data [0x29] (likely setting max upload size). Expect status 0x00 on completion.
        self._send_bootloader(0x14, [0x29])
        # BL_CMD_STAT (0x08): Send SET_ADDR command (0x43) with [0x00,0x00] to set RAM address to 0x0000. Expect status 0x00.
        self._send_bootloader(0x43, [0x00, 0x00])
        # BL_CMD_STAT (0x08): Send W_RAM command (0x41) for each chunk to write firmware to RAM. Expect status 0x00 per chunk.
        for i in range(0, len(fw), 80):
            chunk = fw[i:i+80]
            self._send_bootloader(0x41, list(chunk))
        # BL_CMD_STAT (0x08): Send RAMREMAP_RESET command (0x11) to remap and reset to application. Expect status 0x00.
        self._send_bootloader(0x11, [])
        time.sleep_ms(3)
    def _send_bootloader(self, cmd, data):
        message = [cmd, len(data)] + data
        chksum = (sum(message) & 0xFF) ^ 0xFF
        message.append(chksum)
        # Write to BL_CMD_STAT (0x08): Send bootloader command with data and checksum.
        self.i2c.writeto(ADDR, bytes([0x08] + message))
        for _ in range(100):
            # Read from BL_CMD_STAT (0x08): Fetch 3 bytes for status. Expect first byte 0x00 for success.
            self.i2c.writeto(ADDR, b'\x08')
            status = self.i2c.readfrom(ADDR, 3)[0]
            if status == 0x00:
                return
            time.sleep_ms(1)
        raise RuntimeError("Bootloader command 0x{:02X} failed".format(cmd))
    def _configure_4x4(self):
        # Send command 0x16 to CMD_STAT (0x08): LOAD_CONFIG_PAGE - Loads common configuration page into registers starting at 0x20. Expect status 0x00.
        self._send_command(0x16)
        # Read CONFIG_RESULT (0x20, 4 bytes): Verify config page loaded. Expect byte0=0x16 (cid_rid for config), byte2=0xBC (possibly header), byte3=0x00.
        check = self._read_reg(0x20, 4)
        if check[0] != 0x16 or check[2] != 0xBC or check[3] != 0x00:
            raise RuntimeError("Failed to load configuration page")
        # SPAD_MAP_ID (0x34 in config page): Set to 0x04 for 4x4 mode (60deg FoV). Defines zone configuration.
        self._write_reg(0x34, 0x04)
        # Send command 0x15 to CMD_STAT (0x08): WRITE_CONFIG_PAGE - Writes changes back to device. Expect status 0x00.
        self._send_command(0x15)
       
    def read(self):
        # INT_STATUS (0xE1): Write 0xFF to clear all interrupts. Prepares for new measurement.
        self._write_reg(0xE1, 0xFF)
        # Send command 0x10 to CMD_STAT (0x08): MEASURE - Starts a measurement. Expect status 0x00 when done.
        self._send_command(0x10)
        # Wait for INT_STATUS (0xE1): Bit1 (0x02) set indicates result ready.
        for _ in range(500):
            if self._read_reg(0xE1) & 0x02:
                break
            time.sleep_ms(1)
        else:
            raise RuntimeError("Measurement timeout")
        # Read measurement results starting at 0x20 (132 bytes): Contains result data when cid_rid=0x10 (measurement page). Includes distances, confidences, etc.
        data = bytearray()
        reg = 0x20
        remaining = 132
        while remaining > 0:
            sz = min(remaining, 32)
            self.i2c.writeto(ADDR, bytes([reg]))
            chunk = self.i2c.readfrom(ADDR, sz)
            data += chunk
            reg += sz
            remaining -= sz
        # Send command 0xFF to CMD_STAT (0x08): STOP - Aborts ongoing measurement. Expect status 0x00.
        self._write_reg(0x08, 0xFF)
        # Extract primary distances (18 results, but 4x4 uses 16 specific ones)
        self.temperature = data[3]
        
        distances = []
        for i in range(18):
            offset = 25 + 3 * i
            dist = int.from_bytes(data[offset:offset+2], 'little')
            distances.append(dist)
        
      
        # TMF8821 4×4 layout: results 0–7 + 9–16 (skips result 8)
        zones = distances[0:8] + distances[9:17]
        # Format into nice 4×4 grid (row 0 = top, row 3 = bottom)
        grid = [
            zones[0:4], # top row
            zones[4:8],
            zones[8:12],
            zones[12:16] # bottom row
        ]
        return zones