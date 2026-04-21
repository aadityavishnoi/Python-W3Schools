# Python - Access List Items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])

# Negative Indexing
print(thislist[::-1])
print(thislist[-1])

# Range Of Indexes
print(thislist[1:3:4])
print(thislist[:2])
print(thislist[3:])

name = "Aaditya"
character1 = name[2]
print(character1)

s = "Pyhton Programming"
print("SubString:", s[0 : 6])
print("Reverse Slice:", s[::-1])
print(s[4 : 12])

def is_palindrome(s):
  s = s.casefold() 
  return s == s[::-1]

print(is_palindrome("madam"))   
print(is_palindrome("hello"))  
print(is_palindrome("Racecar")) 

a = "harry"
count = 0
for ch in s:
  count = count + 1
  print(count)

#Reverse Of A String

s = "hello"
reversed_s = s[::-1]
print(reversed_s)

def count_vowels_sum(text):
 
  vowels = "aeiouAEIOU"

  count = sum(1 for char in text if char.lower() in vowels)
  return count


input_string = input("Enter The Name")
vowel_count = count_vowels_sum(input_string)
print(f"Number of vowels in '{input_string}': {vowel_count}")


