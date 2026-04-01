### EJOM CODE ###

from machine import Pin, PWM
import time
from time import sleep


PINION = PWM(12)
PINION.freq(50)

class servo:
    
    def VARIABLE(Pin, var): 
        
        PINION = PWM(Pin)
        
        if var >= 2_200_000:
            var = 2_190_000
            
        elif var <= 800_000:
            
            var = 810_000
            
        PINION.duty_ns(var)
        previous = "variable"
        sleep(.05)
        servo.stop(12)
        print( var)
     
    def stop(Pin):
        
        PINION = PWM(Pin)
        
        PINION.deinit()
    
    
    def left(Pin):
        
        PINION = PWM(Pin)
        
        PINION.duty_ns(2_000_000)
        sleep(.05)
        servo.stop(12)
        
        previous = 'left'
        
    def right(Pin):
        
        PINION = PWM(Pin)
        
        PINION.duty_ns(1_000_000)
        sleep(.05)
        servo.stop(12)
        
        previous = 'right'
        
    def center(Pin):
        
        PINION = PWM(Pin)
        
        PINION.duty_ns(1_500_000)
        sleep(.05)
        servo.stop(12)
        
        previous = 'center'
        
        
