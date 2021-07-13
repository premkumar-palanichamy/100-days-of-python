import random

word = ["apple", "orange", "grapes", "pineapple"]

chosen_word = random.choice(word)

print(chosen_word)

user_choice = input("Type a letter: ").lower()

for letter in chosen_word:
    if letter == user_choice:
        print("Right")
    else:
        print("Wrong")
