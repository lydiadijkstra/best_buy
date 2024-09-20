class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.deactivate = False


    def get_quantity(self):
        return f"Product: {self.name}\nQuantity: {self.quantity}"


    def set_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        if self.quantity == 0:
            self.deactivate = True
        #print(f"{self.name} quantity: {self.quantity}")


    def is_active(self):
        if self.quantity >= 1:
            return self.active
        else:
            return False


    def show(self):
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        total_purchase_amount = self.price * quantity
        self.quantity = self.quantity - quantity
        print(f"{self.name} * ${self.price}")
        print(f"Total amount: ${total_purchase_amount}")
        return self.quantity, total_purchase_amount
