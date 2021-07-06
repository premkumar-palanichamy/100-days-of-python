## Code for finding the leap year

year = int(input("Year you want to check?: "))

if (year % 4 == 0):
    if (year % 100 ==0):
        if (year % 400 ==0):
            print ("This is Leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is Leap year")
else:
    print("This is not a leap year")