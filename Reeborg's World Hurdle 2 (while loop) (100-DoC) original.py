### CLICK THE LINK BELOW to go to Reeborg's World and try the code ###
## Link

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
#Start of the journey    
#While loop that operates until the goal is reached
while not at_goal():
    move()
    single_jump_right()
