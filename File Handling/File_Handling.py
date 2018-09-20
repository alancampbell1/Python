"""
Python File Open

File Handling is an important part of any Web Application. Python has several functions
for creating, reading, updating and deleting files.

The main function for working with files in Python is the open() function.
open() takes two parameters: filename and mode.
There are 4 different methods/modes for opening a file:
"r" - Read - Default value. Opens a file for reading, error if file not found
"a" - Append - Opens a file for appending, creates the file if it doesn't exist
"w" - Write - Opens a file for writing, creates the file if it doesn't exist
"x" - Create - creates a specific file, returns an error if the file exists already
"""

#The following reads in a file located in the same folder

f = open("demoFile.txt")

#An alternative to the above is in the following, r for 'read', t for 'text'

g = open("demoFile.txt", "rt")