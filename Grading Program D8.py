### Exercise 1 from Day 8 of 100 Days of Code: Utilises Dictionaries (target skill) and Functions. ###

    #Section 1 = My annotated code
    #Section 2 = Original unedited code

        #Section 1
    
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,

# 1 Create an empty dictionary called student_grades.
student_grades = {}

# 2 Create a function that converts the value in student_scores to be used in a for loop.    
def score_converter(stu_score):
    #converts the 'value' from student_scores dictionary, into a string representative of the score range when used in for loop using 'key' as item.
    if int(student_scores[key]) <= 70:
        return("Fail")
    elif int(student_scores[key]) in range(71,80):
        return("Acceptable")
    elif int(student_scores[key]) in range(81,90):
        return("Exceeds Expectations")
    elif int(student_scores[key]) in range(91,100):
        return("Outstanding")
    
# 3 Run a for loop to add the new grades from the converter into the student_grades dictionary.
for key in student_scores:
    student_grades[key] = score_converter(student_scores[key])
    
# 4 Display the new student grades
print(student_grades)
    
                        #COMMENTS
    # 2
        ## First I created a function that will convert a single dictionary value when called upon.
        ## Each if statement calls on the value within the target dictionary (student_scores) using student_scores[key] and checks it against the scoring band.
        ## The int() was used as a precaution to ensure that there is no type error when comparing to the range().
        ## return() was used instead of print() to minimise wasted processes, and allow the result of the function to be used outside of the function.
    # 3
        ## Next I used a for loop to introduce the 'key' dictionary index for the converter function.
        ## score_converter(student_scores[key]) = the result of the function to be entered as the student_grades value.
    
    
#         #SECTION 2
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# def score_converter(stu_score):
#     if int(student_scores[key]) <= 70:
#         return("Fail")
#     elif int(student_scores[key]) in range(71,80):
#         return("Acceptable")
#     elif int(student_scores[key]) in range(81,90):
#         return("Exceeds Expectations")
#     elif int(student_scores[key]) in range(91,100):
#         return("Outstanding")
# for key in student_scores:
#     score_converter(student_scores[key])
#     student_grades[key] = score_converter(student_scores[key])
    

# # 🚨 Don't change the code below 👇
# print(student_grades)
