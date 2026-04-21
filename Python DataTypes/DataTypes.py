# Data Types -- Python

# Built-In-DataTypes
'''
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

'''

# Getting DataTypes
x = 5
print(type(x))

# Complex DataType
x = 1j
print(type(x))

# List DataType
x = ["orange", "apple", "banana"]
print(type(x))

# Tuple DataType
x = ("Orange", "Banana", "Apple")
print(type(x))

# Range DataType
x = range(10)
print(x)
print(list(x))

# Dict DataTypes
x = {"name" : "John", "age" : 36}
print(x)
print(type(x)) 

# Set DataType
x = {"apple", "banana", "cherry"}
print(x)
print(type(x)) 

# FrozenSet
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) 