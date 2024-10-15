
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


    def deactivate_product(self):
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


    def buy(self, amount):
        """
        Check if product in stock, buy product and deduct buying-amount from stock
        :param quantity: buying quantity
        :return: buying quantity and total amount
        """
        if amount > self.quantity:
            print(f"Purchase not possible, {self.name} requested: {amount}. Available: {self.quantity}")
            return None
        else:
            self.quantity -= amount #deducts the buying quantity
            total_purchase_amount = self.price * amount
            return amount, total_purchase_amount


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=None)


    def show(self):
        """
        Display details of a non-stocked product (e.g., digital product).
        """
        super().show()
        print(f"{self.name} is a non-stocked product (digital or service).")


class LimitedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=1)


    def buy(self, amount=1):
        """
        Override the buy function for limited products like shipping.
        Limited products can only be purchased once (quantity is always 1).
        :return: tuple of (purchased amount, total purchase amount)
        """
        if amount > 1:
            print(f"You can only purchase 1 {self.name}.")
            return None
        else:
            return 1, self.price


    def show(self):
        """
        Display details of a limited product.
        """
        super().show()
        print(f"{self.name} is a limited product, available only in limited quantities.")


class Promotion():
    pass

class SecondHalfPrice(Promotion):
    pass

class ThirdOneFree(Promotion):
    pass

class ThirtyPercent(Promotion):
    pass
