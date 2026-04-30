# WRO_EATCHIWI_PR_2026

This repository contains the documentation of the team EatChiwi on the challenge of creating a self-driving vehicle. Here you're going to find all about the creation of the vehicle: mechanical parts, programation, and system thinking. 

## Table of Content :

|Code-Development | Links |
|-----------------|-------|
|Codes | [Code-Development\codes]()|
|Readme| [Code-Development\README.md]()|

|Electrical-Design | Links |
|------------------|-------|
|Hardware CADS     | [Electrical-Design\HardwareCADS]()|
|Electrical Diagram| [Electrical-Design\Electrical_Diagram.png]()|
|Readme            | [Electrical-Design\README.md]()|

|Journal | Links |
|--------|-------|
|Readme| [Journal\README.md]()|

|Mechanics | Links |
|----------|-------|
|CAD   | [Mechanics\CAD]()|
|Readme| [Mechanics\README.md]()|

|T-Photo | Links |
|--------|-------|
|Normal|[T-Photo\Photo Team EatChiwi.jpg]()|
|Crazy |[T-Photo\Photo Team EatChiwi (2).jpg]()|
|Readme|[T-Photo\README.md]()|

|V-Photo | Links |
|--------|-------|
|V-1.0|[V-Photo\V-Photo Version_1.0]()|
|V-1.1|[V-Photo\V-Photo Version_1.1]()|
|V-1.2|[V-Photo\V-Photo Version_1.2]()|
|V-1.3|[V-Photo\V-Photo Version_1.3]()|
|V-1.4|[V-Photo\V-Photo Version_1.4]()|
Readme|[V-Photo\README.md]()|

|Video | Link |
|------|------|
Open Lap for PRNRO 2026 (Team EatChiwi)|[https://youtu.be/rVMPH4gbWxk?feature=shared]

## Introduction:

Hi! This is the team EatChiwi, a team of 3 students of the Vocational Superior School Benjamin Harrison of Cayey, Puerto Rico. We are a dedicated team that is participating on the WRO 2026 competition on the category of Future Engineer's. Our dedication in this team work project was the key to the development of our vehicle. All the parts that make up the car (chassis, mechanics, axles, etc.) were designed by our trusted mechanical engineer Efrain Ortiz. All the parts designed were printed using PETG and PLA filaments with the Creality 3 v3 ke and Dremel 3d45 printers. The design of the car it's a squeletical design to be quicker to print, modify or change anything in case of be needed. The brain of the car consists of the microcontroller MOTION PRO RP2350 which is a versatile 30 programmable pin board capable of more than what we need it for. Alongside that, we have 2 APDS9960 color sensors and 2 TMF8821 distance sensors on the front, vl53l0x distance sensors on each side of the car, and a bno08x sensor for the orientation on top.

Team Photo (from left to right)
===
- Efrain Ortiz (18) - current senior and our trusted mechanic. Responsible of the creation of the models of the vehicle and the car itself. He's a real innovator and main strategist.
- Faneshka Cartagena (17) - current junior and is the person dedicated to take note of everything. She's a very dedicated and creative person. Responsible of all the documentation of the creating and thinking process. 
- Jose Ortiz (16) - current junior and the programmer of the group. Responsible of the creation of the program of the vehicle and the one in charge to make the strategy come to life.
<table>
    <tr> 
        <td> <img src = "T-Photo\Photo Team EatChiwi.jpg" width ="400" height ="300">
        </td> 
        <td> <img src = "T-Photo\Photo Team EatChiwi (2).jpg" width ="400" height ="300">
        </td>
        </tr>
    </table>

V-Photo
===

## V-1.4 (Apr/29/26)
<table>
    <tr> 
        <td> <img src = "V-Photo\V-Photo Version_1.4\V-1.4_Back.jpeg" width ="400" height ="300">
        </td> 
        <td> <img src = "V-Photo\V-Photo Version_1.4\V-1.4_Bottom.jpeg" width ="400" height ="300">
        </td>
    </tr>
    <tr> 
        <td> <img src = "V-Photo\V-Photo Version_1.4\V-1.4_Left.jpeg" width ="400" height ="300">
        </td>
        <td> <img src = "V-Photo\V-Photo Version_1.4\V-1.4_Top.jpeg" width ="400" height ="300">
        </td> 
    </tr>
    </table>

## About the Mechanics:

The design of the car it's an compact design created in this way to be more quicker to print and more easy to avoid obstacules. The measurements of the car are: lenght = 25cm, width = 11.5cm, tall = 9cm. The car is RWD drived by a TT motor and a MG996r servo motor for steering. The brain of the car is the microcontroller MOTION PRO RP2350. The car counts with 4 wheels of 51mm, 2 apds9960 on front, 2 tmf8821 on front, vl53l0x sensors on each side and a bno08x for orientation. On the top, just below the microcontroller it's the battery that have a capacity of 37W/h and can supply 35W continuos and counts with a capacity of 10,000mAh.

## About the Code:

Our robot is an autonomous robot programed to complete the Future Engineer's track. To program the robot, the IDE we use is Thonny. To create the code we're using different libraries and sensors:

- `vl53l0x` - https://github.com/uceeatz/VL53L0X/tree/master
- `apds9960` - https://github.com/liske/python-apds9960/tree/master
- `tmf8821` - EJOM CODE @Dde567
- `servo` - EJOM CODE @Dde567
- `dcmotor` - https://github.com/cnadler86/MicroPython_Motor/tree/master
- `bno08x` - https://github.com/dobodu/BOSCH-BNO085-I2C-micropython-library/tree/main

To upload the code to the microcrontoller: connect the microcontroller to your computer using a USB cable. Turn it on, then open your IDE (in our case, Thonny) and make sure the microcontroller is recognized. Press the right click on the program you want to upload and select save. Once saved, the code is successfully uploaded to the microcontroller.
