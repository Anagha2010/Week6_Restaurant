# class definition for class MenuItem
class MenuItem:
    # class constructor
    def __init__(self, name, price, isveg=True, size='Regular', cal='NA'):
        # default_args = ['' if arg is None else arg for arg in args]
        self.name = name
        self.price = price
        self.is_veg = isveg
        self.serving_size = size
        self.calories = cal

    def adjust_drink_price(self):
        if self.serving_size.lower() == 'large':
            self.price += 0.50
        if self.serving_size.lower() == 'small':
            self.price -= 0.50

    # The __str__() method returns a reader-friendly string representation of class object when we print() it
    def __str__(self):
        return f"{'_' * 25}\nItem: {self.name}\nPrice ${self.price}\n{'(V)' if self.is_veg else '(Non Veg)'}\n{'_' * 25}\n"
