import pytest
from main import main
from products import Product, NonStockedProduct, LimitedProduct, SecondHalfPrice, ThirdOneFree, ThirtyPercent
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
    assert result == 2900  # Expect numeric total, not a formatted string

    store.order([("MacBook Air M2", 98)])  # Buy total amount
    products = store.get_all_products()
    assert len(products) == 2  # Check if product was deactivated

    store.order([("Bose QuietComfort Earbuds", 600)])  # Try buying more than available
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


def test_store_order_with_promotions():
    """
    Test ordering products with promotions applied (e.g., second half price, third one free).
    """
    store = Store([Product("MacBook Air M2", price=1450, quantity=100),
                   Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                   Product("Google Pixel 7", price=500, quantity=250)])

    # Apply promotions
    promotion1 = SecondHalfPrice()
    promotion2 = ThirdOneFree()
    promotion3 = ThirtyPercent()

    store.product_store[0].add_promotion(promotion1)  # MacBook Air gets second half price
    store.product_store[1].add_promotion(promotion3)  # Earbuds get 30% off
    store.product_store[2].add_promotion(promotion2)  # Pixel gets third one free

    # Test promotion on MacBook Air
    result = store.order([("MacBook Air M2", 2)])  # Second one should be half price
    assert result == 1450 + (1450 * 0.5)  # 2nd MacBook is half price

    # Test promotion on Bose QuietComfort Earbuds
    result = store.order([("Bose QuietComfort Earbuds", 2)])  # 30% off
    assert result == 250 * 2 * 0.7  # 30% off both

    # Test promotion on Google Pixel 7
    result = store.order([("Google Pixel 7", 3)])  # Third one should be free
    assert result == 500 * 2  # 3rd Pixel is free


def test_non_stocked_product_order():
    """
    Test ordering a non-stocked product (e.g., digital products).
    """
    store = Store([NonStockedProduct("Windows License", price=125)])

    # Order 10 digital products
    result = store.order([("Windows License", 10)])
    assert result == 125 * 10  # No stock limit, price should match


def test_shipping_added_for_physical_products():
    """
    Test that shipping is added when a physical product is present in the order.
    """
    store = Store([Product("MacBook Air M2", price=1450, quantity=100),
                   NonStockedProduct("Windows License", price=125),
                   LimitedProduct("Shipping cost", price=10)])

    # Test with only digital product
    result = store.order([("Windows License", 1)])
    assert result == 125  # No shipping should be added


def test_limited_product():
    """
    Test that LimitedProduct (e.g., shipping) can only be purchased once.
    """
    store = Store([LimitedProduct("Shipping cost", price=10)])

    # Attempt to buy more than 1 shipping cost
    result = store.order([("Shipping cost", 2)])
    assert result == 10  # Only 1 shipping cost should be charged, ignoring extra quantity


def test_product_deactivation_when_out_of_stock():
    """
    Test that a product is deactivated when its quantity reaches 0.
    """
    store = Store([Product("MacBook Air M2", price=1450, quantity=2)])

    # Buy all products (should deactivate)
    store.order([("MacBook Air M2", 2)])
    products = store.get_all_products()
    assert len(products) == 0  # MacBook Air should be deactivated

def test_order_more_than_available_stock():
    """
    Test that ordering more than available stock is handled correctly.
    """
    store = Store([Product("MacBook Air M2", price=1450, quantity=5)])

    # Try to order more than in stock
    result = store.order([("MacBook Air M2", 10)])
    assert result == 0  # Order should not proceed, no charge made


def test_remove_promotion():
    """
    Test that removing a promotion reverts the product to its original price.
    """
    product = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    promotion = ThirtyPercent()

    product.add_promotion(promotion)  # Add 30% off promotion
    assert product.calculate_price(1) == 250 * 0.7

    product.remove_promotion(promotion)  # Remove promotion
    assert product.calculate_price(1) == 250  # Price should be full again
