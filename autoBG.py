# You will see it if configfile won't be in it's place at runtime. :\
NOFILEERROR = "AutoBG-script shouts : couldn't find my config file! Exiting."
# This will be printed in case of some problem with feh's work:
FEHUNEXPECTEDERROR = "AutoBG-script says: There was some unexpected problem running feh."
# Here is a no-directory-found-error text:
NOTADIRECTORYERROR = "AutoBG-script says: Specified parameter is not a directory! Exiting."
# Feel free to change it, but also put your config file in pointed place. :)
configDir_inhome = "/.scripts/autoBG/config.py" # must be a script just to set IMAGESPATH variable like "IMAGEPATH = /home/images/wallpapers"
# (".py" in configfile's name is not essential)
#  !!WARNING!!  
# In wallpaperFolder there must be images only. Read feh's documentation for knowing about supported types.

import os
import sys
from random import random

HOMEDIR = os.getenv("HOME")
configDir = HOMEDIR + configDir_inhome

def SetWallBG(pathToImage):
	return(os.system("feh --bg-fill " + pathToImage))
def TakeImageFromFolder(pathToFolder):
	return(pathToFolder + "/" + os.listdir(pathToFolder)[round(random()*(len(os.listdir(pathToFolder))-1))])

if(len(sys.argv) == 2):
	if(os.path.isdir(sys.argv[1])):
		rez = SetWallBG(TakeImageFromFolder(sys.argv[1]))
		if(rez > 0):
			print(FEHUNEXPECTEDERROR)
	else:
		print(NOTADIRECTORYERROR)
else:
	if(os.path.isfile(configDir)):
		exec(open(configDir).read())
		if(os.path.isdir(IMAGESPATH)):
			rez = SetWallBG(TakeImageFromFolder(IMAGESPATH))
			if(rez > 0):
				print(FEHUNEXPECTEDERROR)
	else:
		print(NOFILEERROR)
