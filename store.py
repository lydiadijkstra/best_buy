from products import Product, NonStockedProduct, LimitedProduct


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
        Calculates and display total amount of items in the store, excluding non-stocked products.
        :return: total amount of items
        """
        total_quantity = 0
        for product in self.product_store:
            if product.quantity is not None:  # Exclude non-stocked products
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

    @staticmethod
    def add_shipping(shopping_cart, active_products):
        """
        Adds shipping cost to every order with at least 1 physical products, not excluding digital products
        :param shopping_cart:
        :return:
        """
        print("Current SC = ", shopping_cart)
        has_physical_product = any(
            any(product.name == item[0] and not isinstance(product, NonStockedProduct) for product in active_products)
            for item in shopping_cart
        )
        print("Has physical product", has_physical_product)

        if has_physical_product:
            shipping_cost_in_cart = any(item[0] == "Shipping cost" for item in shopping_cart)

            if not shipping_cost_in_cart:  # If shipping is not already in the cart
                shipping_cost = LimitedProduct(name="Shipping cost", price=10)
                shopping_cart.append((shipping_cost.name, 1))  # Add 1x shipping cost
                print("Shipping added to cart", shopping_cart)
            else:
                # If shipping is already in the cart, set its quantity to 1 (ignoring user input)
                shopping_cart = [(product_name, 1) if product_name == "Shipping cost" else (product_name, quantity)
                                 for product_name, quantity in shopping_cart]
                print("Shipping quantity set to 1", shopping_cart)

        return shopping_cart


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
                    if isinstance(product, LimitedProduct) and product.name == "Shipping cost":
                        total_cost_order += product.price
                    else:
                        purchased_product = product.buy(quantity)
                        if purchased_product is not None:
                            total_cost_order += purchased_product[1]
                        else:
                            print(f"Could not complete purchase for {product.name}.")
                        break

        #if any(item[0] == "Shipping cost")
        print(list(item for item in shopping_list))
        return total_cost_order
