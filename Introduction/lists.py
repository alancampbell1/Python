"""
Python Lists:

There are 4 collection types in the Python Programming Language:
- List: A collection which is ordered and changeable. It allows duplicate members
- Tuple: A collection which is ordered and unchangeable. It allows for duplicate members
- Set: A collection which is unordered and unindexed. No duplicate members allowed
- Dictionary: A collection which is unordered, changeable and indexed. No duplicate members

Choosing the right type comes down to retention of meaning, and increased efficiency and
security.
"""

"""
List:
A List is a collection which is ordered and changeable. In Python, lists are written 
with square brackets.
"""

thisList = ["apple", "banana", "cherry"]
print(thisList)

#You can access items by referring to its index number
print(thisList[1])		#prints banana

#You can change a specific item be referring to its index number
thisList[0] = "orange"
print(thisList)

#You can loop through a list by using a for loop:
for x in thisList:
	print(x)

#You can determine how many items a list has by using the len() method
print(len(thisList))

#To add an item to a list you use the append() method
thisList.append("blueberries")
print(thisList)

#To insert an item into a specified index, you use the insert() method
thisList.insert(1, "pear")
print(thisList)				#everything else gets pushed along


#There are several methods that can be deployed to remove an item from a list

thisList.remove("pear")		#removes a specified item by its contents

thisList.pop()				#removes at a specified index or last index if not specified

del thisList[0]				#removes at a specified index

print(thisList)

thisList.clear()			#clears all elements from the list


"""
append() - add element to the end of the list
clear() - remove element from the list
copy() - returns a copy of the list
count() - returns the number of elements with a specified value
extend() - add the elements of a list to the end of the current list
index() - returns the index of the 1st element with a specified value
insert() - adds an element at a specified position
pop() - removes an element at a specified position
remove() - removes the item with a specified value
reverse() - reverses the order of the list
sort() - sorts a list

"""











