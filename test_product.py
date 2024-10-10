import pytest
from main import main
from products import Product
from store import Store


# Test the functions in the products.py file


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


# Test the functions in the store.py file

"""
def test_store_add_product():
    store = Store([Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ])
    product = Product(name="Test product", price=299, quantity=50)
    store.add_product(product)
    assert product in store.product_store
"""

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
    store = Store([Product("MacBook Air M2", price=1450, quantity=100),
                   Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                   Product("Google Pixel 7", price=500, quantity=250)
                   ])

    products = store.get_all_products()
    expected_products = [Product("MacBook Air M2", price=1450, quantity=100), Product("Bose QuietComfort Earbuds", price=250, quantity=500), Product("Google Pixel 7", price=500, quantity=250)]
    assert len(products) == len(expected_products)

    store.product_store[0].deactivate_product()
    products = store.get_all_products()
    expected_products = [Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                         Product("Google Pixel 7", price=500, quantity=250)]
    assert len(products) == len(expected_products)


def test_store_order():
    """
    Test function for ordering products and deducting quantity.
    Test deactivation when quantity reaches 0
    Test that order is not proceeded when buying-quantity is bigger than warehouse quantity
    :return:
    """
    store = Store([Product("MacBook Air M2", price=1450, quantity=100),
                   Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                   Product("Google Pixel 7", price=500, quantity=250)
                   ])

    result = store.order([("MacBook Air M2", 2)])
    assert result == "Total amount: $2900"

    store.order([("MacBook Air M2", 98)]) # Buy total amount
    products = store.get_all_products()
    assert len(products) == 2 # Check if product was deactivated

    store.order([("Bose QuietComfort Earbuds", 600)])  # Buy total amount
    products = store.get_all_products()
    assert len(products) == 2  # Check if order was blocked, same amount of products


def test_store_add_product():
    """
    Test function for adding valid and invalid products
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)

    # Add qualified product:
    best_buy.add_product(Product("testproduct", price=1450, quantity=100))
    products = best_buy.get_all_products()
    expected_products = [Product(name="MacBook Air M2", price=1450, quantity=100),
                         Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                         Product("Google Pixel 7", price=500, quantity=250),
                         Product("testproduct", price=1450, quantity=100)]
    assert len(products) == len(expected_products)

    # Add unqualified product - empty name:
    best_buy.add_product(Product("", price=1, quantity=103847))
    products = best_buy.get_all_products()
    expected_products = [Product(name="MacBook Air M2", price=1450, quantity=100),
                         Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                         Product("Google Pixel 7", price=500, quantity=250),
                         Product("testproduct", price=1450, quantity=100)]
    assert len(products) == len(expected_products)

    # Add unqualified product - negative price:
    best_buy.add_product(Product("test_object", price=-11, quantity=103847))
    products = best_buy.get_all_products()
    expected_products = [Product(name="MacBook Air M2", price=1450, quantity=100),
                         Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                         Product("Google Pixel 7", price=500, quantity=250),
                         Product("testproduct", price=1450, quantity=100)]
    assert len(products) == len(expected_products)

    # Add unqualified product - negative quantity:
    best_buy.add_product(Product("test_object", price=11, quantity=-1))
    products = best_buy.get_all_products()
    expected_products = [Product(name="MacBook Air M2", price=1450, quantity=100),
                         Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                         Product("Google Pixel 7", price=500, quantity=250),
                         Product("testproduct", price=1450, quantity=100)]
    assert len(products) == len(expected_products)

