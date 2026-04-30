# Code Explanation 

 In this document you'll find all the explanation of the code, system thinking and decision making.

## About the Code 

The robot's code is designed so that it can complete all the challenges of the WRO Future Engineers 2026 competition circuit. This code was created on Thonny, an IDE for Phyton and in this case, used for microphyton. The microcontroller we used is the MOTION PRO RP2350.

## The Code 

The code itself begins like this: at the start, it imports all the libraries. After that, it sets up the communication channels and the buttons, along with other functions. Then, the robot verifies the communication channels before defining the different sensors and functions.

After that, the code starts creating and defining the functions, as well as calculating or compensating values. Once this is done, the robot begins running, centering the wheels and reading all the data in order to calculate where it will move and how much it will move.

## System Thinking 

The robot’s critical thinking works like this: at the beginning, the robot reads everything to determine where it is located and where it needs to move. Then, it starts moving forward to detect a larger distance. This is because the robot checks both distances and moves toward the one with the greater value, since that indicates more open space (in other words, not a wall). For example, if the left distance sensor detects a greater distance than the right one, the robot will move to the left.

After moving in the corresponding direction, the robot will center itself by reading both distances and calculating an average so it can stay in the middle. To verify that it moved in the correct direction, the robot uses an orientation sensor, which indicates how many degrees it has turned and whether it is moving straight or in a curve.

The robot will also detect any walls in front of it and stop before crashing. If it detects a wall ahead, it will reverse for approximately 1 to 1.5 seconds. This would be the full behavior on a track without obstacles.

On a track with obstacles, the robot follows the same logic, but additionally uses the front distance sensors while it is between two walls (it determines this when both distances are similar and the average is not very large). If the robot detects an object, it will approach it to identify its color. If the obstacle is red, the robot will pass on the right side of the block; if it is green, it will pass on the left side.
To know when it has completed three laps, the robot keeps count of how many times it detects a larger distance or how many times it turns in a certain direction. In total, there would be 12 turns, since the track is square and each lap represents 4 turns.