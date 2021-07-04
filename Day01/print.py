## To print a line in python
print("I am Prem")
## or
print('I am Prem')

## Python doesnt real care about the quotes between the string.
## But when the statement needs to do something like string inside string type then do like below snippet

print("print('What is your name?')")

## To print the state in the new line use '\n'

print("print('What is your name?') \nMy name is Prem")

## To combine the strings use Concatenation by using '+'

print("print('What is your name?') \nMy name is Prem" + "Kumar")

## While binding the strings you can add space between the strings by leaving the space at the end of the frist string or at the begining of the second string or
## you can add one more concatenation func

print("print('What is your name?') \nMy name is Prem" + " " + "Kumar")

## To ask for user input during execution in python
input("What is your name?")

## To cross check the input func by using a variable
name = input("What is your name?")
print(name)

## To print the line by biding the user input
print("I am" + " " + input("what is your name?"))

## Practice coding
## To print the number of character of the string
print(len(input("What is your name?" )))

## Switch the value
name = input("Prem: ")
greeting = input("Good Morning: ")

say = name
name = greeting
greeting = say

print(name)
print(greeting)

## Extra tip:

## Use a human readable name
## Avoid using func name as variable
## can use my_name but no 'my name' as variable

## Possible error on the string type
## - SyntaxError - Mainly due to missing of the literals
## - IndentationError - Mainly due to unwanted space
## - NameError - Variable name is wrongly referred

## Tools for debugging
## - Thonny - To get a step by step explanation of the function execution

## Extra fun coding

## Create a simple program to print your name and your profession by getting the values separately.

## Solution: For reference purpose only [./Day01/funcode.py]