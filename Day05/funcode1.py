## Even sum program

start_number = 0

for number in range(2, 101, 2):
#    print(number)                   ## For testing
    start_number += number
print(start_number)