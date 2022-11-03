# ### LONG CODE ###
# # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# years_til_ninty = 90 - int(age)
# months_til_ninty = 12 * years_til_ninty
# weeks_til_ninty = 52 * years_til_ninty
# days_til_ninty = 365 * years_til_ninty

# print(f"You have {days_til_ninty} days, {weeks_til_ninty} weeks, and {months_til_ninty} months left.")



### SHORT CODE/ MY VERSION ###
# Collect Input Data + Type Convert
age = int(input("What is your current age? "))
# Conversion Calculations into months, weeks, & days
years_til_ninty = 90 - age
months_til_ninty = 12 * years_til_ninty
weeks_til_ninty = 52 * years_til_ninty
days_til_ninty = 365 * years_til_ninty

print(f"You have {days_til_ninty} days, {weeks_til_ninty} weeks, and {months_til_ninty} months left.")
