MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.00
    }
}
WATER = 300
MILK = 200
COFFEE = 100
MONEY = 0


def menu(decision):
    global WATER
    WATER -= MENU[decision]["ingredients"]["water"]
    global COFFEE
    COFFEE -= MENU[decision]["ingredients"]["coffee"]
    if decision != "espresso":
        global MILK
        MILK -= MENU[decision]["ingredients"]["milk"]
    global MONEY
    MONEY += MENU[decision]["cost"]
    print(f"Here is your {decision}. Enjoy!")


def coin_operation(quarter, dime, nickle, penny, decision):
    dollar = (quarter*0.25) + (dime*0.10) + (nickle*0.05) + (penny*0.01)
    change = round(dollar - MENU[decision]["cost"], 2)
    return change


def check_resource(decision):
    enough_water = ""
    enough_milk = ""
    enough_coffee = ""
    if MENU[decision]["ingredients"]["water"] <= WATER:
        enough_water += "1"
    else:
        print("Not enough water")
    if decision != "espresso":
        if MENU[decision]["ingredients"]["milk"] <= MILK:
            enough_milk += "1"
        else:
            print("Not enough milk")
    if MENU[decision]["ingredients"]["coffee"] <= COFFEE:
        enough_coffee += "1"
    else:
        print("Not enough coffee")
    if decision != "espresso":
        if enough_water == "1" and enough_milk == "1" and enough_coffee == "1":
            return True
        else:
            return False
    else:
        if enough_water == "1" and enough_coffee == "1":
            return True
        else:
            return False


while True:
    user_decide = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_decide == "espresso" or user_decide == "latte" or user_decide == "cappuccino" or user_decide == "report" or user_decide == "off":
        if user_decide == "off":
            print("The machine turned off")
            break
        if user_decide == "report":
            print(f"water\t{WATER}ml\ncoffee\t{COFFEE}gr\nmilk\t{MILK}ml\nmoney\t${MONEY}")
        else:
            if check_resource(user_decide):
                print("Please insert coins:")
                user_quarter = float(input("How many quarters?: "))
                user_dime = float(input("How many dimes?: "))
                user_nickle = float(input("How many nickles?: "))
                user_penny = float(input("How many pennies?: "))
                user_change = coin_operation(user_quarter, user_dime, user_nickle, user_penny, user_decide)
                if user_change >= 0:
                    if user_change != 0:
                        print(f"Here is your change ${user_change}")
                    menu(user_decide)
                elif user_change < 0:
                    print("Sorry that is not enough money. Money refunded.")
    else:
        print("Sorry! you must choose (espresso/latte/cappuccino)!")

