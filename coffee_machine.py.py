from logo import logo

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
print(logo)

money =0

def calculate_money(cost_of_order,q,d,n,p):
    in_dollars = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
    if in_dollars >= cost_of_order:
        change = in_dollars - cost_of_order
        global money
        money += 1
        print(f"Here is ${change: .2f} in change.")
        print("Here is your cappuccino ☕️. Enjoy!")
        resouces_ingridients(user_choice)
    else:
        print("Sorry that's not enough money. Money refunded.")


def check_resources(order):

    for i in MENU[order]["ingredients"]:
       if resources[i] < MENU[order]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
       else:
            return True

def resouces_ingridients(order):
    for i in MENU[order]["ingredients"]:
        resources[i] -= MENU[order]["ingredients"][i]


game_over = False
while not game_over:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        game_over = True
    elif user_choice == "report":
        print(f"water : {resources["water"]}")
        print(f"milk : {resources["milk"]}")
        print(f"coffee : {resources["coffee"]}")
        print(f"money : ${money}")
    else:
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        cost = MENU[user_choice]["cost"]
        if check_resources(user_choice):
            calculate_money(cost, quarters, dimes, nickles, pennies)





