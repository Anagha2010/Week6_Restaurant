# Importing base class
from Food.restaurant import Restaurant

# Class declaration for Cafe class(derived class) that inherits Restaurant class(base class)
class Cafe(Restaurant):
    # class constructor
    def __init__(self, name):
        # calling base class constructor
        super().__init__(name, "Cafe")

    # methods
    def add_coffee(self, item):
        super().add_menu_item(item)
        pass

    def add_pastry(self, item):
        super().add_menu_item(item)
        pass

    def display_menu(self):
        print(f"\nThis and following Menu is printed by overriding base class method:\n~~~~~Menu at {self.name}(Cafe)~~~~~")
        for item in self.menu:
            print(f"{item.name} - ${item.price:.2f}")
        print("**Displayed drink prices are for regular size. +.50 for large and -0.50 for small.\n")
