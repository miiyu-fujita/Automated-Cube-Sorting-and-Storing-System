#!/usr/bin/env python 3
"""
input_tower.py
*** TO DO ***

Authors: Muqtadir Ahmed
Date: March 15th, 2022
"""
"""
This class contains the functions that would be used by the input tower components of the system
"""

#Push the cube onto the platform
def move_cube_to_platform(motor):
    motor.set_position_relative(360) # move the motor 360 degrees to push the cube and return to the initial position

def store_cube_color_and_angle(color, angle, dictionary): 
    dictionary[color].append(angle) #add the angle to the dictionary of colors and angles

def move_platform(platform_motor):
    platform_motor.set_position_relative(-60) #rotates the motor by -60 degrees relative to current position