### REFERENCE DOCUMENT FOR WORKING WITH DICTIONARIES IN PYTHON ###

variable = {
    "age": "number",
    "height": "centimeters or feet/inches",
    "foot size": "shoe size"
}

#loop through dictrionaries method 1:
#print key then call value by printing key in variable.
for key in variable:
    print(key)
    print(variable[key])

#loop through dictionaries method 2:
#.items() method.
for items in variable.items():
    print(items)

        #Nesting with dictionaries
#Nesting Lists in dictionaries
game_stats = {"shots made": ["midrange pull-up", "3-pointer", "lay-up"]}

#Nesting dictionaries in dictionaries
game_stats2 = {
    "shots taken": {
        "shots made": [{"midrange pull-up": 3}, {"3-pointer": 2}, {"lay-up": 5}],
        "shots missed": [{"free throws": 1}, {"midrange pull-up": 2}, {"lay-up": 2}],
    },
    "assists": 4,
    "turnovers": {
        "live-ball": 1,
        "out of bounds": 1
    },
    "fouls": 3
}

                              
#Retrieving nested dictionary keys and items
# NOTE: Items must be retrieved by going in order of highest key to lowest nested key

# retrieving items from nested dictionaries
print(game_stats2["turnovers"]["live-ball"]) #retrieves the items in "live-ball" nested key

# retrieving list items nested within a dictionary - call the necessary keys first, then call the item index like with a normal list.
print(game_stats["shots made][1])

# retrieving items from dictionaries nested within a dictionary-nested list - if a dictionary nested in a list has multiple key:items, you can call on the key next
print(game_stats2["shots taken"]["shots made"][0]

      
    #Using the Random Module with dictionaries
# random.choice() using: print(random.choice(list(dictionary)))
import random
      print(random.choice(list(variable)))
