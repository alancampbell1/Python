"""
Python Functions:

A function is a block of code that only runs when it is called.
You can pass data into a function, known as parameters.
A function can also return data as a result
"""

#To create a function we use the keyword def

def myfunction():
	print("Hello Function")

#To call the function we type the name of the function and ()

myfunction()

#Information can be passed into functions using the parameters

def newFunction(x):
	print("Hello " + x)

newFunction("Alan")

#A function can have a default parameter value if none is provided

def anotherFunction(country = "Ireland"):
	print("I am from " + country)

anotherFunction("England")
anotherFunction()				#Defaults to Ireland

#A function can return a value into a variable like so

def returnFunction():
	return 5 * 4

x = returnFunction()
print(x)				#x is now assigned 20, 5 * 4

