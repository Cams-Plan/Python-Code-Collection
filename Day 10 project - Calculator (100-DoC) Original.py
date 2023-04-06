### Basic calculator made by following 100 days of code course as well as my own exploration.
#  NOTES:
## My Deviations from the guide:
##      - Added type checks within the operator functions to ensure the parameters passed through are handled without errors
##      - Created a function that detects whether an input string should be converted to a float or int for presentation purposes.

calc_ascii = """
 _____________________\n|  _________________  |
| | Camille's Calc  | |\n| |_________________| |\n|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |\n| |___|___|___| |___| |\n| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |\n| | 1 | 2 | 3 | | x | |\n| |___|___|___| |___| |
| | . | 0 | = | | / | |\n| |___|___|___| |___| |\n|_____________________|
"""
# create functions for +, -, *, and / operations
def add(n1, n2):
    """Add two numbers together and checks for absence of string data type.
    \n2 Parameters Required - Integers or Floats."""
    if type(n1) is str and type(n2) is str:
        return("Error.\nNumbers only")
    else:
        return(n1 + n2)

def subtract(n1, n2):
    """Subtracts two numbers together and checks for absence of string data type.
    \n2 Parameters Required - Integers or Floats."""
    if type(n1) is str and type(n2) is str:
        return("Error.\nNumbers only")
    else:
        return(n1 - n2)

def multiply(n1, n2):
    """Multiplies two numbers together and checks for absence of string data type. 
    \n2 Parameters Required - Integers or Floats."""
    if type(n1) is str and type(n2) is str:
        return("Error.\nNumbers only")
    else:
        return(n1 * n2)

def divide(n1, n2):
    """Divides two numbers together and checks for absence of string data type.
    \n2 Parameters Required - Integers or Floats."""
    if type(n1) is str and type(n2) is str:
        return("Error.\nNumbers only")
    else:
        return(n1 / n2)
# Create a function that converts a string to an int or float based on the presence of a '.' within the target string.
def convert_int_float(number):
    """Converts one string into a float or int based on the presence of a '.' substring.
    \nRequires 1 parameter.
    \nIdeal use: input variable to fulfil the parameter."""
    if '.' in number:
        number = float(number)
        return(number)
    else:
        number = int(number)
        return(number)
#Create a dictionary with a operator string as the key and corresponding function as the item
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
#Create the calculation function to allow for recurrsion
def calculator():
    """Calculates a sum of numbers using '+' '-' '*' '/' operators.
    \nNo Parameters Required."""
    print(calc_ascii)

    num_1 = convert_int_float((input("Enter the first number: ")))
    #cycle through operations dict keys to print operator options
    for symbol in operations:
        print(symbol)
    should_cont = True

    while should_cont:
        operator = input("Select your operator: ")
        
        #while loop activates if/for as long as the inputed operator string is not one of the options available
        while operator not in operations:
            operator = input("Select a valid operator: ")
        num_next = convert_int_float((input("Enter the second number: ")))
        #calculate by calling on a specific operator via index of 'operations' dictionary item
        calc_function = operations[operator]
        answer = (calc_function(num_1, num_next))
        
        #display the sum contents to user
        print(f"{num_1} {operator} {num_next} = {answer}")
        
        #allow users to continue sum, start a new sum, or exit the calculator
        end_q = input(f"Type 'y' To continue calculating with '{answer}', type 'c' to start a new calculation, OR type 'x' to exit: ").lower()
        
        if end_q == 'y':
            num_1 = answer
            calc_function = operations[operator]
            answer = (calc_function(num_1, num_next))
        elif end_q == 'c':
            should_cont = False
            calculator()
        else:
            should_cont = False

calculator()
