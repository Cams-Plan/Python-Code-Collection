import random

word_list = ["arctic", "blanket", "blizzard", "zombie", "coat", "calendar", "monkey", "pillow", "pepper"]
figure_parts = 0

#1 - Randomly choose a word from the word_list and assign it to a variable
secret_word = random.choice(word_list)
print(secret_word)

#2: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
for lettter in secret_word:
    display += "_"

#3: - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
choice = input("Choose a Letter: ").lower()

#4: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

if choice in secret_word:
    for letter in secret_word:                
        if letter == choice:
            index_swap = secret_word.index(letter)      # PROBLEM = Searches ONLY for the first index of the identified item/character 
            display[index_swap] = choice                # PROBLEM = the index number will represent the first occurance of the letter so the display will only
                                                        # change the item at that idex, even if it occurs in other places. SOLUTION IN FINAL CODE
                                                        # which identifies the current position of the iteration (using for position in range(len(secret_word)) to use
                                                        # as an index for reference if guess is in substring or not. e.g. display[x] = choice OR display[x] = "_"
        else:
            index_stay = secret_word.index(letter)


    print(display)
else:
    print(display)
    print("guess again")
