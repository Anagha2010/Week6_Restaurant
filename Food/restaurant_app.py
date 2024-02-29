# importing the classes
from Food.restaurant import Restaurant
from Food.menuItem import MenuItem
from Food.cafe import Cafe

# Instantiating class MenuItem
burger = MenuItem("Bean burger", 8.99, True, 'Regular', '450')
pasta = MenuItem("Spaghetti", 12.99, False, cal=400)
salad = MenuItem("Caesar Salad", 6.99, True)
bread = MenuItem("Cheesy garlic bread", 5.99, True)

coffee1 = MenuItem("Latte", 2.99, size="Small", cal=150)
print("\n*Regular price:", coffee1.price)
coffee1.adjust_drink_price()
# calls __str__() method to present instance as formatted string
print(coffee1.serving_size)
print(coffee1)


coffee2 = MenuItem("Cappuccino", 2.49, size="Regular")

coffee3 = MenuItem("Mocha", 3.49, size="Large")
print("\n*Regular price:", coffee3.price)
coffee1.adjust_drink_price()
print(coffee3)

pastry1 = MenuItem("Croissant", 2.49, True)
pastry2 = MenuItem("Blueberry Muffin", 2.99, True, cal=200)

print(burger)
print(pasta)
print(pastry1)

# Instantiating class Restaurant
restaurant = Restaurant("Burgers and more", "American")

# Calling add_menu_item method on instance of Restaurant class
restaurant.add_menu_item(burger)
restaurant.add_menu_item(pasta)
restaurant.add_menu_item(salad)
restaurant.add_menu_item(bread)

# Calling display_menu method on instance of Restaurant class
restaurant.display_menu()

# Calling more methods on instance of Restaurant class
restaurant.place_order("Peter", [burger, salad])
restaurant.place_order("Edmund", [pasta, bread])
restaurant.list_orders()

# Instantiating class Cafe
cafe = Cafe("Central Park")

# Calling methods on instance of Restaurant class
cafe.add_menu_item(coffee1)
cafe.add_menu_item(coffee2)
cafe.add_menu_item(coffee3)
# cafe.add_menu_item(pastry1)
cafe.add_pastry(pastry2)
cafe.add_menu_item(pastry1)

cafe.display_menu()

# calling base class method on cafe object for placing orders at the cafe
cafe.place_order("Lucy", [cafe.menu[0], cafe.menu[3]])
cafe.place_order("Susan", [cafe.menu[2], cafe.menu[4]])

# Listing orders at the cafe
cafe.list_orders()
