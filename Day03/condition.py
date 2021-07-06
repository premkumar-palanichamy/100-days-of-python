## To print the letter without space
name = 'Prem'
print ("Hi %s Nice meeting you" % name)

## Try Modulo

print(10 % 3)

## Simple if condition statment

age = 10

if (age < 15):
    print ("you are allowed inside the zoo")        # This will print the output


age = 20
if (age < 15):
    print ("you are allowed inside the zoo")        # This willnot print the output as their to no else condition

## Simple if - else condition statement

age = 20
if (age < 15):
    print ("you are allowed inside the zoo")
else:
    print ("you are not allowed inside the zoo")

## Simple Nested if - else condition statement

age = 10
caretaker = input("Do you have any one with you?(yes or no): ")
if (age < 15):
    print ("you are allowed inside the zoo")
    if (caretaker == 'yes'):
        print ("You are allowed")
    else:
        print ("You are not allowed")
else:
    print ("you are not allowed inside the zoo")

## Simple elif - else condition statement

age = 20
caretaker = input("Do you have any one with you?(yes or no): ")
beenbefore = input("Have you been to zoo before?(yes or no): ")
if (age < 15):
    print ("you are allowed inside the zoo")
elif (caretaker == 'yes'):
        print ("You are allowed")
elif (beenbefore == 'yes'):
        print ("You are allowed")
else:
    print ("you are not allowed inside the zoo")


## Extra tip:

## Can I make a variable like this: 1 = 'Prem'?
## No, the 1 is not a valid variable name. They need to start with a character, for example name1 = 'prem' but not as 1name = 'prem'

## What does %s, %r, and %d do again and what are they?
## They are “formatters.” They tell Python to take the variable on the right and put it in to replace the %s with its value.

## In Nested if, the first if condition needs to be true always
## If the statement wants to continue on to check the other conditions the mutliple if conditions needs to be used, (i.e) else-if --> elif

## Possible error on the Condition statements - If else
## - IndentationError - Mainly due to the code expecting an indented block
## - IndexError - Occurs when we are trying to access a character out of index range

## Modulo Operators:

## Modulo operator is written as a percentage sign (%) but it gives the remainder after a division

## Extra fun coding

## Create a simple od or even program

## Solution: For reference purpose only [./Day03/funcode1.py]

