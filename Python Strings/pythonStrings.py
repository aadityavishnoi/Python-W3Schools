# Python Strings

'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".
You can display a string literal with the print() function

'''

print("Hello")
print('Hello')

'''
Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string

'''

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign String To A Variable

a = "hello"
print(a)

# MultiLine Strings

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings Are Arrays
'''
Like many other popular programming languages, strings in Python are arrays of unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Get the character at position 1 (remember that the first character has the position 0)
'''
a = "Hello World!"
print(a[4])

# Looping Through A String
for x in "banana":
    print(x)

# String Length
a = "Hello"
print(len(a)) # Returns Length Of A String

# Check String
txt = "The best things in life are free!"
'''
To check if a certain phrase or character is present in a string, we can use the keyword in.
'''
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is Present")

# If Not Statement
if "aaditya" not in txt:
    print("Not Present")