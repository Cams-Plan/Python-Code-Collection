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
game_stats = {"shots taken": ["midrange pull-up", "3-pointer", "lay-up"]}

#Nesting dictionaries in dictionaries
game_stats2 = {"shots made": {
    "midrange pull-up": 3, "3-pointer": 4, "freethrow": 2
}, "shots misssed": {
    "midrange pull-up": 2, "3-pointer": 1, "freethrow": 1, "lay-up": 2
    }
}

print(game_stats2)
