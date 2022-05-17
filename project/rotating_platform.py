#!/usr/bin/env python 3
"""
rotating_platform.py
*** TO DO ***

Authors: Muqtadir Ahmed, Miiyu Fujita
Date: March 9th, 2022
"""
"""
This class contains the function that would be used for the the rotating platform subsytem
"""
# move motor to the target location by choosing the motor and the desired position in angle as parameters
def move_motor(motor, angle):
    if angle >= 180:
        motor.set_position(360 - angle)
    else:
        motor.set_position(0 - angle)

