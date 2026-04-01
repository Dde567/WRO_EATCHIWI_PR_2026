#######ejomcode########


from machine import Pin, PWM
import time
from apds9960.const import *					# https://github.com/liske/python-apds9960.git
from apds9960 import uAPDS9960 as APDS9960
from motors import *
from servo import servo
from hc_sr04 import *
from APDS import *




mtr = m1()



servo.center(12)
mtr.stop()
gp20 = Pin(20, Pin.IN, Pin.PULL_UP)
gp21 = Pin(21, Pin.IN, Pin.PULL_UP)

US_1 = HCSR04(trigger_pin= 26, echo_pin= 6, echo_timeout_us=500*2*30) 
US_2 = HCSR04(trigger_pin= 5, echo_pin= 4, echo_timeout_us=500*2*30)

while True:
    if gp20.value() == 0:
        servo.center(12)
        sleep(1)
        mtr.forward(93)
        break
    
while True:
    
    
    dist_L= US_1.distance_cm()
    dist_R = US_2.distance_cm()
    
    



    vrbl = int(3_000_000 * (60 - dist_L - dist_R) / 60)
    servo.VARIABLE(12, var = vrbl)
    print( dist_L, dist_R )
    
    
    APDS.color_detect()
    
    
    if color_detect() == "red":
        
        tim1 = utime.ticks_ms()
        
        while utime.ticks_diff(utime.ticks_ms(), tim1) <= 1000:
            
            vrbl_R = int(3_000_000 * (20 - dist_R) / 20)
            servo.VARIABLE(12, var = vrbl_R)
            print( dist_L, dist_R)
            
        tim2 = utime.ticks_ms()
            
        while utime.ticks_diff(utime.ticks_ms(), tim2) <= 1000:
            
            vrbl_L = int(3_000_000 * (20 - dist_L) / 20)
            servo.VARIABLE(12, var = vrbl_L)
            print( dist_L, dist_R)
            
            
        print("cycle complete")
        
        
    if color_detect() == "green":
        
        tim1 = utime.ticks_ms()
        
        while utime.ticks_diff(utime.ticks_ms(), tim1) < 1000:
            
            vrbl_L = int(3_000_000 * (20 - dist_L) / 20)
            servo.VARIABLE(12, var = vrbl_L)
            print( dist_L, dist_R)
            
        tim2 = utime.ticks_ms()
            
        while utime.ticks_diff(utime.ticks_ms(), tim2) < 1000:
            
            vrbl_R = int(3_000_000 * (20 - dist_R) / 20)
            servo.VARIABLE(12, var = vrbl_R)
            print( dist_L, dist_R)
            
            
        print("cycle complete")
            
        
        
        
        
        