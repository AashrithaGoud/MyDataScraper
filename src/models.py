class Product:
    def __init__(self, name, price, discount, old_price):
        self.name = name
        self.price = price
        self.discount = discount
        self.old_price = old_price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Discount: {self.discount}, OldPrice: {self.old_price}"
