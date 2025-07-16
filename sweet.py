class Sweet:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.id}: {self.name} | ₹{self.price} | Qty: {self.quantity} | Category: {self.category}"