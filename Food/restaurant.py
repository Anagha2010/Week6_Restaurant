# Class definition for class Restaurant
class Restaurant:
    # class constructor
    def __init__(self, name, cuisine_type):
        # class attributes
        self.name = name
        self.cuisine_type = cuisine_type
        self.menu = []  # list
        self.orders = []  # list

    # class methods
    def add_menu_item(self, item):
        self.menu.append(item)
        print(f"{item.name} ({item.serving_size}) Calories: {item.calories} {'(Non Veg)' if not item.is_veg else
        '(V)'} has been added to the menu.---")

    def display_menu(self):
        print(f"\n~~~~~Menu at {self.name} ({self.cuisine_type} Cuisine)~~~~~" if not self.cuisine_type == 'Cafe'
              else f"\n~~~~~Menu at {self.name} (Cafe)~~~~~")
        for item in self.menu:
            print(f"{item.name} - ${item.price}")
        print()

    def place_order(self, customer_name, items):
        order_total = sum(item.price for item in items)
        self.orders.append({"customer": customer_name, "items": items, "total": order_total})
        print(f"Order placed by {customer_name}. Total: ${order_total}.")

    def list_orders(self):
        print("\nOrders received:")
        for order in self.orders:
            print(f"Customer: {order['customer']}, Items: {[item.name for item in order['items']]}, "
                  f"Total: ${order['total']}")
        print()
