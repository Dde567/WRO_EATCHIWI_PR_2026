#######ejomcode########


from machine import Pin, PWM, I2C
from time import sleep, sleep_ms			
import utime
from apds9960.const import *					# https://github.com/liske/python-apds9960.git
from apds9960 import uAPDS9960 as APDS9960

R = 0
G = 1
B = 2
C = 3
FRONTL = [1,1,1,1]
FRONTR = [1,1,1,1]
COLOR_COMP = [1,1.17,1.16,1]
WHITE_POINT = .9

LED = PWM(Pin(14))

LED.freq(1000)

LED.duty_u16(50000)


APDS9960_ATIME = 219
Integration_Sleep = ((2.78 * (256 - APDS9960_ATIME))/1000)

try:
    #it tries to connect the front color sensors (GROVE 4)
    i2c_fL = I2C(0, scl = Pin(17), sda = Pin(16), freq = 400000)
    frontl = APDS9960(i2c_fL)
    print("Front Sensor Connected")
    
except OSError as e:
	#if it fails to connect it will produce an error message.

    print("Error initializing", e)

try:
    #it tries to connect the down color sensors (GROVE 6)
    i2c_fR = I2C(1, scl = Pin(3), sda = Pin(2), freq = 400000)
    frontr = APDS9960(i2c_fR)
    print("Lower Sensor Connected")
    
except OSError as e:
	#if it fails to connect it will produce an error message.
    print("Error initializing", e)
    
    
def read():
    
     global R, G, B, C, FRONTL, FRONTR, COLOR_COMP, Integration_Sleep
     
     try:
         
         frontl.enableLightSensor()
         print("FRONT 1")
         FRONTL = (frontl.readRedLight()*COLOR_COMP[R], frontl.readGreenLight()*COLOR_COMP[G], frontl.readBlueLight()*COLOR_COMP[B], frontl.readAmbientLight()*COLOR_COMP[C])
         
     except OSError as e:
         
         print("Error initializing", e)
         
     
         
     
     
     
def WHITECAL():
    
    global R, G, B, C, FRONTL, FRONTR, COLOR_COMP, Integration_Sleep
    frontl.enableLightSensor()
    
    for i in range(50):
        sleep(Integration_Sleep)
        FRONTL[R] += (frontl.readRedLight())
        FRONTL[G] += (frontl.readGreenLight())
        FRONTL[B] += (frontl.readBlueLight())
        
    FRONTL[R] /= 10 
    FRONTL[G] /= 10 
    FRONTL[B] /= 10

    if FRONTL[G] <= FRONTL[R] >= FRONTL[B]:
        COLOR_COMP[R] = 1
        COLOR_COMP[G] = FRONTL[R] / FRONTL[G]
        COLOR_COMP[B] = FRONTL[R] / FRONTL[B]
    
    elif FRONTL[R] <= FRONTL[G] >= FRONTL[B]:
        COLOR_COMP[R] = FRONTL[G] / FRONTL[R]
        COLOR_COMP[G] = 1 
        COLOR_COMP[B] = FRONTL[G] / FRONTL[B]
   
    elif FRONTL[R] <= FRONTL[B] >= FRONTL[G]:
        COLOR_COMP[R] = FRONTL[B] / FRONTL[R]
        COLOR_COMP[G] = FRONTL[B] / FRONTL[G]
        COLOR_COMP[B] = 1
   
    else:
        pass
    
    
def color_detect():
    
    global R, G, B, C, FRONTL, FRONTR, COLOR_COMP, WHITE_POINT
    read()
    
    if FRONTL[G] <= FRONTL[R] >= FRONTL[B]:
        
        if FRONTL[R] * WHITE_POINT < FRONTL[B] and FRONTL[G]:
            
            print("	WHITE ", FRONTL)
            return "white"
        
        
        
        else:
            print("red", FRONTL)
        
    elif FRONTL[R] <= FRONTL[G] >= FRONTL[B]:
        
         if FRONTL[G] * WHITE_POINT < FRONTL[B] and FRONTL[R]:
            
             print("	WHITE ", FRONTL)
             return "white"
        
         
         else:
             print("green", FRONTL)
        
       
    else:
        print("	WHITE ", FRONTL)
        return "white"
        
    
