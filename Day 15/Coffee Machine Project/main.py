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
## 현재 자원을 output 해주는 함수
def resource_report():
    return print(f"Water: {resources["water"]}, Milk: {resources["milk"]}, "
            f"Coffee: {resources["coffee"]}, Money:{resources["money"]}")
## 고른 음료에 대해서 현재 남은 자원이 충분한지 판단해주는 함수
def resource_enough(drink):
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    if drink != 'espresso':
        milk = MENU[drink]["ingredients"]["milk"]

    if resources['water'] < water:
        return f"Sorry there is not enough water"
    elif coffee > resources['coffee']:
        return f"Sorry there is not enough coffee"
    elif drink != 'espresso':
        if milk > resources['milk']:
            return f"Sorry there is not enough milk"

    return 'enough'

def cost_enough(q, d, n, p, drink):
    global cost
    global customer_money
    customer_money = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    cost = MENU[drink]['cost']
    if cost > customer_money:
        return False
    else:
        return True

def add_resource(income, drink):
    resources["money"] += income
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    if drink != 'espresso':
        milk = MENU[drink]["ingredients"]["milk"]

    resources["water"] -= water
    resources["coffee"] -= coffee
    if drink != "espresso":
        resources["milk"] -= milk


customer_money = 0
cost = 0
while True:
    if "money" not in resources:
        resources["money"] = 0

    selected_drink = input("무엇을 드시겠습니까? (espresso/latte/cappuccino): ")
    if selected_drink == 'off':
        break
    elif selected_drink == 'report':
        resource_report()
        continue

    enough = resource_enough(selected_drink)
    if enough != 'enough':
        print(enough)
        break

    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))

    enough_cost = cost_enough(quarters, dimes, nickles, pennies, selected_drink)
    if enough_cost:
        print(f"Here is ${customer_money - cost} in change.\n"
              f"Here is your {selected_drink} ☕️. Enjoy!")
        add_resource(cost, selected_drink)
    else:
        print("Sorry that's not enough money. Money refunded.")
