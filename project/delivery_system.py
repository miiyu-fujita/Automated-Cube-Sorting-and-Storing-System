#!/usr/bin/env python 3
"""
delivery_system.py
*** TO DO ***

Author: Muqtadir Ahmed
Date: March 15th, 2022
"""
"""
This class contains the functions that would be used for the delivery process of the system
"""
from utils.brick import configure_ports


def move_requested_cube(motor):
    motor.set_position_relative(360) # move the motor 360 degrees to push the cube and return to the initial position

def remove_delivered(color, angle, dictionary):
    dictionary[color].remove(angle)