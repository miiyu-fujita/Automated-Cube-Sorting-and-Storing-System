#!/usr/bin/env python 3
"""
*** TO DO ***

Authors: Muqtadir Ahmed
Date: March 20th, 2022
"""
"""
This class contains functions that are used by the motor gate component of the input tower in order to open or close the gate.
"""
from time import sleep
from utils.brick import configure_ports, Motor

# Open the gate to let the cubes drop
def open_gate(motor):
    motor.set_limits(0,360)
    motor.set_position_relative(20)

#Close the gate to prevent the cubes from falling   
def close_gate(motor):
    motor.set_limits(0,360)
    motor.set_position_relative(-20)

    