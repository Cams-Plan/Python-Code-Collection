import os
from time import sleep
import random

def score_calc(score, hand):
    #set score to zero to neutralise any previous score_calc (key for re-scoring after ace change)
    score = 0
    #add every card value from the hand and store it within the score variable
    for number in hand:
        score += number
    return score

def ace_decider(hand,position,score):
    if score + 11 > 21: 
        hand[position] = 1
        return hand
    else:
        hand[position] = 11
        return hand

blackjack_ascii = """
       Camille's Blackjack Game (Cams-Plan @GitHub)
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |
      `------'                           |__/ 
"""

def collect_card(hand, deck):
    """"Allows the player to add a card to their hand by appending a random item from deck list
    \nRequires 2 Parameters"""
    hand.append(random.choice(deck))
    return hand

def clear_terminal():
    #Clear screen of hands played amount
    sleep(2)
    os.system('cls')

def computer_hit_stand(hand, deck, score):
    #utilise hit or stand tactics to determine how the computer plays
    if score >= 17:
        #no cards drawn if score is more than or equal to 17
        return hand, score

    elif score in range(12,17):
        #check if there's already an 11 because there can only be 1
        if 11 in hand:
            while score in range(12, 17):
                #while score is 12 to 16 computer should draw a card   
                hand = collect_card(hand, deck)
                #check if newest card is an ace (= 11)
                if hand[-1] == 11:
                    #process the ace to be changed to 1 or remain an 11
                    #done without function as score outcome from an 11 value ace can be predicted
                    hand[-1] = 1
                    score = score_calc(score, hand)
                else:
                    score = score_calc(score, hand)
        else:
            #separate code condition for non-elevens in deck
            #allows for potential of 11 card ace be drawn and ace_decider function
            while score in range(3, 14):
                hand = collect_card(hand, deck)
                if hand[-1] == 11:
                    #decide ace value with ace-decider function because scores of 3-10 can use an 11-value ace
                    hand = ace_decider(hand, -1, score)
                    score = score_calc(score, hand)
                else:
                    score = score_calc(score, hand)

        return(hand, score)
    else:
        #for any score that is <12
        if 11 in hand:
            while score in range(3, 14):
                #while score is 3 to 14 computer should draw a card   
                hand = collect_card(hand, deck)
                #check if newest card is an ace (= 11)
                if hand[-1] == 11:
                    #process the ace to be changed to 1 as there's already an 11 value ace
                    hand[-1] = 1
                    print(f"new hand {hand}")
                    score = score_calc(score, hand)
                else:
                    print(f"new hand {hand}")
                    score = score_calc(score, hand)

            return hand, score
        else:
            while score in range(3, 14):
                hand = collect_card(hand, deck)
                newest_card = hand[-1]
                if newest_card == 11:
                    #decide ace value with ace-decider function because scores of 3-10 can use an 11-value ace
                    hand = ace_decider(hand, -1, score)
                    score = score_calc(score, hand)
                    print(f"new hand {hand}")
                else:
                    print(f"new hand {hand}")
                    score = score_calc(score, hand)

            return hand, score

def blackjack_game():
    clear_terminal()
    card_collection = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #declare player and computer score variables to be used for function parameters
    player_score = 0
    computer_score = 0
    #create and draw the initial 2 cards for the player and computer's hand
    player_hand = random.choices(card_collection, k=2)
    computer_hand = random.choices(card_collection, k=2)
    player_score = score_calc(player_score, player_hand)
    # check for an ace in player's hand
    if 11 in player_hand: 
        #collect index of 'Ace' for later reference
        ace_position = player_hand.index(11)
        #use function to decide whether the ace value is 11 or 1
        player_hand = ace_decider(player_hand, ace_position, player_score)
        #recalculate player's score after
        player_score = score_calc(player_score, player_hand)

    if 11 in computer_hand: 
        #collect index of 'Ace' for later reference
        ace_position = computer_hand.index(11)
        #use function to decide whether the ace value is 11 or 1
        computer_hand = ace_decider(computer_hand, ace_position, computer_score)
        #recalculate computer's score after
        computer_score = score_calc(computer_score, computer_hand)

    print(blackjack_ascii)
    print(f"    Your cards: {player_hand}, Current score: {player_score}\n      Computer's first card: {computer_hand[0]}")

    #Create option for player to hit (get another card), or stand (pass on pick up)
    hit_or_stand = input("Type 'y' to get another card, or type 'n' to pass: ")
    #program the computer's card drawing

    if hit_or_stand == 'y':
        while hit_or_stand == 'y':
            print("Drawing a card...")
            player_hand = collect_card(player_hand, card_collection)
            player_score = score_calc(player_score, player_hand)
            #clear terminal for final score 
            clear_terminal()
            print(blackjack_ascii)
            print(f"    Your cards: {player_hand}, Current score: {player_score}\n      Computer's first card: {computer_hand[0]}")
            hit_or_stand = (input("Type 'y' to get another card, or type 'n' to pass: "))

        print("Locking in hand...")
        clear_terminal()
    else:
        print("Locking in hand...")
        clear_terminal()
    #call function to perform computer's decisions to hit (pick up) or stand (pass)
    computer_stats = computer_hit_stand(computer_hand, card_collection, computer_score)
    #check if player went bust
    if player_score > 21:
        print(blackjack_ascii)
        print(f"    Your final hand: {player_hand}, your final score: {player_score}")
        print(f"    Computer's final hand: {computer_hand}, computer's final score: {computer_score}")
        print("Player went over. Computer wins! :(")
        play = input("Would you like to play a round of Blackjack?\nType 'y' to play or 'n' to exit: ")
        if play == "y":
                blackjack_game()
        elif play != "y":
            print(" Goodbye,\nWe hope to see you soom")

    elif computer_stats[1] > 21:
        print(blackjack_ascii)
        print(f"    Your final hand: {player_hand}, your final score: {player_score}")
        print(f"    Computer's final hand: {computer_hand}, computer's final score: {computer_score}")
        print("Computer went over. Player wins! :)")
        play = input("Would you like to play a round of Blackjack?\nType 'y' to play or 'n' to exit: ")
        if play == "y":
                blackjack_game()
        elif play != "y":
            print(" Goodbye,\nWe hope to see you soom")
    elif player_score > computer_stats[1]:
        print(blackjack_ascii)
        print(f"    Your final hand: {player_hand}, your final score: {player_score}")
        print(f"    Computer's final hand: {computer_hand}, computer's final score: {computer_score}")
        print("Player has the higher score. Player wins! :)")
        play = input("Would you like to play a round of Blackjack?\nType 'y' to play or 'n' to exit: ")
        if play == "y":
                blackjack_game()
        elif play != "y":
            print(" Goodbye,\nWe hope to see you soom")
    elif computer_stats[1] > player_score:
        print(blackjack_ascii)
        print(f"    Your final hand: {player_hand}, your final score: {player_score}")
        print(f"    Computer's final hand: {computer_hand}, computer's final score: {computer_score}")
        print("Computer has the higher score. Computer wins! :(")
        play = input("Would you like to play a round of Blackjack?\nType 'y' to play or 'n' to exit: ")
        if play == "y":
                blackjack_game()
        elif play != "y":
            print(" Goodbye,\nWe hope to see you soom")
    else:
        print(blackjack_ascii)
        print(f"    Your final hand: {player_hand}, your final score: {player_score}")
        print(f"    Computer's final hand: {computer_hand}, computer's final score: {computer_score}")
        print("It's a TIE! :)")
        play = input("Would you like to play a round of Blackjack?\nType 'y' to play or 'n' to exit: ")
        if play == "y":
                blackjack_game()
        elif play != "y":
            print(" Goodbye,\nWe hope to see you soom")
            
#### Beginning of blackjack script ####
play = input("Would you like to play a round of Blackjack?\nType 'y' to play or 'n' to exit: ")
if play == "y":
        blackjack_game()
elif play == "n":
    print(" Goodbye,\nWe hope to see you soom")
else:
    confirm = input("did you mean to type 'n'? type 'yes' or 'no' to confirm: ")
    if confirm == 'no':
        blackjack_game()
    else:
        print(" Goodbye,\n  We hope to see you soom")
