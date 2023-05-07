import random

# Include an ASCII art logo.
heading_ascii_2 = """
     __                 _                   ___                _     _      
  /\ \ \_   _ _ __ ___ | |__   ___ _ __    / _ \___ _   _  ___| |__ (_) ___ 
 /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|  / /_)/ __| | | |/ __| '_ \| |/ __|
/ /\  /| |_| | | | | | | |_) |  __/ |    / ___/\__ \ |_| | (__| | | | | (__ 
\_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    \/    |___/\__, |\___|_| |_|_|\___|
                                                    |___/
WELCOME TO NUMBER PSYCHIC!                   
"""

# Create list of numbers from 1 to 100 and secret number from the list
numbers_list = list(range(1,101))
SECRET_NUMBER = random.choice(numbers_list)

def easy_mode():
    global SECRET_NUMBER
    attempts_easy = 10
    while attempts_easy != 0:
        print(f"You have {attempts_easy} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
     
        if guess == SECRET_NUMBER:
            print(" _________________________________________________________________" +
            "\n|                   Great Job! You Are Correct!                   |" +
            f"\n    -The SECRET NUMBER was {SECRET_NUMBER}")
            print(f"    -You guessed the correct number with {attempts_easy} attempt(s) remaining")
            play_again = input("\n Would you like to play again? y/n? ")
          
            if play_again == "y":
                print("let's play")
            else:
                break

        elif guess > 100:
            print("That's not a number between 1-100\nGuess again.")

        elif guess > SECRET_NUMBER:
            print("That's too high.\nGuess again.")
            attempts_easy -= 1
            print(attempts_easy)

        else:
            print("That's too low.\nGuess again.")
            attempts_easy -= 1
          
    if attempts_easy == 0:
        print(" _______________________________\n|    You ran out of attempts.   |\n            You lose.")
        print(f"    -The SECRET NUMBER was {SECRET_NUMBER}.")
        play_again = input("\nWould you like to play again? y/n? ")
          
        if play_again == "y":
            number_psychic_game()
        else:
            print("Thank you for playing.")

def hard_mode():
    global SECRET_NUMBER
    attempts_hard = 5
    while attempts_hard != 0:
        print(f"You have {attempts_hard} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == SECRET_NUMBER:
            print(" _________________________________________________________________" +
            "\n|                   Great Job! You Are Correct!                   |" +
            f"\n    -The SECRET NUMBER was {SECRET_NUMBER}")
            print(f"    -You guessed the correct number with {attempts_hard} attempt(s) remaining")
            play_again = input("\nWould you like to play again? y/n? ")
          
            if play_again == "y":
                number_psychic_game()
            else:
                break

        elif guess > 100:
            print("That's not a number between 1-100\nGuess again.")

        elif guess > SECRET_NUMBER:
            print("That's too high.\nGuess again.")
            attempts_hard -= 1
            print(attempts_hard)

        else:
            print("That's too low.\nGuess again.")
            attempts_hard -= 1
    if attempts_hard == 0:
        print(" _______________________________\n|    You ran out of attempts.   |\n            You lose.")
        print(f"    -The SECRET NUMBER was {SECRET_NUMBER}.")
        play_again = input("\nWould you like to play again? y/n? ")
          
        if play_again == "y":
            print("let's play")
        else:
            print("Thank you for playing.")

def number_psychic_game():
    print(heading_ascii_2, "\nI'm thinking of a number for 1-100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        easy_mode()
    elif difficulty == 'hard':
        hard_mode()
    else:
        print("Please choose 'easy' or 'hard'. ")
        number_psychic_game()

number_psychic_game()
