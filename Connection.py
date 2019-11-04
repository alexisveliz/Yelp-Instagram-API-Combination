# Implementation by Haley Anderson and Elise May

import os

location = input("Where are you looking to eat?\nCurrently Supported Locations: Los Angeles, San Francisco, Seattle\nLocation: ")
term = input("What kind of food are you looking for?\nExamples: bars, dinner, Thai, etc\nResponse: ")

#os.system(python YelpAPI.py --term= %s --location= %s)

subprocess.call(["python YelpAPI.py --term=", term, " --location=", location])
