from products import Product
from store import Store


def start(store, product_list):
    """
    Display menu, prompt for menu number, call suitable function
    :param store: store.py with class Store
    :param product_list: initial list of products
    :return: store and list of products
    """
    while True:
        print("""\n------------ Store Menu: ------------\n
    \t1. List all products in store
    \t2. Show total amount of items in store
    \t3. Make an order
    \t4. Quit""")
        menu_choice = input("\nPlease choose a number: \n")

        if menu_choice == "1":
            products = store.get_all_products()
            print("\nAvailable products:")
            for id_nr, product in enumerate(products, 1):
                print(f"\t{id_nr}. {product}")
        elif menu_choice == "2":
            print(store.get_total_quantity())
        elif menu_choice == "3":
            convert_order(store, product_list)
        elif menu_choice == "4":
            print("Thank you for your order, have a nice day!")
            break
        else:
            print("Please enter a valid number (1-4)")
            continue
    return store, product_list


def convert_order(store, product_list):
    """
    Ask for item and quantity and purchase order
    :param store: store.py with class Store
    :param product_list: initial list of products
    """
    numerate = 0
    print("\n")
    active_products = store.get_all_products()
    print("\nAvailable products:")
    for product in active_products:
        numerate += 1
        print(f"\t{numerate}. {product}")
    print("\nWhen you want to finish order, enter empty text.")
    shopping_list = []
    while True:
        choice_product = input("Which product number do you want to buy? \n")
        if choice_product == "":
            break

        try:
            choice_product = int(choice_product)
        except ValueError:
            print(f"Please enter a valid number between 1 and {len(product_list)}")
            continue
        except TypeError:
            print(f"Please enter a valid number between 1 and {len(product_list)}")
            continue

        if choice_product < 1 or choice_product > len(product_list):
            print(f"No such item, please enter a number between 1 and {len(product_list)}")
            continue
        choice_amount = input("What amount do you want? \n")
        if choice_amount == "":
            break

        try:
            choice_amount = int(choice_amount)
        except ValueError:
            print("Please enter a valid amount of items")
            continue
        except TypeError:
            print("Please enter a valid amount of items")
            continue

        chosen_product = active_products[choice_product - 1]
        product_and_quantity = (chosen_product.name, choice_amount)
        shopping_list.append(product_and_quantity)
    if shopping_list:
        order_summary = store.order(shopping_list)
        print(order_summary)
    else:
        print("No items were added to your order")


def main():
    """
    Main function with list of items and call the start function
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    #start(best_buy, product_list) # Run the store to order products


if __name__ == "__main__":
    main()
