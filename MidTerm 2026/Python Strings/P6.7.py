# Program to count vowels in a string

s = input("Enter String: ")
count = 0
for ch in s.lower():
    if ch in 'aeiou':
        count += 1
    
print("Number Of Vowels: ", count)