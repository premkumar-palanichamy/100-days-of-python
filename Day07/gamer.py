## Gamer letter guessing word app

import random
import replit
#from replit import clear

word = ["apple", "orange", "grapes", "pineapple"]

chosen_word = random.choice(word)
print(chosen_word)

end_of_game = False
lives = 6

print (f'Solution result {chosen_word}.')

display = []
for _ in range(len(chosen_word)):
    display += "_"
print (display)

while not end_of_game:
    user_choice = input("Type a letter: ").lower()
    replit.clear()

    if user_choice in display:
        print(f"You've already guessed {user_choice}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_choice:
            display[position] = letter



    if user_choice not in chosen_word:

        print(f"You guessed {user_choice}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

   # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

    from art import stages

    print(stages[lives])


## Extra tip:

## What is _ and __ in python?
## - For storing the value of last expression in interpreter.
## - For ignoring the specific values. (so-called “I don’t care”)
## - To give special meanings and functions to name of variables or functions.
## - To use as ‘Internationalization(i18n)’ or ‘Localization(l10n)’ functions.
## - To separate the digits of number literal value.