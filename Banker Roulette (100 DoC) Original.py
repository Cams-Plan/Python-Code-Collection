### SHORT CODE ###

# Import the random module
import random
# Split string method to split the input string into a list
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

      ## |OPTION 1| ## - len & random range method
# Shuffle (optional) - done to increase randomness and mimic shuffling that occurs in real life
random.shuffle(names)
# Call on a random name via the range of indexes collected through the length of the split name list
random_names = random.randrange(len(names))
# Print the result
print(names[random_names].title() +" is going to buy the meal today!")

      ## |OPTION 2| ## - shuffle & append method
# # Shuffle to randomise the name in position 0
# random.shuffle(names)
# # Create an empty list to contain the appended item
# choice = []
# choice.append(names[0])
# # Use a for loop to print the name choice neatly without quotation marks
# for name in choice: 
#     print(name + " is going to buy the meal today!")
