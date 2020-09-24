#!/usr/bin/python

import os
import shutil

dirPath = "."

for fileName in os.listdir(dirPath):
	print "Removing " + dirPath+"/"+fileName
	if os.path.isdir(dirPath+fileName) and fileName != "." and fileName != "..": 
		os.system("rm -rf "+dirPath+"/"+fileName+"/*")
