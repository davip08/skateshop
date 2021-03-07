# Models
class Product:
    def __init__(self, size, color, brand, price):
        self.size = size
        self.color = color 
        self.brand = brand 
        self.price = price


class Shape(Product):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Truck(Product):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Wheel(Product):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Stock:
    def __init__(self):
        self.shapes = [
            Shape(size=8, color='blue', brand='celobrands', price=50),
            Shape(size=8.25, color='blue', brand='celobrands', price=50),
            Shape(size=8, color='green', brand='celobrands', price=50),
            Shape(size=8, color='yellow', brand='celobrands', price=50),
            Shape(size='30mm', color='white', brand='celobrands', price=50)
        ]
        self.trucks = [
            Truck(size='139mm', color='black', brand='celoco', price=60),
            Truck(size='139mm', color='pink', brand='celoco', price=60),
            Truck(size='149mm', color='green', brand='celoco', price=60)
        ]
        self.wheels = [
            Wheel(size='53mm', color='white', brand='celobrands', price=30),
            Wheel(size='54mm', color='white', brand='celobrands', price=30),
            Wheel(size='55mm', color='white', brand='celobrands', price=30)
        ]

    # TODO: Create function to check whether an item exists in stock or not

    # TODO: Create function to etrieve the item from Stock


stock = Stock()