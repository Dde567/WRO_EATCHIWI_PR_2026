from machine import Pin, PWM

class m1:
    
    def __init__(self, freq=120):
        self.m1a = PWM(Pin(8))
        self.m1b = PWM(Pin(9))
        self.m1a.freq(freq)
        self.m1b.freq(freq)
        
    def forward(self, speed):
        self.m1a.duty_u16(int(2**(speed/6.25)))
        self.m1b.duty_u16(0)
        
    def reverse(self, speed):
        self.m1a.duty_u16(0)
        self.m1b.duty_u16(int(2**(speed/6.25)))
        
    def stop(self):
        self.m1a.duty_u16(0)
        self.m1b.duty_u16(0)
        
class m2:
    
    def __init__(self, freq=120):
        self.m2a = PWM(Pin(10))
        self.m2b = PWM(Pin(11))
        self.m2a.freq(freq)
        self.m2b.freq(freq)
        
    def forward(self, speed):
        self.m2a.duty_u16(int(2**(speed/6.25)))
        self.m2b.duty_u16(0)
        
    def reverse(self, speed):
        self.m2a.duty_u16(0)
        self.m2b.duty_u16(int(2**(speed/6.25)))
        
    def stop(self):
        self.m2a.duty_u16(0)
        self.m2b.duty_u16(0)
        

