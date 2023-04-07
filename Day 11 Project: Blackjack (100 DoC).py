import os
from time import sleep
import random

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
    else:
        ace_position = hand.index({'Ace': [11, 1]})
        person_score += hand[ace_position]['Ace'][0]
        hand[ace_position]['Ace'] = 11


def score_calc(hand):
    for number in hand:
        print()


card_collection = [{'Ace':[11, 1]}, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []
