#write a simple program that calculates the square root of number.
#prints the current date and time
#and displays the current working directory.

import math
import datetime
import os

#Calculate the square root of 30.
sqrt_value = math.sqrt(30)
print(f"Sqaure root of 30: {sqrt_value}")

#Get the current date and time
current_time = datetime.datetime.now()
print(f"Current date and time: {current_time}")

#Displays the current working directory
Current_directory = os.getcwd()
print(f"Current working directory: {Current_directory}")
