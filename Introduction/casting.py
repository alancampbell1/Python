"""
Python Casting


There will be times when you want to specify a type onto a variable. This can be done
with casting. 
Python is object-orientated and it uses classes to define data types, incl primitive types.

Casting is done using constructor functions
"""

x = int(1)		# x will be 1
y = int(2.8)	# y will be 2
z = int("3")	# z will be 3

x = float(1)		# x will be 1.0
y = float(2.8)		# y will be 2.8
z = float("3")		# z will be 3.0
w = float("4.3")	# w will be 4.3

x = str("s1")		# x will be 's1'
y = str(2)			# y will be '2'
z = str(3.0)		# z will be '3.0'

"""
String literals are surrounded by single or double quotation marks
'hello' is the same as "hello"

Strings in python are an array of elements

Python does not have a single character type, like a char. To access single elements
in a string we use the [].
"""

a = "Hello, World"
print(a[1])			#prints e

b = "Hello, World"
print(b[2:5])		#prints llo, characters from position 2 to 5 (not included)

#The strip() function removes any whitespace from the beginning to the end
a = " Hello, World "
print(a.strip())


#len method returns the length of a String
a = "Hello World"
print(len(a))


#upper() method returns the string to uppercase
a = "Hello World"
print(a.upper())

#replace() method replaces a string with another string
a = "Hello World"
print(a.replace("H", "J"))

#split() splits a string into substrings if it finds instances of a separator
a = "Hello, World"
print(a.split(","))


"""
Python allows for command line input. This means it asks the user for an input
In the following example, it asks for the user's name, by using the input() method
"""

print("Enter your name")
a = input()
print("Hello, " + a)





