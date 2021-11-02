# For Loop

### Additonal For looping
> As we know `for loop` is a programming language statement (i.e) an iteration statement, which allows a code block to be repeated a certain number of times.

There are different kinds of loop:
- Count-controlled for loop
- Numeric Ranges
- Vectorized for loops
- Iterator-based for loop (The one used by Python).

Syntax:

The iteration based loop in Python steps through the items of lists, tuples, strings and dict and other iterables.

The general Syntax looks like: `for in : else:`

####Python For Loop Syntax
- Tuple: 
Let us understand the for loop syntax with an example based on tuples:
```
x = (1,2,3,4,5)
for i in x:
     print(i)
```

- Range: 
Range is a Built-in function that returns a sequence.A range function has three parameters which are starting parameter, ending parameter and a step parameter. Ending parameter does not include the number declared, let us understand this with an example.
```
a = list(range(0,10,2))
print(a)
```

##### Break:
Break in python is a control flow statement that is used to exit the execution as soon as the break is encountered. 

```commandline
company = ['E','D','U','R','E','K','A']
 
for x in company:
    if x == "R":
        break
    print(x)
```

##### Continue:
Continue statement is also a control statement but it will only skip the current iteration and execute the rest of the iterations anyway.

```commandline
company = ['E', 'D', 'U', 'R', 'E', 'K', 'A']
 
for x in company:
    if x == "R":
        continue
    print(x)
Output: E

        D

        U

        E

        K

        A
```

res = 1
 
for i in range(0,5):
    n = int(input("enter a  number"))
    res *= n
    print(res)

### Extratip

##### Loop in plain way:

Normal way:

```commandline
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

Output:
milk
sugar
vanilla extract
dough
chocolate
```

Write 10 print() statements below! 
```
x = "This can be so much easier with loops!"
for i in range(10):
  print (x)
```

#### ZIP ()

Zip () is used to loop through two arrays at once.

(e.g.)

```commandline
for first,second in zip(array1,array2):
    print(first)
    print(second)
```

```commandline
odds = [1,3,5,7,9]
even = [2,4,6,8,10]
for oddnum, evennum in zip(odds, even):
    print(oddnum)
    print(evennum)
    
Output:
1
2
3
4
5
6
7
8
9
10
> 
```

#### Sorted ()

Sorting works both with String and integer (-,+..)

```commandline
l = [14,19,26,14,5,6]
for i in sorted(l):
    print(i)

Output:

5
6
14
14
19
26
> 

To reverse the sort:
for i in sorted(l,reverse = True):
    print(i)
    
Output:

26
19
14
14
6
5
> 
```