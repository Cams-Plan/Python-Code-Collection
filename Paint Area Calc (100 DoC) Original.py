### Create a function that calculates the required amount of paint, based on parameters given (area to be painted)

def paint_calc(height, width, cover):
    #calculates number cans needed to finish paint job
    area = height * width
    can_calc = area / cover
    can_calc = round(can_calc)
    if can_calc == 1:
        print(f"You'll need {can_calc} can of paint")
    else:
        print(f"You'll need {can_calc} cans of paint")
  

# 🚨 Don't change the code below 👇         ## PRE-MADE CODE BELOW
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
