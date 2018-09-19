"""
Python Lambda
The Lambda function is a small anonymous function. It can take any number of arguments
but can only have one expression.

Syntax:
lambda arguments: expression
"""

#The following example adds 10 to the number passed in as an argument and prints the 
#result
x = lambda a : a + 10
print(x(5))


#Lambda functions can take any number of arguments
x = lambda a, b : a * b
print(x(5, 6))

"""
Why use lambda?:
The power of this function comes from when you use it as an anonymous function inside
another function.

The following is an example of this:

"""

def myfunc(n):
	return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))