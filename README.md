# WRO_EATCHIWI_PR_2026

Engineering materials
====

This repository contains the documentation of the team EatChiwi on the challenge of creating a self-driving vehicle. Here you're going to find all about the creation of the vehicle: mechanical parts, programation, and system thinking. 

## Table of Content :

* `Code-Development` code of the robot.
    * `Codes` contains the libraries used to create the code of the robot.
* `Electrical-Specs` schematic diagrams of the electrical components of the robot.
    * `HardwareCADS` 3d files the vehicle hardware (electrical components).
* `Journal` register of the things we do on the days we work on the robot.
* `Mechanics` schematic diagrams of the mechanical components of the robot.
    * `CAD` contains 3D files used for the robot.
* `T-photos` photos of the team.
* `V-photos` contains photos of the differents versions of the robot.
* `Video` contains a link to a video where is a driving demostration of our robot.

## Introduction:

Hii this is EAT CHIWI, we are a team of 3 from the Vocational School Benjamin Harrinson of Cayey. Our dedication to this project team work was the key to the development of our vehicle. This compact but reliable vehicle runs on RWD drived by a trusty TT motor and a MG996r servo motor for steering. The brain of the car consists of the microcontroller MOTION PRO RP2350 which is a versatile 29 programmable pin board capable of more than what we need it for. Alongside that we have our trusty vl53l0x sensors for distance on each side and 2 apds9960 color sensors on front for a wider detecting range. Our chassis, mechanics, axles etc. are all designed and made by our mechanical engineer and printed using PETG and PLA filaments with the Creality 3 v3 ke and Dremel 3d45 printers

V-Photos
===

## V-1.0 (Feb/21/26)
This design was made using 3D printing. It is a small vehicle that has an ultrasonic sensor to detect when it should turn the front wheels. On top of the robot, the battery is located, and above that is the Maker Pi controller, which processes all the data. This model doesn't detect colors.
<table>
    <tr> 
        <td> <img src = "V-Photo\V-Photo Version_1.0\V-1.0_Bottom.jpg" width = "400" height = "300">
        </td> 
        <td> <img src = "V-Photo\V-Photo Version_1.0\V-1.0_Left.jpg" width = "400" height ="300">
        </td>
    </tr>
    <tr> 
        <td> <img src = "V-Photo\V-Photo Version_1.0\V-1.0_Right.jpg" width ="400" height ="300">
        </td> 
        <td> <img src = "V-Photo\V-Photo Version_1.0\V-1.0_Top.jpg" width ="400" height ="300">
        </td>
    </tr>
    </table>

## V-1.1 (Mar/28/26)
 This model is made using 3D-printed materials and is very similar to the previous design. It includes an ultrasound sensor on the left side, although it is not programmed yet.

This version uses a different differential, which is larger than the one in the previous design. On top of the vehicle, the battery is mounted along with the Maker Pi controller, where all the robot’s data is processed. Overall, this model is a simpler version of the design.

<table>
    <tr> 
        <td> <img src = "V-Photo\V-Photo Version_1.1\V-1.1_Back.jpg" width ="400" height ="300">
        </td> 
        <td> <img src = "V-Photo\V-Photo Version_1.1\V-1.1_Bottom.jpg" width ="400" height ="300">
        </td>
        <td> <img src = "V-Photo\V-Photo Version_1.1\V-1.1_Front.jpg" width ="400" height ="300">
        </td> 
    </tr>
    <tr> 
        <td> <img src = "V-Photo\V-Photo Version_1.1\V-1.1_Left.jpg" width ="400" height ="300">
        </td>
        <td> <img src = "V-Photo\V-Photo Version_1.1\V-1.1_Right.jpg" width ="400" height ="300">
        </td> 
        <td> <img src = "V-Photo\V-Photo Version_1.1\V-1.1_Top.jpg" width ="400" height ="300">
        </td>
    </tr>
    </table>

## V-1.2 (Apr/10/26)
This model is made using 3D printing materials. It includes an ultrasound sensor located on the left side of the model. The chassis has been redesigned because we changed the differential model, which required adjustments to the overall structure. On the top, you can see the battery, and above it is the Cytron Motion RP2350 Pro, where all the data is processed. At the front, there are two TMF8821 sensors used for distance detection, which are not programmed at the moment.
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

## About the Code:

Our robot is an autonomous robot programed to complete the Future Engineer's track. To program the robot, the IDE we use is Thonny. To create the code we're using different libraries and sensors:

- `vl53l1x` - https://github.com/drakxtwo/vl53l1x_pico/tree/main
- `vl53l0x` - https://github.com/uceeatz/VL53L0X/tree/master
- `apds9960` - https://github.com/liske/python-apds9960/tree/master
- `hcrs04` - https://github.com/rsc1975/micropython-hcsr04/tree/master
- `tmf8821` - EJOM CODE
- `servo` - EJOM CODE 
- `dcmotor` - https://github.com/cnadler86/MicroPython_Motor/tree/master
- `bno08x` - https://github.com/dobodu/BOSCH-BNO085-I2C-micropython-library/tree/main

To upload the code to the microcrontoller: connect the microcontroller to your computer using a USB cable. Turn it on, then open your IDE (in our case, Thonny) and make sure the microcontroller is recognized. Press the right click on the program you want to upload and select save. Once saved, the code is successfully uploaded to the microcontroller.
