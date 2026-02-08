from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while True:
    choice = input(f"What would you like to order? ({menu.get_items()}): ")
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if not order:
            print("Couldn't find that drink. Try again!")
            continue

        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)