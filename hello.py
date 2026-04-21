text = "  Hello, Python World!  "

print("Original:", repr(text))
print("Strip():", repr(text.strip()))
print("Upper():", text.upper())
print("Lower():", text.lower())
print("Replace():", text.replace("Python", "Java"))

words = text.split(",")
print("Split():", words)

