# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
#
# print(table)


# A coffee machine by using OOP (object-oriented programming)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_items = MenuItem
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    order_name = input(f"What would you like? ({menu.get_items()}): ")

    if order_name == "off":
        is_on = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
