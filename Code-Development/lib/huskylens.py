# Save this file on the Pico as: huskylens.py
import struct

class HuskyLensProtocol:
    def __init__(self, uart_instance):
        self.uart = uart_instance
        # Header for HuskyLens 2 commands
        self.header = b'\x55\xAA\x11'

    def send_cmd(self, cmd):
        # Frame format: Header(3 bytes) + Length(1 byte) + Command(1 byte) + Checksum(1 byte)
        length = 0
        checksum = (0x11 + length + cmd) & 0xFF
        packet = self.header + bytes([length, cmd, checksum])
        self.uart.write(packet)

    def request_data(self):
        # 0x24 is the request command code for object data
        self.send_cmd(0x24)
        
    def read_blocks(self):
        self.request_data()
        # Read the incoming serial frame from the Pico hardware buffer
        if self.uart.any() >= 5:
            head = self.uart.read(5)
            if head and head[0:3] == b'\x55\xAA\x11':
                data_len = head[3]
                cmd = head[4]
                
                # Check for standard data payload command (0x29)
                if cmd == 0x29 and data_len >= 10:
                    payload = self.uart.read(data_len + 1) # Payload + Checksum
                    if len(payload) >= 11:
                        # Unpack binary data mapping coordinates from the UART stream
                        x, y, w, h, obj_id = struct.unpack('<hhhhh', payload[0:10])
                        return {"x": x, "y": y, "width": w, "height": h, "id": obj_id}
        return None
