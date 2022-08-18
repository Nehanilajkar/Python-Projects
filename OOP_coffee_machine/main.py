from menu import Menu
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj=Menu()
coffee_obj=CoffeeMaker()
money_obj=MoneyMachine()

while True:
    options=menu_obj.get_items()
    choice=input(f"What would you like? ({options}):").lower()
    if choice=="report":
        coffee_obj.report()
        money_obj.report()
        continue
    elif choice=="off":
        break
    else:
        drink=menu_obj.find_drink(choice)
        if coffee_obj.is_resource_sufficient(drink) and money_obj.make_payment(drink.cost):
            coffee_obj.make_coffee(drink)
