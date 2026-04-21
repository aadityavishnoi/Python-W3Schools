# Python - Change List Items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "guava"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["watermelon", "pomegranate"]
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)