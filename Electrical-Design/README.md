# Electrical Engineer 

In this document you'll find all the things about the electrical components like the capacity of the sensors, the battery, and how is designed the electrical on the robot.

## Battery
The battery it's a JUOVI power bank that have a capacity of 37W/h and can supply 35W continuos, with a capacity of 10,000mAh and includes dual USB Type-C ports and one USB-A port. 


## How much the sensors consume?
- MOTION PRO RP2350 (microcontroller) = Normal Run: Approximately 22mA.

- APDS9960 (color/proximity sensor) = Active Sensing (Light/Proximity): Generally under 1 mA.

- bno08x (orientation sensor) = Active/Awake Mode: ~12.3 mA 

- vl53l0x (distance sensor) = Active Ranging: ~19mA (normal operation) but can peak up to 40mA.

- tmf8821 (distance sensor) = Active Current Consumption: ~57 mA.

- MG996r (servo) = Operating Current (Under Load): 500mA - 900mA.

- TT motor = At 6VDC: 160mA @ 250 RPM no-load, and 1.5 Amps when stalled.

## Electrical Diagram 
<img src = "Electrical-Design\Electrical_Diagram.png" width = "400" height = "300">
