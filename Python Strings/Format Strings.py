# Python Format Strings

# F-String
'''
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

'''
age = 36
txt = f"I Am {age} years Old"
print(txt)

# Placeholders And Modifiers
price = 249
txt = f"The Price Is {price} rupees"
print(txt) # Output Will Be The Price Is 249 rupees

'''
Include Placeholders
'''
price = 59
txt = f"The Price Is {price:.2f} rupees"
print(txt) # Output Will Be> The Price Is 59.00 rupees

'''Other Codes'''
txt = f"The Price Is {25 * 145}"
print(txt) 