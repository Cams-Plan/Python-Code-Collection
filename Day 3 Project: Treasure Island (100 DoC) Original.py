### 100 Days of Code Day 3 Project: Treasure Island ###

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Set starting statement
print("\nYou've just arrived, and you see a quad bike and an old Land Rover.\nWhich one will you choose?")
choice1 = input("'BIKE' or 'ROVER'? ").upper()
# Statement for invalid inputs as a variable - Quality Control
invalid = "\nThat option is invalid!\nTry again another time."
#Create the path for the answer route: leading with the correct answers for the initial if statements.
if choice1 == "BIKE":
    print("\nYour skin's burning afer riding for so long.\nDo you rest under a coconut tree, or look to make a shelter?")
    choice2 = input("'TREE' or 'SHELTER'? ").upper()
    if choice2 == "SHELTER":
        print("\nAll that work has made you hungry. Do you hunt and forage, or eat a small snack bar? ")
        choice3 = input("'HUNT' or 'SNACK'? ").upper()
        if choice3 == "SNACK":
            print("You see a crate suspended by a rope. Do you cut it, or slowly lower it?")
            choice4 = input("'CUT' or 'LOWER'? ").upper()
            if choice4 == "LOWER":
                print("You avoided triggering the TNT in the treasure box!\nYou have won the hunt!")
# Elif for the wrong answers, and Else to account for invalid choice selection.
            elif choice4 == "CUT":
                "The impact triggered the TNT in the box!\nGame Over"
            else:
                print(invalid)

        elif choice3 == "HUNT":
            print("You got stung by a puffer fish!\nGame Over")
        else:
            print(invalid)

    elif choice2 == "TREE":
        print("\nA coconut fell on your head while you slept!\nGAME OVER")
    else:
        print(invalid)

elif choice1 == "ROVER":
    print("The old vehicle blew up!\nGAME OVER")
else:
    print(invalid)
    
### BY CAM'S PLAN ###
