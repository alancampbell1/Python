"""
Python Conditionals

Python supports the usual logical conditions from Mathematics incl:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than a > b
Greater than or equal to: a >= b
"""

#Basic if statement
a = 33
b = 2000
if b > a:
	print("b is greater than a")

#Remember, Python relies on indentation to define scope

#elif is a python keyword of Java's else if statement

a = 33
b = 33
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")

#else is used to catch anything that doesn't satisfy the previous conditionals

a = 200
b = 33
if b > a:
	print("b is greater than a")
elif b == a:
	print("a and b are equal")
else:
	print("a is greater than b")

#Note you don't have to always use elif, same as not having to use else if in Java


#A short hand if is a conditional and statement on a single line like so
a = 5
b = 2
if a > b: print("a is greater than b")

#The AND keyword is a logical operator used to combine conditional statements
#Both need to be true to excute the code
a = 10 
b = 5
c = 15

if a > b and c > a:
	print("Both conditionals are true")

#The OR keyword is a logical operator and used to combine conditionals
#Only a single conditional needs to pass for the code to execute

if a < b or a < c:
	print("At least one of the conditions is true")

