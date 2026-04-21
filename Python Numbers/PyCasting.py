# Python Casting

'''
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

'''
# Integers
x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)

# Floats
x, y, z, w = float(1), float(2.8), float("3"), float("4.2")
print(x) # x will be 1.0
print(y) # y will be 2.8
print(z) # z will be 3.0
print(w) # w will be 4.2

# Strings
x, y, z = str("s1"), str(2), str(3.0)
print(x) # x will be s1
print(y) # y will be 2
print(z) # z will be 3.0