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

auction_item = random.choice(list(auction_list))
auction_status = "yes"

print(f"The item up for bidding is a '{auction_item}'")
item_and_price = {auction_item: int(auction_list[auction_item])}
print(f"The starting bid is at £{item_and_price[auction_item]}")

while auction_status == "yes":
    question = input("Would you like to make a bid? yes or no: ").lower()
    auction_status = question
    if auction_status == "no":
        break
    bidder = input("What is your firstname? ").lower()
    bid = int(input("What is your bid? "))
    if bid < item_and_price[auction_item]:
        print(f"bids must be at least {item_and_price[auction_item]} so we've rounded it up to the minimum")
    else:
        auctioners_list[bidder] = bid
        item_and_price[auction_item] = bid
    print("Your bid is locked!")
    sleep(.5)
    #Clear screen of bidding amount
    print("clearing screen...")
    sleep(2)
    os.system('cls')
    #display all progressive bidders
    print(f"The list of bids for current item:")
    for person in auctioners_list:
        print(f"Bidder: {auctioners_list[person]}")
    sleep(2)
    print(f"The current bid is at £{item_and_price[auction_item]}")

print("This auction is over, Thank you for your time")
