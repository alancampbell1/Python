"""
Python Try Catch

A try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try/catch blocks

When an error occurs, aka an exception, Python normally stops and generates an error message.
These exceptions can be handled using the try statement.

"""

#In this example, x is not known so the try block is skipped and the except block is printed.

try:
	print(x)
except:
	print("An Exception occurred")


#You can define as many exceptions as you want. These can be specific to the error caused
#in the try block

try:
	print(x)
except NameError:
	print("Value for x not known")
except:
	print("Some other error")

#An else block can be included to define a block of code to be executed if no errors are
#found

try:
	print("Hello")
except:
	print("something happened")
else:
	print("No errors found")

#Finally is a special block that is executed regardless of whether a try block raises an
#error or not

try:
	print(x)
except:
	print("Something bad happened")
finally:
	print("We will continue here")



