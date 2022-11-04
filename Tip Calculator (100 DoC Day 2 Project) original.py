### TIP CALCULATOR - FREESTYLE ###
# Tip Calculator as a Function #

def tip_calc(bill,people,tip):
  #Collect Input for calculating the cost per person.
  bill = float(input("Please Enter the cost of the bill. £"))
  people = int(input("How many people are splitting the bill? "))
  tip = int(input("What percentage (%) tip will you give? ")) / 100             #Design Decision: Input for tip amount to allow for freedom and variation
  #Calculate per person tips, bill, and sum.
  tip_per_pers = (bill / people) * tip
  bill_per_pers = bill / people
  full_bill_pers = bill_per_pers + tip_per_pers
  #return the amount
  return(f"Each person will pay £{full_bill_pers:.2f}, which is £{bill_per_pers:.2f}, plus £{tip_per_pers:.2f} tip.")

print(tip_calc())
