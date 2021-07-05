## Data Types:

## String

print("Hello"[0])

# Even the integer inside "" will be consider as String.
print("123" + "456")

## Integer
print(123 + 456)

## To specify a larger integer use _ (Underscore) between the numbers
print(123_456_789)

## Float
x = 1.234
print(x)

## Boolean
print(1 > 2)
print(2 < 3)

## To check the data type
type(x)
print(type(x))

## To convert the data from one type to another type use type conversion
y = int(x)
print(y)

## PEMDAS {Always calculation goes from Left to Right : PEMDASLR}
print(2 * 2 + 2 / 2 - 2)

## Learn coding
## Sample BMI Calculator

a = input("Enter the height in meter: ")
b = input("Enter the weight in kg: ")

answer = int(b) / float(a) ** 2 # To do the calucation

print(int(answer)) # To print the whole number

## To round off the number after division for example, use round function

print(3 / 4)    # with out rounding

print(round(3 /4))  # with rounding off the number

print(round(3.14768, 2))    # to round off with two decimal values

print(4 // 2)   # to print the whole number during division by using // for integer

## Chain calc func

a = 3 + 4
a -= 4
print (a)

## To auto covert the values on fly use "f-string"

a = 0
b = 1.8
c = True

print(f"Print the value of {a}")

print(f"Print all the values {a}, now {b}, and finally {c}")




## Extra tip:

## Divison will always give float point value as result
## * - Multiplication
## ** - Power of (e.g) 2 ** 3 = 8
## Calculation priorty rule  --> PEMDAS
## PEMDAS
## - Parenthese (), Exponents **, Multiplication *, Division /, Addition +, Subtraction -

## Possible error on the Data type - Integer
## - TypeError - Mainly due to usage of int instead of strings or any other datatypes
## - IndexError - Occurs when we are trying to access a character out of index range

## We can only concatenate str to str not str to int and vice versa
## To cross check the data type use type() function

## Extra fun coding

## Create a simple two digit math program

## Solution: For reference purpose only [./Day02/funcode1.py]

## Create a simpple splitwise calculator

## Solution: For reference purpose only [./Day02/funcode2.py]