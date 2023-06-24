def cafe_logo():
    #flatten the ascii art  by Joe Jacques
    machine_ascii = ("    /~~~~~~~~/|\n   / /######/ / |\n  / /______/ /  |\n ============ /||\n |__________|/ ||\n  |\__,,__/    ||"
    + "\n  | __,,__     ||\n  |_\====/%____||\n  | /~~~~\ %  / |\n _|/      \%_/  |\n| |        | | /\n|__\______/__|/")
    #return the variable
    return machine_ascii

def coffee_cup():
    #flatten the ascii art by James Christopher Goodwin
    cup_ascii = "    )))\n    (((\n  +-----+\n  |     |]   ENJOY YOUR DRINK!\n  `-----'\n___________\n`---------'"
    #return the variable
    return cup_ascii

#Create a dictionary for the drinks so that it can be accessed anywhere
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

TENDER = {
    "quarter": 25,
    "dime": 10,
    "nickle": 5,
    "penny": 1    
}

def process_payment(ones, fives, tens, twenty_fives, price):
    """Function checks for correct payment amount.
    Accepts payment, returns change if overpayment occurs, or declines payment if underpayment occurs"""
    #forego the ones as no conversion is needed
    if fives > 0:
        fives *= 5
    if tens > 0:
        tens *= 10
    if twenty_fives > 0:
        twenty_fives *= 25
    #sum of coins into payment and compare to price
    payment = (ones + fives + tens + twenty_fives) / 100
    if payment == price: 
        return "Payment Accepted..."
    elif payment < price:
        return "ERROR: Insufficient Payment"
    else:
        surplus_cash = (payment - price) * 100
        return (int(surplus_cash))

def use_resource(resource_stash, drink_ingredients):
    """Function that selects ingredients for the drink order and updates the resources stocklist
    2 Parameters: dictionary of machine resources, 'ingredients' sub-dict key-pairs for any drink
    """
    for ingredient in drink_ingredients:
        resource_stash[ingredient] -= drink_ingredients[ingredient]     #subtract stock in machine by ingredients being used

    return resource_stash

def refill(resources_list, resource):
    """Function checks replenishes item based on amount"""
    if resource == "water":
        resources_list["water"] += 300
        return resources_list
    elif resource == "milk":
        resources_list["milk"] += 200
        return resources_list
    else:
        resources_list["coffee"] += 100
        return resources_list

def manager_display(orders_history, profits_history, coin_float, machine_inventory):        #Accessed with 'KEY' in order collection input
    status = ""
    while status != "exit":
        status = input("\nManagers Menu:\nORDERS | PROFITS | CASH | INVENTORY | exit\n Type an option OR type 'exit' OR type 'shutdown': ").lower()
        if status == "exit":
            print("\nExiting Manager Mode...")
            break
        elif status == "shutdown":
            if input("Type 'YES' to confirm: ") == "YES":
                return "off"
        elif status == "orders":
            print("\nManager's Menu > ORDERS")
            print(f"\nTotal Orders: {orders_history}")
        elif status == "profits":
            print("\nManager's Menu > PROFITS")
            print(f"\nTotal Profits: ${profits_history}")
        elif status == "cash":
            print("\nManager's Menu > CASH")
            for coin, amount in coin_float.items():
                print(f"\n{coin} Totals: {amount}")
        elif status == "inventory":
            print(f"\nManager's Menu > INVENTORY")
            for resource, amount in machine_inventory.items():
                print(f"\nItem:\n'{resource}': {amount} units")
        else:
            print("\nplease choose a valid option").upper()

def cafe_camille():
    """Function that hosts hot drink orders by taking inputs for drink selection and cash payments."""
    #Create variable to use for while loop to keep the machine running
    machine = "on"
    #import the menu variable as a global variable *NOT TO BE CHANGED*
    global MENU
    global TENDER
    #create the base level of resources for the machine
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    #declare all counters
    total_orders = 0
    total_profits = 0
    total_coins = {
        "quarter": 0,
        "dime": 0,
        "nickle": 0,
        "penny": 0
    }
    while machine != "off":
        #print logo and welcome message
        print(cafe_logo() + "\nThis is CAFE CAMILLE")
        #print the drinks from the menu
        print("The drinks available at this machine are:\n")
        for key in MENU:
            print(key.upper())
        cust_order = input("What drink would you like to order? ").lower()
        if cust_order == "key":         #PATH TO MANAGER'S CONSOLE
            machine = manager_display(total_orders, total_profits, total_coins, resources)      #returns "off" or "none" depending on in-function inputs

        elif cust_order in MENU:      # PATH FOR VALID ITEM SELECTION
            low_supplies = [] ### Essential code for upgrade version ###
            #check if enough ingredients are available

            if cust_order == "espresso":        # MENU-OPTION: ESPRESSO 

                for resource, amount in MENU["espresso"]["ingredients"].items():        # CHECKING INGREDIENT SUPPLIES TO MAKE DRINK
                    if resources[resource] < amount:
                        print(f"The {resource} is too low!".upper())
                        low_supplies.append(resource) ### Essential code for upgrade version ###
                #reloop to the start of function or move forward with drink order 

                if low_supplies:
                    print("Please choose another drink")
                else:
                    #present the item price
                    drink_price = MENU["espresso"]["cost"]
                    print(f"The total price is: ${drink_price} ")
                    #Collect the payment
                    coin_quarters = int(input("Insert Amount of Quarters (25 cent): "))
                    coin_dimes = int(input("Insert Amount of Dimes (10 cent): "))
                    coin_nickles = int(input("Insert Amount of Nickles (5 cent): "))
                    coin_pennies = int(input("Insert Amount of Pennies (1 cent): "))
                    #process the money - ADD INSERTED COINS INTO MACHINE COLLECTION
                    total_coins["quarter"] += coin_quarters
                    total_coins["dime"] += coin_dimes
                    total_coins["nickle"] += coin_nickles
                    total_coins["penny"] += coin_pennies
                    #process the money - ADD INSERTED COINS INTO MACHINE COLLECTION
                    pay_outcome = process_payment(coin_pennies, coin_nickles, coin_dimes, coin_quarters, drink_price)
                    #provide options for failed payments, surplus cash, and exact cash
                    if (pay_outcome) == "ERROR: Insufficient Payment": # PATH FOR UNDER-PAYMENT
                        #remove coins from total coins
                        print(pay_outcome)
                        
                    else:       #PATH EXCLUSIVELY FOR OVER-PAYMENT AND EXACT PAYMENT
                        if pay_outcome == "Payment Accepted...":           # PATH EXCLUSIVELY FOR EXACT CORRECT PAYMENTS
                            print(pay_outcome)      #prints "payment accepted"
        
                        elif type(pay_outcome) != str():        #account for extra change - return change
                            print(f"Your change is £{pay_outcome/100}...")
                            #remove coins from total coin inventory to return change
                            while pay_outcome != 0:     #continue until all due change is returned
                                #check if quarters can be returned as change
                                if pay_outcome // 25 > 0 and total_coins["quarter"] > 0: 
                                    total_coins["quarter"] -= 1     #remove 1 quarter from machine stash
                                    pay_outcome -= 25             #subtract remaining change by the value of current coin taken 

                                elif pay_outcome // 10 > 0 and total_coins["dime"] > 0:
                                    total_coins["dime"] -= 1
                                    pay_outcome -= 10

                                elif pay_outcome // 5 > 0 and total_coins["nickle"] > 0:
                                    total_coins["nickle"] -= 1
                                    pay_outcome -= 5
                                    
                                elif pay_outcome // 1 > 0 and total_coins["penny"] > 0:
                                    total_coins["penny"] -= 1
                                    pay_outcome -= (1)

                            print("\nPlease collect your change.\n")

                        #UPDATE MANAGERS LOG
                        total_profits += (MENU["espresso"]["cost"])
                        total_orders += 1
                        #MAKE THE ESPRESSO - for valid payments only
                        print("Making your drink...\n".upper())
                        resources = (use_resource(resources, MENU["espresso"]["ingredients"]))      #Update machine inventory
                        print(coffee_cup())

            elif cust_order == "latte":        # MENU-OPTION: LATTE 
                for resource, amount in MENU["latte"]["ingredients"].items():        # CHECKING INGREDIENT SUPPLIES TO MAKE DRINK
                    if resources[resource] < amount:
                        print(f"The {resource} is too low!".upper())
                        low_supplies.append(resource)

                #reloop to the start of function or move forward with drink order 
                if low_supplies:
                    print("Please choose another drink")

                else:
                    #present the item price
                    drink_price = MENU["latte"]["cost"]
                    print(f"The total price is: ${drink_price} ")
                    #Collect the payment
                    coin_quarters = int(input("Insert Amount of Quarters (25 cent): "))
                    coin_dimes = int(input("Insert Amount of Dimes (10 cent): "))
                    coin_nickles = int(input("Insert Amount of Nickles (5 cent): "))
                    coin_pennies = int(input("Insert Amount of Pennies (1 cent): "))
                    #process the money - ADD INSERTED COINS INTO MACHINE COLLECTION
                    total_coins["quarter"] += coin_quarters
                    total_coins["dime"] += coin_dimes
                    total_coins["nickle"] += coin_nickles
                    total_coins["penny"] += coin_pennies
                    #process the money - ADD INSERTED COINS INTO MACHINE COLLECTION
                    pay_outcome = process_payment(coin_pennies, coin_nickles, coin_dimes, coin_quarters, drink_price)
                    #provide options for failed payments, surplus cash, and exact cash
                    if (pay_outcome) == "ERROR: Insufficient Payment": # PATH FOR UNDER-PAYMENT
                        #remove coins from total coins
                        print(pay_outcome)
                        
                    else:       #PATH EXCLUSIVELY FOR OVER-PAYMENT AND EXACT PAYMENT      
                        if pay_outcome == "Payment Accepted...":           # PATH EXCLUSIVELY FOR EXACT CORRECT PAYMENTS
                            print(pay_outcome)      #prints "payment accepted"
                        #account for extra change - return change

                        elif type(pay_outcome) != str():
                            print(f"Your change is £{pay_outcome/100}...")
                            #remove coins from total coin inventory to return change
                            while pay_outcome != 0:     #continue until all due change is returned
                                #check if quarters can be returned as change
                                if pay_outcome // 25 > 0 and total_coins["quarter"] > 0: 
                                    total_coins["quarter"] -= 1     #remove 1 quarter from machine stash
                                    pay_outcome -= 25             #subtract remaining change by the value of current coin taken 

                                elif pay_outcome // 10 > 0 and total_coins["dime"] > 0:
                                    total_coins["dime"] -= 1
                                    pay_outcome -= 10

                                elif pay_outcome // 5 > 0 and total_coins["nickle"] > 0:
                                    total_coins["nickle"] -= 1
                                    pay_outcome -= 5

                                elif pay_outcome // 1 > 0 and total_coins["penny"] > 0:
                                    total_coins["penny"] -= 1
                                    pay_outcome -= (1)

                            print("\nPlease collect your change.\n")
                        
                        else:           # PATH EXCLUSIVELY FOR EXACT CORRECT PAYMENTS
                            print(pay_outcome)      #prints "payment accepted"

                        #UPDATE MANAGERS LOG
                        total_profits += (MENU["latte"]["cost"])
                        total_orders += 1
                        #MAKE THE ESPRESSO - for valid payments only
                        print("Making your drink...\n".upper())
                        resources = (use_resource(resources, MENU["latte"]["ingredients"]))      #Update machine inventory
                        print(coffee_cup())
            
            elif cust_order == "cappuccino":        # MENU-OPTION: CAPPUCCINO 
                for resource, amount in MENU["cappuccino"]["ingredients"].items():        # CHECKING INGREDIENT SUPPLIES TO MAKE DRINK
                    if resources[resource] < amount:
                        print(f"The {resource} is too low!".upper())
                        low_supplies.append(resource)

                #reloop to the start of function or move forward with drink order 
                if low_supplies:
                    print("Please choose another drink")

                else:
                    #present the item price
                    drink_price = MENU["cappuccino"]["cost"]
                    print(f"The total price is: ${drink_price} ")
                    #Collect the payment
                    coin_quarters = int(input("Insert Amount of Quarters (25 cent): "))
                    coin_dimes = int(input("Insert Amount of Dimes (10 cent): "))
                    coin_nickles = int(input("Insert Amount of Nickles (5 cent): "))
                    coin_pennies = int(input("Insert Amount of Pennies (1 cent): "))
                    #process the money - ADD INSERTED COINS INTO MACHINE COLLECTION
                    total_coins["quarter"] += coin_quarters
                    total_coins["dime"] += coin_dimes
                    total_coins["nickle"] += coin_nickles
                    total_coins["penny"] += coin_pennies
                    #process the money - ADD INSERTED COINS INTO MACHINE COLLECTION
                    pay_outcome = process_payment(coin_pennies, coin_nickles, coin_dimes, coin_quarters, drink_price)
                    #provide options for failed payments, surplus cash, and exact cash
                    if (pay_outcome) == "ERROR: Insufficient Payment": # PATH FOR UNDER-PAYMENT
                        #remove coins from total coins
                        print(pay_outcome)
                        
                    else:       #PATH EXCLUSIVELY FOR OVER-PAYMENT AND EXACT PAYMENT      
                        if pay_outcome == "Payment Accepted...":           # PATH EXCLUSIVELY FOR EXACT CORRECT PAYMENTS
                            print(pay_outcome)      #prints "payment accepted"
                        #account for extra change - return change

                        elif type(pay_outcome) != str():
                            print(f"Your change is £{pay_outcome/100}...")
                            #remove coins from total coin stash to return change
                            print(total_coins)      # TESTING/TROUBLESHOOTING MEASURE #
                            # 
                            while pay_outcome != 0:     #continue until all due change is returned
                                #check if quarters can be returned as change
                                if pay_outcome // 25 > 0 and total_coins["quarter"] > 0: 
                                    total_coins["quarter"] -= 1     #remove 1 quarter from machine stash
                                    pay_outcome -= 25             #subtract remaining change by the value of current coin taken 
                                elif pay_outcome // 10 > 0 and total_coins["dime"] > 0:
                                    total_coins["dime"] -= 1
                                    pay_outcome -= 10
                                elif pay_outcome // 5 > 0 and total_coins["nickle"] > 0:
                                    total_coins["nickle"] -= 1
                                    pay_outcome -= 5
                                elif pay_outcome // 1 > 0 and total_coins["penny"] > 0:
                                    total_coins["penny"] -= 1
                                    pay_outcome -= (1)

                            print("\nPlease collect your change.\n")
                        
                        else:           # PATH EXCLUSIVELY FOR EXACT CORRECT PAYMENTS
                            print(pay_outcome)      #prints "payment accepted"

                        #UPDATE MANAGERS LOG
                        total_profits += (MENU["cappuccino"]["cost"])
                        total_orders += 1
                        #MAKE THE ESPRESSO - for valid payments only
                        print("Making your drink...\n".upper())
                        resources = (use_resource(resources, MENU["cappuccino"]["ingredients"]))      #Update machine inventory
                        print(coffee_cup())

        else: #account for input error - while loop re-cycles upon incorrect input
            print("   ERROR.\nPlease select from the options provided.")

    ## LOOP BACK TO BEGINNING##

cafe_camille()
