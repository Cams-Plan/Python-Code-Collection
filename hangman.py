import random

#set diagrams and counters for lives, ASCII art.
diagram = [
    "   +---+\n       |\n       |\n       |\n      ===\n",
    "   +---+\n   O   |\n       |\n       |\n      ===\n",
    "   +---+\n   O   |\n   |   |\n       |\n      ===\n",
    "   +---+\n   O   |\n  /|   |\n       |\n      ===\n",
    "   +---+\n   O   |\n  /|\  |\n       |\n      ===\n",
    "   +---+\n   O   |\n  /|\  |\n  /    |\n      ===\n",
    "   +---+\n   O   |\n  /|\  |    [GAME OVER! x_X] \n  / \  |\n      ===\n"
    ]

figure_parts = 0
life_counter = 6
# Create list of words + randomly choose a word from the word_list + create empty list for used words as a control measure. 

import hangman_words
secret_word = random.choice(hangman_words.word_list)
word_length = (len(secret_word))
used_words = []
# Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.

display = []
for lettter in secret_word:
    display += "_"
# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the 
# letters or if all lives are gone.

while "_" in display:
    #display the scoreboard at the beginning of every round + Ask the user to guess a letter and control the type case
    lives = "Remaining Lives:" +  str(life_counter) + " \n"
    print(lives, diagram[figure_parts], display)
    choice = input("Choose a Letter: ").lower()

    # Check if the letter the user guessed is one of the letters in the chosen_word and ONLY ONE letter
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.

    if choice in secret_word and len(choice) == 1:
        if choice not in used_words:
            occur = secret_word.count(choice,0)
            print(f"letter {choice} occurs {occur} time(s)")
            used_words.append(choice)
            for position in range(word_length):
                letter = secret_word[position]
                if letter == choice:
                    display[position] = choice
                    #check if the player has won/completed the word. End game if so.
                    if "_" not in display:
                        print(f"{display}\nYou've Won!")
                        break
        else:
            print(f"correct choice! but you've already chosen '{choice}'. Choose again.".upper())

    # Address incorrect answers. Account for unwanted input and duplicates 
    else:
        if len(choice) == 0:
            print("\nYour choice was blank.\n".upper())
        elif len(choice) > 1:
            print("\nYou can only select ONE word at a time. No cheating!\n".upper())
        elif choice in used_words:
            print(f"Incorrect choice! but luckily you've already chosen '{choice}'. Choose again.".upper())
        else:    
            figure_parts += 1
            life_counter -= 1
            used_words.append(choice)
            # check if the lives have on zero OR if you've reached the final diagram index. If so, end the game.
            if figure_parts == 6:
                print("\nRemaining Lives: 0\n", diagram[figure_parts], display, f"\nSecret Word was '{secret_word}'", "\nYou've Lost :(")
                break
            else:
                print(f"{choice} isn't in the secret word. Guess again")