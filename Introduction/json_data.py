"""
JSON in Python

JSON is a syntax for storing and exchanging data.
JSON is text and stands for 'JavaScript Object Notation'

Python has an in-built package called JSON, used to work with JSON data

"""

#importing the JSON package
import json

#Parse JSON (Converting from JSON to Python)

#A piece of JSON Data
x = '{ "name":"John", "age":30, "city":"New York"}'

#parsing the variable 'x' into 'y'
y = json.loads(x)

#the result is a Python Dictionary
print(y["age"])


#Convert from Python to JSON
"""
If you have a Python object, you can convert it to a JSON string by using the
json.dumps() method
"""

#A basic Python dictionary object
x = {"name": "Alan", "age": 26, "country": "Ireland"}

#convert to JSON
y = json.dumps(x)

#The result is a JSON string
print(y)

"""
The following is a list of Python objects that can be converted into JSON strings:
dict, list, tuple, string, int, float, true, false, none


The following is a list of different Python object and their JSON equivalent when 
they get converted:

Python			JSON
dictionary      Object
list			Array
tuple			Array
str             String
int             Number
float           Number
true            true
False           false
None            null
"""

#The following example shows how to convert a Python object containing all legal data types:

z = {
	"name": "Alan",
	"age": 26,
	"married": False,
	"divorced": False,
	"Children": ("None"),
	"pets": None,
	"cars": [
		{"model": "BMW 230", "mpg": 27.5},
		{"model": "Ford Edge", "mpg": 24.1}
	]
}
print(json.dumps(z))



"""
The above example prints the JSON string but it is not very easy to read. json.dumps()
has an indent parameter that makes it easier to read the results
"""

json.dumps(z, indent = 4)


#You can also define separators, default value (",",": ") which means using a comma 
#and a space to separate each object and a colon/space to separate keys from values

print(json.dumps(z, indent=4, separators=(". ", " = ")))

#Finally, you can order the results by the key using a sort_keys parameter

print(json.dumps(x, indent = 4, sort_keys = True))





















