"""
Python While Loops
Python has two primitive loop commands: while and for loops
"""

#The while loop can execute a set of statements as long as a condition is true
i = 1
while i < 6:
	print(i)
	i += 1

#NOTE: i++ does not work unlike in Java

#The break statement allows us to stop a loop even while the conditional is true
i = 1
while i < 6:
	print(i)

	if i == 3:
		break
	i += 1

#The continue statement can be used to stop a current iteration and continue onto the next

i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)


"""
A for loop is used for iterating over a sequence (that is either a list, tuple, dictionary,
set, string)
With a for loop we can execute a set of statements
"""

fruits = ["apples", "pears", "bananas"]
for x in fruits:
	print(x)

#In Python, Strings are considered iterable objects as they contain a sequence of characters

for x in "bananas":
	print(x)			#prints each letter in the string

#Incorporating a break statement into a for loop

for x in fruits:
	print(x)
	if x == "pears":
		break

#Incorporating a continue statement in a for loop
for x in fruits:
	if x == "apples":
		continue
	print(x)

print("Range:")
#To loop through a set of code a specified number of times we can use the range() function
#Once x becomes 6 the for loop ends and 6 is not printed
for x in range(6):
	print(x)

print("Range 2:")
#The range starts at 0 but can get a specified starting value
for x in range(2, 6):
	print(x)			#Starts at 2 but ends at 5

print("Range 3:")
#You can also increase the increments by more than 1
for x in range(2, 30, 3):
	print(x)				#Starts at 2, ends before 30, in increments of 3


#The else keyword after a for loop specifies a block of code to be executed after
#the for loop has completed
print("Range 4")
for x in range(6):
	print(x)
else:
	print("Finally finished")


#Python supports nested loops (a loop in a loop). For every one iteration of the outside
#loop, the inner loop is executed to completion

outer = ["red", "orange", "blue"]
inner = [1, 5, 3, 6]

for x in outer:
	for y in inner:
		print(x, y)
