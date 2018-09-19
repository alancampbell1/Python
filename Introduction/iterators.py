"""
Python Iterators

An iterator in python is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse
through all the values.

In Python, an iterator is an object which implements the iterator protocol, which
consists of the methods __iter__() and __next__()

Iterator vs Iterable
Lists, tuples, dictionaries and sets are all iterable objects. They are iterable
containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator
"""

#The following returns an iterator from a tuple and prints each value

myTuple = ("apple", "banana", "cherry")
myiter = iter(myTuple)

print(next(myiter))		#prints the first value
print(next(myiter))		#prints the next value
print(next(myiter))		#and so forth

#Strings are also iterable objects, as they contain a sequence of characters

mystr = "banana"
myit = iter(mystr)

print(next(myit))		#prints b
print(next(myit))		#prints a

print(myit)				#prints '<iterator object at 0x10191a510>'

#Alternatively, you can use a loop to loop through an iterator
myTuple = ("apple", "banana", "cherry")

for x in myTuple:
	print(x)


"""
Creating an Iterator:
To create an object/class as an iterator you have to implement the methods __iter__()
and __next__() to your object.

The __iter__() method allows you to do operations (e.g. initising) but it must always
return the iterator object itself.

The __next__() method allows you to do operations and must return the next item in the
sequence.
"""
print("Creating an iterator that returns numbers, starting with 1 and increasing")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))























