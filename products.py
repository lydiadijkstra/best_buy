from store import Store

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.deactivate = False


    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity}, Price: ${self.price})"


    def get_quantity(self):
        return f"Product: {self.name}\nQuantity: {self.quantity}"


    def set_quantity(self, quantity):
        self.quantity += quantity
        if self.quantity <= 0:
            self.deactivate = True
        #print(f"{self.name} quantity: {self.quantity}")


    def deactivate(self):
        self.active == False
        self.quantity = 0 # Set Product quantity to 0 for adding quantity not starting in negative numbers


    def is_active(self):
        if self.active == True and self.quantity >= 1:
            return True


    def show(self):
        print(f"//show-method// {self.name}, Price: ${self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        if quantity > self.quantity:
            print(f"Not enough {self.name} in stock. Requested: {quantity}. Available: {self.quantity}")
            return 0

        self.quantity - quantity
        total_purchase_amount = self.price * quantity
        return quantity, total_purchase_amount

