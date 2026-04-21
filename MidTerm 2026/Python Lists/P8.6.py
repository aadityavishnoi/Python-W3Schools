# Program to remove duplicate elements from a list
lst = [10, 20, 30, 20 ,10 , 40]
unique = list(set(lst))
unique.sort()
print(unique)