"""
Python Arrays

Arrays are used to store multiple values in a single variable.
They are a special variable that can hold more than one variable at one time.

You can access the values by referring to their index number
"""

cars = ["Ford", "Volvo", "BMW"]

print(cars)
print(cars[2])

#To change an element you refer to its element number
cars[0] = "Toyota"
print(cars)

#To get length of an array we use the len() method
x = len(cars)
print(x)

#You can use a for in loop to loop through all the elements in the array
for x in cars:
	print(x)

#You can add elements to an array using the append() method
cars.append("Honda")
print(cars)

#You can remove a specific element from an array using the pop() method
cars.pop(1)
print(cars)

#An alternative would be to use the remove() function and the actual name of the value
cars.remove("Toyota")
print(cars)

"""
Arrays have a number of methods to carry out different functions
append() - Adds an element to the end of a list
clear() - removes all elements from a list
copy() - returns a copy of the list
count() - returns the number of elements with specified value
extend() - adds elements of a list to the end of a current list
index() - returns the index of the first element with a specified value
insert() - adds an element at a specified position
pop() - removes an element at a specified position
remove() - removes the first item with the specified value
reverse() - reverses the order of a list
sort() - sorts the list
"""