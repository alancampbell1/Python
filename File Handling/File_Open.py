"""
Python File Open:

The following example reads in a file from the same location as the .py file using the 
open() function. Additionally, the read() function reads the contents of the file.
Printing the contents to the screen
"""

f = open("demoFile.txt", "r")
print(f.read())


#By default read() returns the whole text but you can also specify how many characters
#you want to return.

g = open("demoFile.txt", "r")
print(g.read(5))

#To return the first line use the readline() method:
print(f.readline())
#To print the second line we then call the same line again
print(f.readline())

#Alternatively, you can loop through the lines of a file line by line

a = open("demoFile.txt", "r")
for x in a:
	print(x)