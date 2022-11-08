### SHORT CODE ###

# Collect data input 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Convert the input into lowercase as a fail tolerance measure
lowername1 = name1.lower()
lowername2 = name2.lower()
# Count the number of occurances for the letters "l-o-v-e" and "t-r-u-e" within the two names - I chose a for loop to do this.
for letters in lowername1:
    truecountn1 = lowername1.count("t") + lowername1.count("r") + lowername1.count("u") + lowername1.count("e")
    lovecountn1 = lowername1.count("l") + lowername1.count("o") + lowername1.count("v") + lowername1.count("e")
for letters in lowername2:
    truecountn2 = lowername2.count("t") + lowername2.count("r") + lowername2.count("u") + lowername2.count("e")
    lovecountn2 = lowername2.count("l") + lowername2.count("o") + lowername2.count("v") + lowername2.count("e")
# Combine the number of 't-r-u-e" and "l-o-v-e" occurances as a true love number
tc = str(truecountn1 + truecountn2)
lc = str(lovecountn1 + lovecountn2)
lovecalc = tc + lc
# Return the calculations with range-based score statements
if int(lovecalc) < 10 or int(lovecalc) > 90:
    print(f"Your score is {lovecalc}, you go together like coke and mentos.")
elif int(lovecalc) >= 40 and int(lovecalc) <= 50:
    print(f"Your score is {lovecalc}, you are alright together.")
else:
    print(f"your score is {lovecalc}")
    

### LONG CODE ###

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowername1 = name1.lower()
lowername2 = name2.lower()

for letters in lowername1:
    truecountn1 = lowername1.count("t") + lowername1.count("r") + lowername1.count("u") + lowername1.count("e")
    lovecountn1 = lowername1.count("l") + lowername1.count("o") + lowername1.count("v") + lowername1.count("e")

for letters in lowername2:
    truecountn2 = lowername2.count("t") + lowername2.count("r") + lowername2.count("u") + lowername2.count("e")
    lovecountn2 = lowername2.count("l") + lowername2.count("o") + lowername2.count("v") + lowername2.count("e")

tc = str(truecountn1 + truecountn2)
lc = str(lovecountn1 + lovecountn2)
lovecalc = tc + lc

if int(lovecalc) < 10 or int(lovecalc) > 90:
    print(f"Your score is {lovecalc}, you go together like coke and mentos.")
elif int(lovecalc) >= 40 and int(lovecalc) <= 50:
    print(f"Your score is {lovecalc}, you are alright together.")
else:
    print(f"your score is {lovecalc}")
