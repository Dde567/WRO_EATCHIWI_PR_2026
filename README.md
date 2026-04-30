# WRO_EATCHIWI_PR_2026

This repository contains the documentation of the team EatChiwi on the challenge of creating a self-driving vehicle. Here you're going to find all about the creation of the vehicle: mechanical parts, programation, and system thinking. 

## Table of Content :

* `Code-Development` code of the robot.
    * `Code-Development\codes` contains the libraries used to create the code of the robot.
* `Electrical-Specs` schematic diagrams of the electrical components of the robot.
    * `Electrical-Design\HardwareCADS` 3D files the vehicle hardware (electrical components).
* `Journal` register of the things we do on the days we work on the robot.
* `Mechanics` schematic diagrams of the mechanical components of the robot.
    * `Mechanics\CAD` contains 3D files used for the robot.
* `T-Photo` photos of the team.
* `V-Photo` contains photos of the differents versions of the robot.
* `Video` contains a link to a video where is a driving demostration of our robot.

##

|T-Photo | Links |
|--------|-------|
|Normal|[T-Photo\Photo Team EatChiwi.jpg]()|
|Crazy |[T-Photo\Photo Team EatChiwi (2).jpg]()|

|V-Photo | Links |
|--------|-------|
|V-1.0|[V-Photo\V-Photo Version_1.0]()|
|V-1.1|[V-Photo\V-Photo Version_1.1]()|
|V-1.2|[V-Photo\V-Photo Version_1.2]()|

## Introduction:

Hi! This is EatChiwi, we are a team of 3 from the Vocational Superior School Benjamin Harrison of Cayey. Our dedication to this project team work was the key to the development of our vehicle. This compact but reliable vehicle runs on RWD drived by a trusty TT motor and a MG996r servo motor for steering. The brain of the car consists of the microcontroller MOTION PRO RP2350 which is a versatile 30 programmable pin board capable of more than what we need it for. Alongside that we have our trusty vl53l0x sensors for distance on each side and 2 apds9960 color sensors on front for a wider detecting range. Our chassis, mechanics, axles etc. are all designed and made by our mechanical engineer and printed using PETG and PLA filaments with the Creality 3 v3 ke and Dremel 3d45 printers.

V-Photo
===

## V-1.2 (Apr/10/26)
This model is made using 3D printing materials. It includes an distant sensor (vl53l0x) located on the left side of the model. The chassis has been redesigned because we changed the differential model, which required adjustments to the overall structure. On the top, you can see the battery, and above it is the Cytron Motion RP2350 Pro, where all the data is processed. At the front, there are two TMF8821 sensors used for distance detection, which are not programmed at the moment.
<table>
    <tr> 
        <td> <img src = "V-Photo\V-Photo Version_1.2\V-1.2_Bottom.jpeg" width ="400" height ="300">
        </td> 
        <td> <img src = "V-Photo\V-Photo Version_1.2\V-1.2_Front.jpeg" width ="400" height ="300">
        </td>
        <td> <img src = "V-Photo\V-Photo Version_1.2\V-1.2_Front(1).jpeg" width ="400" height ="300">
        </td> 
    </tr>
    <tr> 
        <td> <img src = "V-Photo\V-Photo Version_1.2\V-1.2_Left.jpeg" width ="400" height ="300">
        </td>
        <td> <img src = "V-Photo\V-Photo Version_1.2\V-1.2_Top_Cytron Motion RP2350 Pro.jpeg" width ="400" height ="300">
        </td> 
        <td> <img src = "V-Photo\V-Photo Version_1.2\V-1.2_Top.jpeg" width ="400" height ="300">
        </td>
    </tr>
    </table>

## About the Mechanics

The design of the car it's an compact design created in this way to be more quicker to print and more easy to avoid obstacules. The measurements of the car are: lenght = 25cm, width = 11.5cm, tall = 9cm. The car is RWD drived by a TT motor and a MG996r servo motor for steering. The brain of the car is the microcontroller MOTION PRO RP2350. The car counts with 4 wheels of 51mm, 2 apds9960 on front, 2 tmf8821 on front, vl53l0x sensors on each side and a bno08x for orientation. On the top, just below the microcontroller it's the battery that have a capacity of 37W/h and can supply 35W continuos and counts with a capacity of 10,000mAh.



## About the Code:

Our robot is an autonomous robot programed to complete the Future Engineer's track. To program the robot, the IDE we use is Thonny. To create the code we're using different libraries and sensors:

- `vl53l0x` - https://github.com/uceeatz/VL53L0X/tree/master
- `apds9960` - https://github.com/liske/python-apds9960/tree/master
- `tmf8821` - EJOM CODE @Dde567
- `servo` - EJOM CODE 
- `dcmotor` - https://github.com/cnadler86/MicroPython_Motor/tree/master
- `bno08x` - https://github.com/dobodu/BOSCH-BNO085-I2C-micropython-library/tree/main

To upload the code to the microcrontoller: connect the microcontroller to your computer using a USB cable. Turn it on, then open your IDE (in our case, Thonny) and make sure the microcontroller is recognized. Press the right click on the program you want to upload and select save. Once saved, the code is successfully uploaded to the microcontroller.
