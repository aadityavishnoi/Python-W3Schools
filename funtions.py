def greet():
    print("Hello World!")
greet()

'''
import math

def calculate_circle_area(radius):
  if radius <= 0:
    return "Please enter a positive number." 
  else:
    area = math.pi * (radius ** 2)
    return area
user_radius = float(input("Enter the radius of the circle: "))
area_result = calculate_circle_area(user_radius)
print(f"The area of the circle with radius {user_radius} is: {area_result}")

import math

def prime_number(number):

    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
try:
    user_input = int(input("Enter a number to check for primality: "))
    if prime_number(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter an integer.")
'''
a = 8
b = 4
c = 3
def greatest(a, b, c):
    if a > b or a > c:
        return (a)
    elif b > c or b > a:
        return(b)
    elif c > a or c > b:
        return (c)
print(greatest(a, b, c))

# Sum Of Digits Of A Number Using A Function
'''
def sum_of_digits_str(n):
  num_str = str(abs(n)) 

  digit_sum = sum(map(int, num_str))
  return digit_sum
number = 12345
print(f"The sum of digits of {number} is {sum_of_digits_str(number)}")

def is_palindrome(data):
    
    return str(data) == str(data)[::-1]

word = "racecar"
number = 121

print(f"'{word}' is a palindrome: {is_palindrome(word)}")
print(f"'{number}' is a palindrome: {is_palindrome(number)}")
print(f"'hello' is a palindrome: {is_palindrome('hello')}")
'''

