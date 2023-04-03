calc_ascii = """
 _____________________\n|  _________________  |
| | Camille's Calc  | |\n| |_________________| |\n|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |\n| |___|___|___| |___| |\n| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |\n| | 1 | 2 | 3 | | x | |\n| |___|___|___| |___| |
| | . | 0 | = | | / | |\n| |___|___|___| |___| |\n|_____________________|
"""
print(calc_ascii)

def add(n1, n2):
    """Adds two numbers together"""
    if type(n1) is str and type(n2) is str:
        return("Error.\nNumbers only")
    else:
        return(n1 + n2)

def subtract(n1, n2):
    """Subtracts two numbers together"""
    if type(n1) is str and type(n2) is str:
        return("Error.\nNumbers only")
    else:
        return(n1 - n2)

def multiply(n1, n2):
    """Multiplies two numbers together"""
    if type(n1) is str and type(n2) is str:
        return("Error.\nNumbers only")
    else:
        return(n1 * n2)

def divide(n1, n2):
    """Divides two numbers together"""
    if type(n1) is str and type(n2) is str:
        return("Error.\nNumbers only")
    else:
        return(n1 / n2)

def convert_int_float(number):
    """Converts one string into a float or int based on the presence of a '.' substring.

    This functions requires 1 parameter.
    
    Ideal use: input variable to fulfil the parameter."""
    if '.' in number:
        number = float(number)
        return(number)
    else:
        number = int(number)
        return(number)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

calculation = ""
while not calculation == "end":
    num1 = convert_int_float((input("Enter the first number: ")))
    num2 = convert_int_float((input("Enter the second number: ")))

    operator = input("Select your operator: ")

    for symbol in operations:
        if symbol == operator:
            print(operations[symbol](num1, num2))
    calculation = "end"
