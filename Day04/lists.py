## Sample module implementation using Random module

import random

random_seed = random.randint(1, 10)
print(random_seed)

## Simple head or tail program

import random

value = random.randint(0, 1)
result = "head" if value == 1 else "tail"  # Ternary operator declaration

print(result)

## Lists

import random

names = input("Enter the names: ")
final_names = names.split(', ')

ranval = random.randint(0, 2)
print(final_names[ranval])

## Pick a random name from the list

import random

names = input("Enter the names: ")
final_names = names.split(", ")

ranval = len(final_names)

result = random.randint(0, ranval - 1)

personname = final_names[result]
print(personname)

## Sample program example for Nested list

game = ["cricket", "footbal", "basketball"]
profession = ["Engineer", "Singer", "Pilot"]

showme = [game, profession]
print(showme)

## Extra tip:

## What is module in python?
## Modules refer to a file containing Pyth on statements and definitions. A file containing Python code, for example: example.py, is called a module, and its module name would be example
## Refer ./Day04/module.py and ./Day04/refer.py for more understanding

## Ternary Operators:
## Ternary operators are more commonly known as conditional expressions in Python. These operators evaluate something based on a condition being true or not.

## str.split(',')
## splits the string based on some sort of divider

## len() - It can be used to get the number of characters in the list or number of words in the list

## What is List?
## A list is a data structure in Python and used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

## What is Nested List?
## A list can contain any sort object, even another list (sublist), which in turn can contain sublists themselves, and so on. This is known as nested list.


## Possible error on the Lists
## -  TypeErrostatement - Mainly due to the wrong declaration of data type
## - IndexError - Occurs when list index is out of range

## Fun coding

## Create a rock, paper, scissors game
## Solution: For reference purpose only [./Day04/funcode1.py]