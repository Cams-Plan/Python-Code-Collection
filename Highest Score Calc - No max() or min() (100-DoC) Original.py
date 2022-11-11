### SHORT CODE ###
## INSTRUCTIONS: You are going to write a program that calculates the highest score from a List of scores.
##               Howver, you are not allowed to use the max() or min() functions.

#Collect input data for student scores and create into a list
student_scores = input("Input a list of student scores ").split()
# Convert the list of strings into a list of integers and display finalised int list
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# Calculate and return the highest score without using Sort()/sorted() or max()
base_score = 0
for score in student_scores:
    if score > base_score:
        base_score = score
print(f"The highest score in the class is: {base_score}")

