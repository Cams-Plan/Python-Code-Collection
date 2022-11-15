### COPY AND PASTE THE LINK BELOW to go to the Reeborg's World Hurdle 3 level and try the code ###
## Link:

def turn_right():
    #Function that turns right within tile
    turn_left()
    turn_left()
    turn_left()
    
def single_jump_right():
    #Function that used 4 tiles to jump over 1 tile hurdle
    #Ascension
    turn_left()
    move()
    turn_right()
    move()
    #landing
    turn_right()
    move()
    turn_left()
    
#start of journey
#create loop that stops at the goal
while not at_goal():
#account for walls/hurdles directly blocking front movememt
    if front_is_clear():
        move()
    else:
        single_jump_right()
