### Silent auction script that utilises with preset list of auction items selected at random per script run.
### Auction rounds take one bid at a time, with bidders stored in auctioners list.

import random
import os
from time import sleep

auctioners_list = {}

auction_list = {
    "silver necklace".title(): 45,
    "rustic table".title(): 68,
    "pokemon card collection".title(): 132,
    "steph curry jersey".title(): 290 
}
#create variables for auction items and auction status for loop
auction_item = random.choice(list(auction_list))
auction_status = "yes"
item_and_price = {auction_item: int(auction_list[auction_item])}

def bid_collecion():
    #collect the bidder's name to store in auctioners list dictionary
    #collect the bid amount and update item's price as the auction progresses 
    bidder = input("What is your firstname? ").lower()
    bid = int(input("What is your bid? "))

    if bid < item_and_price[auction_item]:
        print(f"bids must be at least £{item_and_price[auction_item]}, so we've rounded it up to the minimum")
        round_up_check = input("Would you still like to continue with your bid? yes or no: ".upper())

        if round_up_check == "yes":
            auctioners_list[bidder] = item_and_price[auction_item]        
            sleep(2)
    else:
        auctioners_list[bidder] = bid
        item_and_price[auction_item] = bid

def clear_terminal():
    sleep(1)
    print("Your selection has been confirmed")
    sleep(1)
    #Clear screen of bidding amount
    print("clearing screen...")
    sleep(2)
    os.system('cls')

# OPENING STATEMENT
print(f"The item up for bidding is a '{auction_item}'")
print(f"The starting bid is at £{item_and_price[auction_item]}")

# AUCTION LOOP
while auction_status == "yes":
    question = input("Would you like to make a bid? yes or no: ").lower()
    auction_status = question

    if auction_status == "no":
        break

    #collect bidders name and bid amount
    bid_collecion()
    #clear screen of personal bid details
    clear_terminal()
    
    #display all progressive bidders
    print(f"The list of bids for current item:")
    for person in auctioners_list:
        print(f"Bidder: {auctioners_list[person]}")

    sleep(2)
    print(f"The current bid is at £{item_and_price[auction_item]}")

# end if auction statement
print("This auction is over,\nThank you for your time!".upper())

