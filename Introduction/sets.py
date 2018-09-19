"""
Python Sets
A set is a collection which is unordered and unindexed. In Python, sets are written with
curly brackets {}
"""


thisSet = {"apple", "banana", "cherry"}
print(thisSet)


"""
You cannot access items in a set by referring to their index, since sets are unordered items
that have no index. 
Instead, you can use a for loop to loop through the set and ask if a specific value is
present in the set by using the 'in' keyword
"""

#print each value
for x in thisSet:
	print(x)

#check if banana is present in thisSet
print("banana" in thisSet)				#returns true or false

"""
Once a set is created you cannot change its items, but you can add new items using the 
add() method
"""

thisSet.add("orange")
print(thisSet)

#To add multiple items to a set, use the update() method
thisSet.update(["blueberries", "grapes"])

print(thisSet)

#Get the length of a Set
print(len(thisSet))

#remove an item in a set
thisSet.remove("banana")
thisSet.discard("apple")

#To remove the last item in the set, use the pop() method
x = thisSet.pop()
print(x)

#empty the entire set use the clear() method

thisSet.clear()
print(thisSet)

#To completely delete the set, use the del() method
thisSet = {"apple", "banana", "cherry"}
del thisSet



#We can use the set() constructor to make a set

thisSet = set(("apple", "banana", "cherry"))	#We require double round brackets
print(thisSet)

"""
Python contains a number of built-in methods that can be used on sets

add() - add an element to a set
clear() - remove all elements
copy() - return a copy of a set
difference() - return a set containing the difference between two or more sets
discard() - remove a specified item
intersection() - return a set, that is the intersection of two other sets
update() - Update a set with the union of this set and others
"""










