# Mechanical Engineer

In this document you'll find all the things related to the mechanical engineer like the mobility system, components of the car, and others.

## About Our Car

Our trsuty EC26 is a rear wheel drive vehicle designed entirely our mechanical engineer with Fusion 360 CAD software. This modular vehicle was made with upgradeability and reliability in mind. This is the smallest design made by me (Efrain Ortiz) and the best so far. Its composed by a custom made differetial and steering system (in this case a rack and pinion) drived by a plastic gearbox 1:48 TT motor (the yellow gearbox) and a MG996R servo motor for positional precision on the steering drive.

## Current Model Photos (V-1.5)
<div align='center'>
<table>
    <tr> 
        <td> <div style="position: relative; display: inline-block;">
        <!-- Image -->
         <img src="../V-Photo/V-Photo Version_1.5\V-1.5_Bottom.jpg" alt="Accessibility description" width ="300" height ="300" style="display: block;">
  <!-- The Text Overlay -->
  <div style="
    position: absolute; 
    top: 10px; 
    left: 10px; 
    background-color: rgba(0, 0, 0, 0.79); 
    color: white; 
    padding: 8px 12px; 
    font-family: sans-serif;
    border-radius: 10px;">
    <b> Bottom </b>
  </div>
</div>
        </td> 
        <td> <div style="position: relative; display: inline-block;">
        <!-- Image -->
         <img src="../V-Photo/V-Photo Version_1.5\V-1.5_Back.jpg" alt="Accessibility description" width ="300" height ="300" style="display: block;">
  <!-- The Text Overlay -->
  <div style="
    position: absolute; 
    top: 10px; 
    left: 10px; 
    background-color: rgba(0, 0, 0, 0.79); 
    color: white; 
    padding: 8px 12px; 
    font-family: sans-serif;
    border-radius: 10px;">
    <b> Back </b>
  </div>
</div>
        </td>
        <td> <div style="position: relative; display: inline-block;">
        <!-- Image -->
         <img src="../V-Photo/V-Photo Version_1.5\V-1.5_Front.jpg" alt="Accessibility description" width ="300" height ="300" style="display: block;">
  <!-- The Text Overlay -->
  <div style="
    position: absolute; 
    top: 10px; 
    left: 10px; 
    background-color: rgba(0, 0, 0, 0.79); 
    color: white; 
    padding: 8px 12px; 
    font-family: sans-serif;
    border-radius: 10px;">
    <b> Front </b>
  </div>
</div>
        </td>
    </tr>
    <tr> 
        <td> <div style="position: relative; display: inline-block;">
        <!-- Image -->
         <img src="../V-Photo/V-Photo Version_1.5\V-1.5_Left.jpg" alt="Accessibility description" width ="300" height ="300" style="display: block;">
  <!-- The Text Overlay -->
  <div style="
    position: absolute; 
    top: 10px; 
    left: 10px; 
    background-color: rgba(0, 0, 0, 0.79); 
    color: white; 
    padding: 8px 12px; 
    font-family: sans-serif;
    border-radius: 10px;">
    <b> Left </b>
  </div>
</div>
        </td>
        <td> <div style="position: relative; display: inline-block;">
        <!-- Image -->
         <img src="../V-Photo/V-Photo Version_1.5\V-1.5_Top.jpg" alt="Accessibility description" width ="300" height ="300" style="display: block;">
  <!-- The Text Overlay -->
  <div style="
    position: absolute; 
    top: 10px; 
    left: 10px; 
    background-color: rgba(0, 0, 0, 0.79); 
    color: white; 
    padding: 8px 12px; 
    font-family: sans-serif;
    border-radius: 10px;">
    <b> Top </b>
  </div>
</div>
        </td>
        <td> <div style="position: relative; display: inline-block;">
        <!-- Image -->
         <img src="../V-Photo/V-Photo Version_1.5\V-1.5_Right.jpg" alt="Accessibility description" width ="300" height ="300" style="display: block;">
  <!-- The Text Overlay -->
  <div style="
    position: absolute; 
    top: 10px; 
    left: 10px; 
    background-color: rgba(0, 0, 0, 0.79); 
    color: white; 
    padding: 8px 12px; 
    font-family: sans-serif;
    border-radius: 10px;">
    <b> Right </b>
  </div>
</div>
        </td>
    </tr>
    </table>
  </div>

## Mechanical explanation

### The body (chassis)

  - The chassis was designed AROUND the drive train, this means that we made sure everything has a space before designing the body, the only exception is the oval shape on the differential area that was added later because we had to rework the differential multiple times. THe chassis was made modular for this same purpose, to be easily modified. Also print times and quality are highly improved with a modular design as it can be oriented in ways it takes less support and less movement on the Z axis(up/down).

  ![alt text](image-1.png)

### Drive train

  - The car is rear wheel drive for a simple reason, simplicity. Rear wheel drive does not require rotations a angles in this type of vehicle, so it is more simple as we can skip designing universal jonts. The way the car moves is through a differential drived by a TT motor(1:48), everything except the motor is 3d printed. Another detail is that both axle sides are not the same, this is a trade-off as we decided to prioritize time over comfort because of the problems with the differential.
 

### Steering design

  - The steering was another headache to make, like the differential, it was also reworked multiple times. But it came up to be a rack and pinion system for stability, presicion and just looks cooler. Even though we tried to achive ackermann steering it got messed up when we decided to acommodate the servo upfront, but after testing we realised it did not really matter much at that scale, maybe you get outer wheel 1 or 2 degrees of more turn which you cant even see on track. As it was not a issue we did not waste time correcting it.    



## Design Trade-Off

Some trade offs can be found on the steering system, differential, chassis design and choice of actuators

### Steering System

  - Some common problems with a rack and pinion system is space, it takes more space than other more simple methods, but it also has a better torque transfer and is very stable. our design also has a limited turn radious (~25° to 30°) but this can be modified with the gear ratio and rack length. This isnt really a limiter factor at our aplication as it has not given us much trouble at the challenge.

### Differential

  - Limited max speed as the differential itself lacks bearings and can melt on higher speeds (~200rpm+) even if greased (which is the highly recomended), this was tested by us using a drill to spin the gears at speeds higher than 500rpm (~1000 to 1500 rpm during 1 minute) and surprisingly the differential was still working even after some melting. Our choice of designing our own differential was more of a personal challenge to learn than an actual strategic desicion for better performance, still the results do satisfy our needs in the challenge.

      ![alt text](image.png)

### Chassis design

  - The choice of making the chassis a modular one make us be able to modify parts of the chassis without having to print the whole thing again. The chassis may look a little funny as it contains some big ovals at the differential place, this is because making the differential smaller was taking too much time mainly because of problems with the print quality at small scales with a .4mm noozle. The only trade off of this whacky design is just it being more prone to braking, otherwise is just some stetic preference.



## Speed/torque reasoning
On top is the microcontroller MOTION PRO RP2350 and below of it is the battery. Before the front part is located the TT motor and the MG996r servo motor for steering, and on top of it is located the BMI270 for the orientation. On both sides the car counts with the TMF8821 sensor to read distance. On the front the car counts with 2 TCS3472 for color reading and 2 TMF8821 for distance reading. 

## Mechanical components of choice

  ## MG996r
    -The choice of this bulky space taking servo motor was mainly that the sg90 servos tended to break or burn easily, it was so frequent we had more than 7 servos that were just broken. It is sturdy, reliable and more precise and stable than micro servos, and there is space, so why not.
