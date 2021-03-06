# Models
class Product:
    def __init__(self, size, color, brand, price):
        self.size = size
        self.color = color 
        self.brand = brand 
        self.price = price


class Shape(Product):
    def __init__(self, size, color, brand, price):
        super(Product, self).__init__(size, color, brand, price)


class Truck(Product):
    def __init__(self, size, color, brand, price):
        super(Product, self).__init__(size, color, brand, price)


class Wheel(Product):
    def __init__(self, size, color, brand, price):
        super(Product, self).__init__(size, color, brand, price)


class Stock:
    def __init__(self):
        self.shapes = [
            Shape(8, 'blue', 'celobrands', 50),
            Shape(8.25, 'blue', 'celobrands', 50),
            Shape(8, 'green', 'celobrands', 50),
            Shape(8, 'yellow', 'celobrands', 50),
            Shape('30mm', 'white', 'celobrands', 50)
        ]
        self.trucks = [
            Truck('139mm', 'black', 'celoco', 60),
            Truck('139mm', 'pink', 'celoco', 60),
            Truck('149mm', 'green', 'celoco', 60)
        ]
        self.wheels = [
            Wheel('53mm', 'white', 'celobrands',30),
            Wheel('54mm', 'white', 'celobrands',30),
            Wheel('55mm', 'white', 'celobrands',30)
        ]

    # TODO: Create function to check whether an item exists in stock or not

    # TODO: Create function to etrieve the item from Stock


stock = Stock()