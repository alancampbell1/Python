"""
Python File Write:

To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of a file
"w" - Write - will overwrite any existing content
"""

f = open("demoFile.txt", "a")
f.write("Now this file has an extra line")

#This line overwrites everything in the file

f = open("demoFile.txt", "w")
f.write("Whoops! I deleted everything")

"""
To create a new file we use the open() method with one of the following parameters:
"x" - Create - creates a file, returns a error if the file exists 

"a" - Append - creates a file if not already existing

"w" - Write - creates a file if it does not already exist
"""

#Creates an empty file called myfile
a = open("myfile.txt", "w")

