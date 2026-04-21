# Python Booleans

'''
In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
'''

print(10 < 9)
print(10 > 9)
print(10 == 10)
print(10 == 9)

# Evaluate Values And Variables
'''
The bool() function allows you to evaluate any value, and give you True or False in return,
'''
print(bool("Hello"))
print(bool(15))

x = 5
y  = "Hello"

print(bool(x))
print(bool(y))

# False Values
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

# Functions Can Return a Boolean

def myfunction():
    return True

print(myfunction())

def myfunction():
    return True

if myfunction():
    print("Yes")
else: 
    print("No")


# Check If An Object Is Integer Or Not
x = 200
print(isinstance(x, int))