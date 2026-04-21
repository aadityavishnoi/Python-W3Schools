#Program to check palindrome string

s = input("Enter String ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")