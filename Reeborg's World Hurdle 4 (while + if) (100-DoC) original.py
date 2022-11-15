### COPY AND PASTE THE LINK BELOW to be try out the code for Reeborg's World Hurdle 4 level ###
## LINK: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    #Function that turns right within tile
    turn_left()
    turn_left()
    turn_left()

def jump_right():
    #Function that used 4 tiles to jump over 1 tile hurdle
    #Ascension
    counter = 0    #Counter to count extra tile ascensions
    turn_left()
    move()
    while not right_is_clear():     # To account for higher walls, allow sprite to ascend until the hurdle has been cleared
        move()
        counter += 1    #Counter increases after every extra tile
    turn_right()
    move()
    #landing
    turn_right()
    move()
    while counter != 0:    # To account for higher walls, allow sprite to descend until landing is distance = ascension distance via counter
        move()
        counter -= 1
    turn_left()
#Start Journey
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump_right()
