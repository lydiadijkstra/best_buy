
class Product:
    """
    Represents a product in the store
    """
    def __init__(self, name, price, quantity):
        """
        Initializing the class parameters
        :param name: product name
        :param price: price
        :param quantity: available quantity
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.deactivate = False


    def __str__(self):
        """
        Assuring to print correct format instead of memory ID
        :return: the formatted printing string
        """
        return f"{self.name} (Quantity: {self.quantity}, Price: ${self.price})"


    def get_quantity(self):
        """
        Retreive the quantity of available products in product list
        :return: quantity
        """
        return f"Product: {self.name}\nQuantity: {self.quantity}"


    def set_quantity(self, quantity):
        """
        for adding new supply to stock
        :param quantity: amount to be added
        """
        self.quantity += quantity
        if self.quantity <= 0:
            self.deactivate = True


    def deactivate(self):
        """
        Deactivates a product when is out of stock
        :return: True
        """
        self.active = False
        self.quantity = 0 # Set quantity to 0 after deactivating
        return True


    def is_active(self):
        """
        Check if product is in stock and set to active
        :return: True
        """
        if self.active == True and self.quantity >= 1:
            return True


    def show(self):
        """
        Display all products incl. price and quantity
        :return: print name, price and quantity
        """
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """
        Check if product in stock, buy product and deduct buying-amount from stock
        :param quantity: buying quantity
        :return: buying quantity and total amount
        """
        if quantity > self.quantity:
            print(f"{self.name} requested: {quantity}. Available: {self.quantity}")
            return None
        else:
            self.quantity -= quantity
            total_purchase_amount = self.price * quantity
            return quantity, total_purchase_amount
