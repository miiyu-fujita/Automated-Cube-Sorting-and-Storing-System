#!/usr/bin/env python 3
"""
*** TO DO ***

Authors: Muqtadir Ahmed, Miiyu Fujita
Date: March 9th, 2022
"""
"""
This class contains the main method which would run the entire system. It also contains helper functions which are used in the main method.
"""

# imports
from time import sleep
from utils.brick import configure_ports, Motor, EV3ColorSensor, TouchSensor

import rotating_platform
import color_sensor_arm
import input_tower
import delivery_system
import gate_motor
# add imports here

# configure ports 
MOTOR_RP = Motor("D") # motor for rotating platform 
MOTOR_ARM = Motor("A") # motor for arm
MOTOR_DELIV = Motor("C") # motor for delivery
MOTOR_GATE = Motor("B") #motor for the gate
COLOR_SENSOR_R = configure_ports(PORT_1 = EV3ColorSensor) # request color sensor
COLOR_SENSOR_S = configure_ports(PORT_2 = EV3ColorSensor) # storing color sensor
TOUCH_SENSOR = configure_ports(PORT_3 = TouchSensor) #touch sensor to start the process
# add necessary sensors/motors here 

# define color : angle dictionary
color_angle_dict = {
    "Red":[],
    "Green":[],
    "Blue":[]
}
#set the current angle to 0
def reset_motor(motor):
    #motor.offset_encoder(motor.get_position())

    #if the above doesnt work
    motor.set_power(0)
    motor.reset_encoder() 
    
#get the angle at which the color is stored
def get_rp_angle(motor):
    return abs(motor.get_position()) #color always stored at the absolute value of the inner angle of the motor
    
#wait until the motor is stopped    
def wait_until_stopped(motor):
    sleep(0.1)
    while motor.is_moving() == True:
        continue

# main function
if __name__ == "__main__":
    #Poll touch sensor 10 times per second, if the touch sensor is pressed, then the program will start
    while TOUCH_SENSOR.is_pressed()== False:
        sleep(0.1)

    #set all the motors current angles to 0
    reset_motor(MOTOR_RP)
    reset_motor(MOTOR_ARM)
    reset_motor(MOTOR_DELIV)
    # set the maximum speed for the motors
    MOTOR_RP.set_limits(0,120)
    MOTOR_ARM.set_limits(0,200)
    MOTOR_DELIV.set_limits(0,180)
    MOTOR_GATE.set_limits(0,100)

    #STORING
    gate_motor.close_gate(MOTOR_GATE)
    for i in range(6): #stop once 6 cubes are placed
        while True:
            # get the color of the cube at the bottom of the tower
            color_r = color_sensor_arm.get_requested_color(COLOR_SENSOR_S)
            # If the color isn't in the available colors, then keep polling until the correct color is found
            if color_r == "Red":
                break
            elif color_r == "Blue":
                break
            elif color_r == "Green": 
                break
        input_tower.move_cube_to_platform(MOTOR_ARM) #Push the bottom cube on to the platform
        wait_until_stopped(MOTOR_ARM) #wait until the arm is done pushing
        sleep(0.5)
        MOTOR_GATE.offset_encoder(MOTOR_GATE.get_position()) #reset the motor gate
        MOTOR_GATE.set_limits(0,360)
        gate_motor.open_gate(MOTOR_GATE) #open the gate to let the cubes fall in front of the arm
        wait_until_stopped(MOTOR_GATE)  #wait until the gate is open
        sleep(0.5)
        gate_motor.close_gate(MOTOR_GATE) #close the gate to clamp onto the cube above the pushing arm
        platform_angle = get_rp_angle(MOTOR_RP) #get the angle of the rotational platform
        input_tower.store_cube_color_and_angle(color_r, platform_angle, color_angle_dict) # store the color of the cube and the angle at which its located onto the the dictionary
        
        print(platform_angle)
        print(color_angle_dict)
        input_tower.move_platform(MOTOR_RP) #move the platform by -60 degrees
        wait_until_stopped(MOTOR_RP) #wait until the rotating platform stops rotating

    #DELIVERING
    sleep(1)
    MOTOR_RP.set_position_relative(180) #rotate the platform by 180 degrees to shift the delivery 180 degrees away from the input tower
    wait_until_stopped(MOTOR_RP) #wait until the rotating platform stops rotating
    reset_motor(MOTOR_RP)
    MOTOR_RP.set_limits(0,180) #sweet spot for the speed of the rotating platform
    while True:
        print("Place the cube you desire into the request area and we will send it to you")

        while True:
            # get requested color from color sensor arm 
            color_r = color_sensor_arm.get_requested_color(COLOR_SENSOR_R)
            # If the color isn't in the available colors, then keep polling until the correct color is found
            if color_r == "Red":
                break
            elif color_r == "Blue":
                break
            elif color_r == "Green": 
                break
        # translate requested color to needed motor position angle, then remove that angle from dictionary if there is an angle
        motor_angle = color_sensor_arm.color_to_angle(color_r, color_angle_dict)
        if motor_angle == -1: #No more cubes of that color
            print("Out of stock, please choose a different color")
            sleep(2)
            continue
        else:
            print("Color found in our storage! Your cube is coming shortly.")
            # if supply exists determine angle and move motor to angle 
            rotating_platform.move_motor(MOTOR_RP, motor_angle)
            wait_until_stopped(MOTOR_RP)
            sleep(0.1)
            delivery_system.move_requested_cube(MOTOR_DELIV)
            wait_until_stopped(MOTOR_DELIV)
            delivery_system.remove_delivered(color_r, motor_angle, color_angle_dict) # remove the angle from the list since there is nothing at that list anymore
            print("We have the following in stock: ")
            print(color_angle_dict)
  