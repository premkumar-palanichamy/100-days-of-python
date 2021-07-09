## Password Generator App

import random
import string

letters = (list(string.ascii_lowercase))
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Password Generator")

no_letter = int(input("Enter the number of letters you need: \n"))
no_number = int(input("Enter the number of numbers you need: \n"))
no_symbols = int(input("Enter the number of symbols you need: \n"))

password_list = []

for char in range(1, no_letter + 1):
    password_list.append(random.choice(letters))
for char in range(1, no_number + 1):
    password_list += random.choice(numbers)
for char in range(1, no_symbols + 1):
    password_list += random.choice(symbols)

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your Password is: {password}")
