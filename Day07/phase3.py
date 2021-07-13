import random

word = ["apple", "orange", "grapes", "pineapple"]

chosen_word = random.choice(word)
print(chosen_word)

display = []
for _ in range(len(chosen_word)):
    display += "_"
print (display)

end_of_game = False
while not end_of_game:
    user_choice = input("Type a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_choice:
            display[position] = letter

    print (display)
    if "_" not in display:
        end_of_game = True
        print("You Win !!!")