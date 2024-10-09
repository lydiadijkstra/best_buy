import pytest
from main import main
from products import Product
from store import Store

"""
get_quantity(): Ensure it returns the correct quantity for a product.
set_quantity(): Check if the quantity is updated correctly and triggers deactivation if necessary.
deactivate(): Verify that the product is deactivated and quantity is set to 0.
is_active(): Test whether the function correctly identifies if a product is active or inactive.
buy(): Ensure it correctly reduces the stock when a product is bought and calculates the total amount.
Store Class:

add_product(): Verify that new products are correctly added to the store.
remove_product(): Ensure products are removed from the store when deactivated.
get_total_quantity(): Check if it accurately calculates the total quantity of products in the store.
get_all_products(): Verify that only active products are returned.
order(): Test that the total cost of an order is correctly calculated and stock is deducted appropriately.
"""

def test_product_get_quantity():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    product2 = Product(name="MacBook Air M2", price=1450, quantity=0)
    product3 = Product(name="MacBook Air M2", price=1450, quantity=-40)


    expected_outcome = "Product: MacBook Air M2\nQuantity: 100"
    expected_outcome2 = "Product: MacBook Air M2\nQuantity: 0"
    expected_outcome3 = "Product: MacBook Air M2\nQuantity: -40"

    assert product.get_quantity() == expected_outcome
    assert product2.get_quantity() == expected_outcome2
    assert product3.get_quantity() == expected_outcome3


def test_product_set_quantity():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)

    product.set_quantity(50)
    assert product.quantity == 150

    product.set_quantity(-200)
    assert product.quantity == -50
    assert product.deactivate is True

def test_product_buy():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)

    assert product.buy(20) == (20, 29000)  # Expecting (quantity bought, total cost)
    assert product.quantity == 80

def test_store_add_product():
    store = Store([Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ])
    product = Product(name="Test product", price=299, quantity=50)
    store.add_product(product)
    assert product in store.product_store

def test_store_remove_product():
    store = Store([Product("MacBook Air M2", price=1450, quantity=100),
                   Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                   Product("Google Pixel 7", price=500, quantity=250)
                   ])

    product_to_remove = store.product_store[0]
    product_to_remove.set_quantity(-100)  # Reduce quantity to 0
    product_to_remove.deactivate_product()  # Manually deactivate the product
    store.remove_product(product_to_remove) # Remove function to remove
    assert product_to_remove not in store.product_store

def test_store_get_total_quantity():
    store = Store([Product("MacBook Air M2", price=1450, quantity=100),
                   Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                   Product("Google Pixel 7", price=500, quantity=250)
                   ])

    total_quantity = store.get_total_quantity()
    assert total_quantity == "Total of 850 items in store"
    store.product_store[0].deactivate_product()
    total_quantity = store.get_total_quantity()
    assert total_quantity == "Total of 750 items in store"

def test_store_get_all_products():
    pass

def test_store_order():
    pass
