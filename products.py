from abc import ABC


class Product(ABC):
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
        self.promotions = []  # List of promotions applied to the product


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
        Check if product is in stock and set to active.
        Non-stocked products are always active.
        :return: True if active, False otherwise
        """
        if isinstance(self, NonStockedProduct):
            return True  # Non-stocked products are always active
        return self.active and self.quantity >= 1


    def show(self):
        """
        Display all products incl. price and quantity
        :return: print name, price and quantity
        """
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")


    def add_promotion(self, promotion):
        """
        Add a promotion to the product.
        """
        if promotion not in self.promotions:
            self.promotions.append(promotion)

    def remove_promotion(self, promotion):
        """R
        emove a promotion from the product
        """
        if promotion in self.promotions:
            self.promotions.remove(promotion)


    def calculate_price(self, quantity):
        """
        Calculate the price after applying all promotions
        :return: total price
        """
        final_price = quantity * self.price
        for promotion in self.promotions:
            final_price = promotion.apply_promotion(self, quantity)
        return final_price


    def buy(self, quantity):
        """
        Checks stock vs amount, substracts the amount from stock
        :return: quantity, total amount
        """
        if quantity > self.quantity:
            print(f"Purchase not possible, {self.name} requested: {quantity}. Available: {self.quantity}")
            return None
        else:
            self.quantity -= quantity
            total_purchase_amount = self.calculate_price(quantity)
            return quantity, total_purchase_amount



class NonStockedProduct(Product):
    """Digitial Products which need no stock amount"""
    def __init__(self, name, price):
        super().__init__(name, price, quantity=None)  # quantity is None for non-stocked products

    def buy(self, amount):
        """
        Non-stocked products can be bought in any amount (quantity does not apply).
        :param amount: number of licenses or units of digital product
        :return: tuple of (purchased amount, total purchase amount)
        """
        total_purchase_amount = self.price * amount
        return amount, total_purchase_amount

    def show(self):
        """
        Display details of a non-stocked product (e.g., digital product).
        """
        super().show()
        print(f"{self.name} is a non-stocked product (digital or service).")


class LimitedProduct(Product):
    """Handles the limited products such as shipping = max 1 in shoppingcart"""
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


###############################################################################################


class Promotion:
    """Handles the different promos for the products"""
    def __init__(self, name):
        self.name = name


    def apply_promotion(self, product, quantity):
        """
        Base method for applying promotions.
        :param product: The product to apply the promotion on
        :param quantity: The quantity being purchased
        :return: The discounted price
        """
        raise NotImplementedError("Subclasses must implement this method")


class SecondHalfPrice(Promotion):
    """Handles the promo second item 50% off"""
    def __init__(self):
        super().__init__("Second Half Price")


    def apply_promotion(self, product, quantity):
        """
    Applies the 'Second Half Price' promotion to the given product.
    :param product: The product to which the promotion is applied.
                    Must have a price attribute representing the full price per unit.
    :param quantity: The number of units the customer is purchasing.
    :return: The total cost after applying the promotion.
    """
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    """Handles the promo Third item for free"""
    def __init__(self):
        super().__init__("Third One Free")

    def apply_promotion(self, product, quantity):
        """
           Applies the 'Third one for free' promotion to the given product.
           :param product: The product to which the promotion is applied.
                           Must have a price attribute representing the full price per unit.
           :param quantity: The number of units the customer is purchasing.
           :return: The total cost after applying the promotion.
           """
        full_price_items = quantity - (quantity // 3)
        return full_price_items * product.price


class ThirtyPercent(Promotion):
    """Handles the promo thirty percent offf"""
    def __init__(self):
        super().__init__("30% Off")

    def apply_promotion(self, product, quantity):
        """
           Applies the 'Second Half Price' promotion to the given product.
           :param product: The product to which the promotion is applied.
                           Must have a price attribute representing the full price per unit.
           :param quantity: The number of units the customer is purchasing.
           :return: The total cost after applying the promotion.
           """
        return quantity * product.price * 0.7
