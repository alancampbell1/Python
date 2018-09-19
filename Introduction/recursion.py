"""
Python allows recursion, the process of a function calling itself

Recursion is a common programming concept. It has the benefit that you can loop
through data to reach a result.
"""

"""
In the following example we have a function called tri_recursion. It reads in a variable
k and checks if the value in k is greater than 0.
If so, a new variable 'result' stores k and a method call to tri_recursion is made passing
k - 1. Then printing the 'result' value to the screen
If k is greater than 0, it is defaulted in the else statement to 0 before being returned

Basically, the function keeps calling itself until k is reduced to being less than 0
"""


def tri_recursion(k):
	if k > 0:
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result

print("Recursion function")
tri_recursion(6)