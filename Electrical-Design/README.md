# Electrical Design 

In this document you'll find all the things about the electrical components like the capacity of the sensors, the battery, and how is designed the electrical on the robot.

## Introduction
Our electrical design consists of the amount of 7 sensors, with which our car is capable of flawlessly driving through the track without much difficulty. The sensors of our choice are the 2 APDS9960 sensors on the front for effective proximity and color detecting, some infrared vl53lx0 distance sensors on each side for mantaining the car as centered through the track 2 tmf sensors aiding the APDS upfront because of their grid like detecting. and lastly our bno08x IMU which we will use to make the car know where it is at and where is headed to. The powerful brain here is a MOTION PRO RP2350 which programmed in micropython is more than capable of handling every sensor on the list. Our drive hardware consists of the trusty TT motor for driving and a sturdy MG996r servo motor for steering. But this is too basic isnt it, just using some generic hardware to make our car drive is too basic for us engineers right? Well of course it is we can do more, we can do better and thats why we ARE designing our own sensors for future competitions, as a matter of fact we ALREADY have the schematics for a mix of the powerful TCS and TMF sensors (designed by us) in one board and we plan on making the best hardware we can for our needs in this competence. 

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

