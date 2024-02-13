from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turn_off = False

while not turn_off:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        turn_off = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        choice_name = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(choice_name):
            if money_machine.make_payment(choice_name.cost):
                coffee_maker.make_coffee(choice_name)



