### SHORT CODE ###
## CALCULATE THE AVG USER INPUT HEIGHT WITHOUT USING len() OR sum() ##

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# print(student_heights)    # Used to check. can be left commented out
counter = 0
sumheight = 0
## Add the list items together and generate the total of items in the list WITHOUT sum() and len()
for height in student_heights:
    sumheight += height
#    print(sumheight)       # Used to check. can be left commented out
    counter += 1
#calculate and return the average
avg_height = sumheight / counter
print(int(round(avg_height,0)))

### Line 4-7 are pre-generated code. Line 8 and beyond are my code
