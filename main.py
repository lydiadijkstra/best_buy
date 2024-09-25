from products import Product
from store import Store


def start(store):
    print("""Store Menu:
\t1. List all products in store
\t2. Show total amount in store
\t3. Make an order
\t4. Quit""")


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()