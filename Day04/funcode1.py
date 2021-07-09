# Rock Paper Scissors ASCII Art
import random
# Rock

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
userchoice = int(input("Enter your choice: Type 0 for Rock, 1 for paper, 2 for scissors \n"))
if (userchoice >= 3 or userchoice <0):
    print("Invalid entry")
else:
    print(images[userchoice])
    computerchoice = random.randint(0, 2)
    print(images[computerchoice])

    if (userchoice == computerchoice):
        print("Match draw")
    elif (userchoice > computerchoice):
        print("User wins")
    elif (computerchoice > userchoice):
        print("Computer wins")
    elif (computerchoice==2 and userchoice == 0):
        print("User wins")
    elif (computerchoice == 0 and userchoice == 2):
        print("Computer wins")
    else:
        print("Match draw")
