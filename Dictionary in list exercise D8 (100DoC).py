### The aim was to write a program that adds to the original (two-item) travel log. The log is a list with nested dictionaries. ###

# THE PRE-MADE TRAVEL LOG DATA - UNCHANGED BY ME
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# 1 Write the function that will allow new countries #to be added to the travel_log.
def add_new_country(thecountry, thevisit, thecities):
    new = {}
    new.update({"country": thecountry, "visits": thevisit, "cities": thecities})
    travel_log.append(new)

# Enter data into the function to be added into the travel log. - PRE-MADE DATA, UNCHANGED BY ME
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


            ## COMMENTS/DECISIONS
            ## 1
            ## I made an empty dictionary called new to transfer the function parameter data
            # into so it would be in format for appending later.
            ## I used .update() to change multiple values of the dictionary at once, to save lines of code.
            ## Once all changes were made, I just needed to append the data from new to into the list
            # which would collect the full dictionary as one list item.
            
            
            
# The Original Code (unchanged from the exercise)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(thecountry, thevisit, thecities):
    new = {"country": "none", 
    "visits": "none", 
    "cities": "none"
    }
    new.update({"country": thecountry, "visits": thevisit, "cities": thecities})
    travel_log.append(new)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
