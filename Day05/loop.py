## Sample loop program
games = ["cricket", "basketball", "football"]

for play in games:
    print(play)

## Program to list the highest score of the student in the class

scores = [78, 65, 89, 86, 55, 91, 64, 89]

result = 0
for score in scores:
    if score > result:
        result = score

print(f"The highest score in the class: {result}")

## Sample program for range()

for number in range(1, 5):              ## Will consider from 1 to 4 not 5
    print(number)

## Sample program for step range()

for number in range(1, 30, 3):
    print(number)


## Extra tip:

## What is Loop in python?
## Loops are used to loop through an iterable object (like a list, tuple, set, etc.) and perform the same action for each entry.

## What is Range ()?
## Python range() function generates the immutable sequence of numbers starting from the given start integer to the stop integer. It is a built-in function that returns a range object consists of a series of integer numbers, which we can iterate using a for loop.

## The step value to range()?
## The step Specify the increment.

## Fun coding

## Write a Program that calculates the sum of all the even numbers from 1 to 100 (including 1 and 100)
## Solution: For reference purpose only [./Day05/funcode1.py]

## Write a Program that prints fizzbuzz for the number that can be divided by 3 and 5 (including 1 and 100)
## Solution: For reference purpose only [./Day05/funcode2.py]

## Write a Program to generate the password
## Solution: For reference purpose only [./Day05/funcode3.py]