from main import *
from products import *

class Store:
    def __init__(self):
        self.store = []

    def add_product(self, product):
        if product in self.store:
            return
        else:
            self.store.append(product)

    def remove_product(self, product, deactivate):
        if product in self.store:
            if self.deactivate == True:
                self.store.remove(product)

    def get_total_quantity(self, quantity):
        total_quantity = 0
        total_quantity = total_quantity + self.quantity
        return total_quantity

    def get_all_products(self):
        pass

    def order(self, shopping_list):
        pass

