
class Store:
    """
    Represents a store that manages a collection of products
    """
    def __init__(self, product_store):
        """
        Initializing the store_list for class Store
        :param product_store: list of active products
        """
        self.product_store = product_store


    def __str__(self):
        """
        Assuring to print correct format instead of memory ID
        :return: the formatted printing string
        """
        return f"{self.product_store})"


    def add_product(self, product):
        """
        Adds products to the class Store-List when not in there yet
        :param product: product to be added
        :return: updated list
        """
        if product and product.name and product.price >= 1 and product.quantity >= 1:
            if product not in self.product_store:
                self.product_store.append(product)
                return self.product_store
        else:
            print("Invalid product. Cannot add to the store.")
        return None


    def remove_product(self, product):
        """
        Remove item from list when out of stock
        :param product:product to be checked
        :return: updated list of products
        """
        if product in self.product_store:
            if not product.is_active():
                self.product_store.remove(product)
                return self.product_store


    def get_total_quantity(self):
        """
        Calculates and display total amount of items in the store
        :return: total amount of items
        """
        total_quantity = 0
        for product in self.product_store:
            total_quantity += product.quantity
        return f"Total of {total_quantity} items in store"


    def get_all_products(self):
        """
        Display all available products in stock
        :return: list with active products
        """
        active_products = []
        for product in self.product_store:
            if product.is_active():
                active_products.append(product)

        if not active_products:
            print("No products listed")
        return active_products


    def order(self, shopping_list):
        """
        Calculates the total amount of the ordered items
        :param shopping_list: list of items which user want to buy
        :return: total price for order
        """
        total_cost_order = 0
        for product_name, quantity in shopping_list:
            for product in self.product_store:
                if product.name == product_name:
                    purchased_product = product.buy(quantity)
                    if purchased_product is not None:
                        total_cost_order += purchased_product[1]
                    else:
                        print(f"Could not complete purchase for {product.name}.")
                    break
        return f"Total amount: ${total_cost_order}"
