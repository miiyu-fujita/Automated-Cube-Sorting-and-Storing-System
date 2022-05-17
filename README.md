# ECSE211 Project: Team 1- Prof Ferri(e)'s Wheel

## Project Software Overview

Once the appropriate color is detected near the input tower's color sensor, the system will store the color and save the color and its location on the rotating platform in a dictionary. The storing process is complete when the software loops over the storing process six times to store the six cubes. Once its complete, the delivery process begins by polling the color sensor arm located near the request area for the correct colors. Once the valid color is detected, the location of the cube is taken from the dictionary in order to rotate the platform the right amount to bring the specific cube near the delivery area and then to deliver it. To run the program, simply click run in the class main_robot_ferris.py.

___

## Project Organization

- `lib`: contains libraries used by the robot such as
  the simpleaudio sound library.
- `project`: all Python files in this folder run on the robot.
  - [`doc`](project/doc): documentation for the brick API
  (Application Programming Interface), ie, the classes and functions
  you can use to work with the robot.
  - [`utils`](project/utils): brick-related utilities for this project.
  See the other project files to see examples of how to use these modules.
    - `brick.py`: the main module for interacting with the brick hardware.
    - `sound.py`: module that allows you to play sounds.
    It depends on the simpleaudio library.
  - [**`logic.py`**](project/logic.py): computations that can run on both
  the brick and the computer. Placing these in a separate file allows
  for testing on a computer, which can be faster than running on the brick.
  - [**`main_robot_ferris.py`**](project/main_robot_ferris.py):
  The class containing the main method that sorts and delivers the cubes is **main_robot_ferris.py**. The sorting is done by storing the detected color into a dictionary with a list of keys which correspons to the location at which the cube is being deposited on the rotating platform.
  main_robot_ferris imports five other classes called [**`gate_motor.py`**](project/gate_motor.py), [**`delivery_system.py`**](project/delivery_system.py), [**`input_tower.py`**](project/input_tower.py), [**`color_sensor_arm.py`**](project/color_sensor_arm.py), [**`rotating_platform.py`**](project/rotating_platform.py). Each class is named after the physical subsytem and their methods contain functions that control their specific subsystem.
- `scripts`:
  - `reset_brick.py`: If the program does not exit correctly, eg,
  if it is stuck in an infinite loop, this script can be run on the brick to reset it.
- `deploy_to_robot.py`: a script to deploy the code to the robot from a computer.
  It offers the following options:
  - Deploy DPM Project on Robot without running:
  copy the `project` folder to the robot.
  - Deploy and run DPM Project on Robot:
  copy the `project` folder to the robot and run the file specified
  in `project_info.json`.
  - Reset Robot: reset the robot.
- **`project_info.json`**: a file containing information about the project.
- `robot_setup.sh`: a script to install the required libraries on
the brick as described in the project instructions.
