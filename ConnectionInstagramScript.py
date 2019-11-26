
class LoginError(Exception):
   """No need to login in account"""
   pass

import os

while True:
  try:
    os.system("pip3 install urllib3")
    os.system("pip3 install bottle")
    username = "restaurantvibess"
    os.system("rm -rf pictures")

    os.system("pip3 install instaloader")
    string = "instaloader %s"%(username)
    os.system(string)

    string = "mv %s pictures"%(username)
    os.system(string)
    raise LoginError
    break
  except LoginError:
    print("Downloaded completed, No need for login")
    print("")
    break
