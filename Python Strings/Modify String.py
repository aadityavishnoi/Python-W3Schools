# Python - Modify String

# UpperCase
'''
The upper() method returns the string in upper case:
'''
a = "Hello, World!"
print(a.upper())

# LowerCase
'''
The Lower() method returns the string in lower case:
'''
a = " HELLO, AADITYA "
print(a.lower())

# Strip
'''
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
'''
a = " HELLO, AADITYA "
print(a.strip()) # Removes The WhiteSpaces

# Replace String
'''
The replace() method replaces a string with another string.
'''
a = "Hello, Abhishek"
print(a.replace("H", "j"))

# Split String
'''
Split String
The split() method returns a list where the text between the specified separator becomes the list items.
'''
a = "Hello, World, Aadi!"
print(a.split(","))