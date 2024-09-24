#from products import Product


class Store:
    def __init__(self, product_store):
        self.product_store = product_store
        for product in self.product_store:
            print(f"class Store print // {product}")


    def add_product(self, product):
        if product not in self.product_store:
            self.product_store.append(product)


    def remove_product(self, product):
        if product in self.product_store:
            #if self.deactivate == True:
           self.product_store.remove(product)


    def get_total_quantity(self):
        total_quantity = 0
        for product in self.product_store:
            total_quantity += product.quantity
        return total_quantity


    def get_all_products(self):
        active_products = []
        for product in self.product_store:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        total_cost_order = 0
        for product, quantity in shopping_list:
            purchase_amount = product.buy(quantity)  # This handles the check
            if purchase_amount is not None:
                total_cost_order += purchase_amount
            else:
                print(f"Could not complete purchase for {product.name}.")
        return f"Total amount: ${total_cost_order}"
