"""
Python Operators

Operators are used to perform operations on variables and values.
They are divided up into the following groups:
"""

#Arithmetic Operators (Perform common mathematical operations)
x = 10
y = 5

print(x + y)		#addition
print(x - y)		#subtraction
print(x * y)		#multiplication
print(x / y)		#division
print(x % y)		#modulus
print(x ** y)		#exponentiation
print(x // y)		#floor division



#Assignment Operators (Used to assign values to variables)
"""
=			x = 5			x = 5
+=			x += 5			x = x + 5
-=			x -= 5			x = x - 5
*=			x *= 5			x = x * 5
/=			x /= 5			x = x / 5
%=			x %= 5			x = x % 5
//=			x //= 5			x = x // 5
**=			x **= 5			x = x ** 5
&=			x &= 5			x = x & 5
|=			x |= 5			x = x | 5
^=			x ^= 5			x = x ^ 5
>>=			x >>= 5			x = x >> 5
<<=			x <<= 5			x = x << 5
"""


#Comparison Operators (returns a boolean)
a = 5
b = 6
print(a == b)		#equal
print(a != b)		#not equal
print(a > b)		#greater than
print(a < b)		#less than
print(a <= b)		#less than or equal to
print(a >= b)		#greater than or equal to


#Logical Operators (used to combine conditional statements)
a = 8
b = 10

print(a < 5 and b > 12)			#returns true if both statements are true
print(a < 5 or b > 12)			#returns true if one statement is true
print(not(a < 5 and b > 12))	#reverses the result, returns false if result is true


#Identity Operators (Used to compare objects, not if they are equal but 
#if they are the same object with the same memory location)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)	#returns true because they are the same object with same memory location

print(x is y)	#returns false because they are two separate objects despite having same contents

print(x == y)	#returns true because contents of x is the same as y


#Membership Operators (Used to test if a sequence is presented in an Object)
x = ["apple", "banana"]
print("banana" in x)		#returns True because "banana" is present in the object x

z = ["apple", "banana"]
print("pineapple" not in z)	#returns True because "pineapple is not in object z"
