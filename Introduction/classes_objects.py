"""
Python Classes and Objects:
Python is an object oriented programming language.
Almost everything in Python is an object with properties and methods
A class is like an object constructor or a 'blueprint' for creating objects
"""

#To create a class we use the keyword class

class myClass:
	x = 5

#From here, you can use the class myClass to create objects
p1 = myClass()
print(p1.x)


"""
Classes become useful when we use the __init__() function
All classes have a function called __init__() which is always executed when a class
is initiated (i.e. created)

We use the __init__() function to assign values to object properties or other operations
that are necessary to do when the object is being created
"""

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myFunc(self):
		print("Hello my name is " +self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myFunc()

"""
self is an import keyword in Python. The self parameter is a reference to the class instance
itself and is used to access variables that belong to the class.
Similiar to the "this" keyword in Java. They are used to access the variable associated
with the current instance.

In Python, self can be renamed to anything but best practice means self is the keyword
"""

#Modify properties on an object
p1.age = 26

#Delete properties on an object
del p1.age

#Completely delete objects
del p1




