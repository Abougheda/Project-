from roboticstoolbox import Bicycle, RandomPath, VehicleIcon,RangeBearingSensor,LandmarkMap
from math import pi , atan2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.io import loadmat
import numpy as np

Robot_initial=(input("Please enter the robot's start coordinates as x  y: "))
initial_pos=Robot_initial.split()
initial_angle=(input("Please enter the robot's initial angle in radians: "))
obs = int(input('Enter the number of obstacles: '))
Target_Coordinates=(input("Please enter the target coordinates as x  y: "))
Target_Coordinates=Target_Coordinates.split()

#Robot's initialization
anim = VehicleIcon('/home/parallels/Desktop/robot', scale = 5)
veh = Bicycle(
animation = anim,
control = RandomPath,
dim = 10,
x0 = [int(initial_pos[0]),int(initial_pos[1]),initial_angle]
)


veh.init(plot=True)

#Target design and coordinates
goal=[float(Target_Coordinates[0]),float(Target_Coordinates[1])]
goal_marker_style = {
    'marker': 'D',
    'markersize': 5,
    'color': 'b'
}

plt.plot(goal[0],goal[1],**goal_marker_style)


#initialization of map

map = LandmarkMap(obs,50)
map.plot()
image = mpimg.imread('map.png')
plt.imshow(image, extent = [-50,50,-50,50])

sensor=RangeBearingSensor(robot=veh,map=map,animate=True)
print('Sensor Readings: ', sensor.h(veh.x))

#Function that detects the obstacle near the car and direction that the car will choose to avoid it
def detect_obstacles(readings):
    for i in readings:
        if i[0]<2:
            print('Obstacle ahead') 
            veh.x[2]+=2

#Function that moves the car to target and update angle to goal
def ON():
    goal_heading=atan2(
    (goal[1]-veh.x[1]),(goal[0]-veh.x[0])
    )
    steer = goal_heading-veh.x[2]
    veh.step(2,steer)
    veh._animation.update(veh.x)
    plt.pause(0.005)
    
    
#Funtion that checks that the car reached the target
def condition_target():
    if ((abs(goal[0]-veh.x[0])<0.45) and (abs(goal[1] -veh.x[1])<0.45)): #distance between the robot and the target
        return True
    else:
        return False

run=True
while(run):
    if not condition_target():
        ON()
    
        detect_obstacles(sensor.h(veh.x))
        if condition_target() is True:
            run=False
            print('you have reached your target!')
        else:
             run= True
    else:
        ON()
        detect_obstacles(sensor.h(veh.x))
        if condition_target() is True:
          run=False
        
#Run robot  for interval seconds
veh._animation.update(veh.x)
plt.pause(1000)

