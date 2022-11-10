### SHORT CODE ### - To be developed with while loop later

# Create the game board using list items as segments
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
# Create nested list of gameboard rows for later indexing via coodinates
map_ = [row1, row2, row3]
# Print the game board - I added numbers on both axis to make it easier for the end user to know which position to choose
print("    0    1    2")
print(f"0{row1}\n1{row2}\n2{row3}")
# collect the row and column coordinates for input
position = input("Where do you want to put the treasure? (row, col) ")
# Split the input into a list. Then create a variable for each list item and convert into an integer
coordinates = position.split(", ")
chrow = int(coordinates[0])
chcol = int(coordinates[1])
# to check for the data type of the conversions use print(type(chcol) + type(chrow))
# change the value of the item in the position specified by user input using the converted row and column variables
map_[chrow][chcol] = "X"
# Display the position of the treasure with the updated gameboard
print("    0    1    2")
print(f"0{row1}\n1{row2}\n2{row3}")


# ### 100 Days of Code Submission ###

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map_ = [row1, row2, row3]
# print("    0    1    2")
# print(f"0{row1}\n1{row2}\n2{row3}")
# position = input("Where do you want to put the treasure? (row, col) ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# coordinates = position.split(", ")
# chrow = int(coordinates[0])
# chcol = int(coordinates[1])
# print(type(chcol))

# map_[chrow][chcol] = "X"


# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print("    0    1    2")
# print(f"0{row1}\n1{row2}\n2{row3}")

