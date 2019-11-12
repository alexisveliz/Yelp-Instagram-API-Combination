#script that gets keywords from yelp, passes and converts it into search  location command for the api
# Implementation Alejandro, Haley Anderson and Elise May

import os

username = "restaurantvibess"
os.system("rm -rf pictures")

os.system("pip3 install instaloader")
string = "instaloader %s"%(username)
os.system(string)

string = "mv %s pictures"%(username)
os.system(string)
