## Treasure Box

print('''
__________________
/\  ______________ \
    /::\ \ZZZZZZZZZZZZ /\ \
    /: / \.\ \ /: / \:\ \
    /: / Z /\:\ \ /: / Z /\:\ \
    /: / Z / __\:\ \____ /: / Z /  \:\ \
    /: / Z / ____\:\ \___\ / Z /    \:\ \
    \:\ \ZZZZZ\:\ \ZZ /\ \     \:\ \
    \:\ \     \:\ \ \:\ \     \:\ \
    \:\ \     \:\ \_\;\_\_____\;\ \
    \:\ \     \:\_________________ \
    \:\ \ /: / ZZZZZZZZZZZZZZZZZ /
\:\ \ /: / Z /    \:\ \ /: / Z /
\:\ \ /: / Z /      \:\ \ /: / Z /
\:\ /: / Z / ________\;\ /: / Z /
\:: / Z / _______itz__\ / Z /
\ / ZZZZZZZZZZZZZZZZZ /
      ''')

print("Welcome to Treasure Box")
print("Find the Treasure")
choice1 = input('You\'re at a crossroad, where do you want to go:? Type "left" or "right"').lower()

if choice1 == "left":
    choice2 = input('You\'ve come. Entry the room to find.Type "wait" to wait').lower()
    if choice2 == "wait":
        choice3 = input("choose you color? select red or yellow or blue").lower()
        if (choice3 == 'red'):
            print("Game over")
        elif choice3 == 'yellow':
            print("You own")
        elif choice3 == 'blue':
           print("Game Over")
        else:
             print("Game Over")
    else:
       print("You failed")
else:
     print("You failed")

