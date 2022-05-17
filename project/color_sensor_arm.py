#!/usr/bin/env python 3
"""
color_sensor_arm.py
*** TO DO ***

Authors: Muqtadir Ahmed, Miiyu Fujita
Date: March 15th, 2022
"""
"""
This class contains the necessary functions used by the color sensors of the enitire system
"""


def most_occured(List):
    # create a list with keys as color names and values as number of occurences in the array
    count_dict = {
        "Red": 0,
        "Green": 0,
        "Blue": 0,
        "Unknown": 0
    }

    for color in List:
        if color in count_dict: # if color is either red green or blue
            count_dict.update({color:count_dict[color]+1}) # increment color occurence by 1
        else:
            count_dict.update({"Unknown":count_dict["Unknown"]+1}) # incrememnt unknown by 1 if its neither of the rgb colors
    # find max value in dict
    max_count = max(count_dict.values())
    # find corresponding color in dict 
    color_list = list(count_dict.keys()) # ["red", "green", "blue"]
    index_color = list(count_dict.values()).index(max_count) 
    likely_color = color_list[index_color] 

    return likely_color

"""
function to get requested color from color sensor arm 
Nour should implement this in another class, but
we have defined it for testing purposes (just for now)
"""
def get_requested_color(color_sensor):
    color_readings = []
    while len(color_readings) <= 20: 
    # read 20 color samples 
        color_readings.append(color_sensor.get_color_name())
    # find color that occurs most in readings 
    color_read = most_occured(color_readings)
    #print(color_read)
    return color_read


"""
translate requested color to needed motor angle 
"""
def color_to_angle(color, dictionary):
    # get the list of angles from the dictionary 
    list_of_angles = dictionary[color]
    if len(list_of_angles) == 0:
        #print("out of stock")
        return -1
    else:
        
        color_angle = dictionary[color][0]
        print(dictionary)# check if angle was removed
        return color_angle