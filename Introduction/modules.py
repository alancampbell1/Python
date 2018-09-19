"""
Python Modules:

A module can be considered as a code library.
Its a file containing a set of functions you can include in your application

To create a Module, just save the file with the extension .py
Look to myModule.py for a sample module.

To use a Module we need to import it using the following statement
"""

import myModule


#From here you can reference the functions available in the module
myModule.greeting("Alan")

#You can get access to variables contained in the module too

a = myModule.person1["age"]
print(a)

#module names can be aliases too
import myModule as mx

b = mx.person1["name"]
print(b)


#Python has several in-built modules in Python, which can be imported whenever you want

import platform

x = platform.system()
print(x)				#Prints system name, Darwin

#The dir() built-in function lists all function names in a module

x = dir(platform)
#print(x)

#You also do not need to import the entire module but select parts. The following
#only imports the person1 dictionary.


from myModule import person1
print(person1["age"])








