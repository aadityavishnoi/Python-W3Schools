# Python - Remove List Items

thislist = ["apple", "guave", "pomegranate"]
thislist.remove("apple")
print(thislist)

# Remove Specified Index
'''
The pop() method removes the specified index.
'''
thislist = ["apple", "guave", "pomegranate"]
thislist.pop(1)
print(thislist)
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "guave", "pomegranate"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "guave", "pomegranate"]
del thislist[0]
print(thislist)

thislist = ["apple", "guave", "pomegranate"]
del thislist

# clear this list
thislist = ["apple", "guave", "pomegranate"]
thislist.clear()
print(thislist)