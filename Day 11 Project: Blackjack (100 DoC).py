import os
from time import sleep
import random


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

def clear_terminal():
    #Clear screen of hands played amount
    sleep(2)
    os.system('cls')

# if sum of hand + 11 > 21:
#     sum of hand + 11 - 10

def ace_decider(person_score, hand):
    if person_score + 11 > 21:
        #find index position of 'Ace' within hand
        ace_position = hand.index({'Ace': [11, 1]})
        person_score += hand[ace_position]['Ace'][1]
        #Use the list position of 'Ace' to change the item to reflect the newly accepted value
        hand[ace_position]['Ace'] = 1
        return hand
    else:
        ace_position = hand.index({'Ace': [11, 1]})
        person_score += hand[ace_position]['Ace'][0]
        hand[ace_position]['Ace'] = 11
        return hand


def score_calc(hand):
    sum = 0
    for number in hand:
        sum += number
    return sum


def collect_card(hand, deck):
    """"Allows the player to add a card to their hand by appending a random item from deck list
    \nRequires 2 Parameters"""
    hand.append(random.choice(deck))
    return hand


def blackjack_game():
    card_collection = [{'Ace':[11, 1]}, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #declare player and computer score variables
    player_score = 0
    computer_score = 0
    #create and draw the initial 2 cards for the player and computer's hand
    player_hand = random.choices(card_collection, k=2)
    computer_hand = random.choices(card_collection, k=2)
    #calculate the player and computer's score based on cards in hand
    player_score = score_calc(player_score)
    computer_score = score_calc(computer_score)

    if 'Ace' in player_hand:
        ace_decider(person_score, hand)

    print(blackjack_ascii)
    print(f"Your Cards: {player_hand}")
