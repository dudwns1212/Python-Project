from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffe_maker = CoffeeMaker()

while True:
    options = menu.get_items()
    coffee = input(f"What would you like? {options}: ")
    if coffee == 'off':
        break
    elif coffee == 'report':
        coffe_maker.report()
        money_machine.report()
        continue
    else:
        drink = menu.find_drink(coffee)
        print(drink.cost)
        is_sufficient = coffe_maker.is_resource_sufficient(drink)

        if is_sufficient:
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
            else:
                continue
        else:
            continue
