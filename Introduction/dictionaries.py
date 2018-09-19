"""
Python Dictionaries
A dictionary is a collection which is unordered, changable and indexed. In Python,
dictionaries are written with curly brackets and have keys/values
Remember:
keys are on the left
values are on the right
Together they are known as items
"""

thisDict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

print(thisDict)

#You can access items of a dictionary by referring to its key name

x = thisDict['model']
print(x)

#Alternatively, you can get access to a dictionairy item by a get() method
x = thisDict.get("model")
print(x)

#You can change the value of a specific value by referring to its key name
thisDict["year"] = 2018
print(thisDict['year'])

#The following for loop loops through the dictionary and returns each key
for x in thisDict:
	print(x)

#The following for loop returns the values of the dictionary
for x in thisDict:
	print(thisDict[x])

#This for loop returns both the keys and values
for x, y in thisDict.items():
	print(x, y)

#Getting the length of a dictionary
print(len(thisDict))


#To add an item to the dictionary
thisDict["colour"] = "red"
print(thisDict)

#To remove an item we can use the del keyword
del thisDict["model"]
print(thisDict)

#clear() removes all items from a dictionary
thisDict.clear()

#You can use the dict() constructor to create a dictionary from scratch
thisDict = dict(brand = "Ford", model = "Mustang", year = "1965")
print(thisDict)

"""
Other methods that can be used on Dictionaries include:

copy() - removes all items
fromkeys() - returns a dictionary with specific keys and values
get() - returns the value of a specific key
items() - returns a list containing the a tuple from each key value pair
values() - returns a list of all values in a dictionary
"""









