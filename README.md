# Project-
Task 3 Computer Engineering
# Project Aim
The aim of this project is to make the robot not to interact with the obstacles on the map

# Dependancies required and software versions

1. Roboticstoolbox version 0.1.0
2. Python 3.6 or higher
3. VScode IDE
4. Ubuntu 18.04 LTS
5. Oracle VM VirtualBox

# Definition of user inputs:
- Robot_initial is input for the initial position of the robot
- initial_angle is input for the robot's initial angle
- obs is input for the number of obstacles that the user wishes to add
- Target_coordinates is input for the target coordinates

# Code Explanation
The code starts with taking input from the user regarding the robot's initial and a target position coordinates, as well as the number of obstacles.
A map is generated with randomly placed obstacles. The "ON" function is moves the target and updates the angle to goal. While ON is running the "detect_obstacles" function is using the readings from the RangeBearingSensor. The object will continue to move until it reaches the target.

# Evaluation 

# Results
The code has been tested with different initial, target positions and various numbers of obstacles<img width="1440" alt="Screen Shot 2022-12-08 at 8 21 19 PM" src="https://user-images.githubusercontent.com/114655121/206535249-a877519c-d300-4774-b561-415c6917d2e2.png">


# Limitation and Further Improvement 
- when the robot approaches an obstacle it spins around the obstacle and spins around itself, this can be fixed by adjusting the steer angle along with the speed.
- if a random obstacle happens to be right next to the target position, it will loop around itself and not stop at the target
- limitation of robot colliding with wall and how to fix this issue

# Project contributions
Ali Abou-Gheda worked on the "ON" and "condition target" functions
Mohamad Moamen worked on the initializations and imports for the codes
Kanzy Tawfik worked on the checking obstacles along with the while loop
