"""
Python Delete File:

To delete a file, you must import the OS module and run its os.remove() function:
"""

import os
os.remove("myfile.txt")


#To avoid errors you can check if the file exists using an if else expression:

if os.path.exists("myfile.txt"):
	os.remove("demofile.txt")
else:
	print("The file does not exist")


#To delete an entire folder, you use the following
os.rmdir("myfolder")