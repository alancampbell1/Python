"""
Python Tuples

A tuple is a collection which is unordered and unchangeable. In Python tuples are written 
with round brackets.


"""

thisTuple = ("apple", "pear", "banana")
print(thisTuple)

#You can access a tuple value by referring to its index number
print(thisTuple[0])

"""
Once a tuple has been created you cannot change its value
thisTuple[0] = "orange"
"""


#You can use a loop to iterate through a tuple
for x in thisTuple:
	print(x)

#You can use the len() method to determine the length of a tuple

print(len(thisTuple))

"""
You cannot add items to a tuple
You cannot remove items from a tuple
However, you can completely delete the tuple 
"""

del thisTuple

#You can use the tuple() constructor to create a tuple

newTuple = tuple(("apple", "banana", "cherry"))
print(newTuple)


"""
Python has two in-built methods that can be used on Tuples
count() - returns the number of times a specified value occurs in a tuple
index() - searches a tuple for a specified value and returns its position
"""

x = newTuple.count("pear")
print(x)						#returns 0 if not found and 1 if found

y = newTuple.index("banana")
print(y)

