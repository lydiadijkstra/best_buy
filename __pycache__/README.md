Store Application
This Python application is a simple store management system that allows users to browse products, check inventory, make purchases, and apply promotions. The application supports various product types, including stocked, non-stocked, and limited-quantity items, with features to add promotions and calculate order totals.

Features
List Products: Display all available products in the store.
Check Inventory: Show the total quantity of stocked items.
Make an Order: Allows users to select products and quantities, add them to a cart, and check out with applied promotions and optional shipping costs.
Product Promotions: Supports different types of promotions that can be applied to products for discounts.
Project Structure
bash
Code kopieren
__pycache__/
main.py                # Main script to run the store application
products.py            # Defines Product classes and promotions
store.py               # Implements the Store class for managing products and orders
test_product.py        # Contains tests for the Product and Store functionalities
Key Classes and Functions
Classes
Product: Base class representing a general product.
NonStockedProduct: Represents products that are always available, such as digital items.
LimitedProduct: Represents products with limited stock, such as shipping fees.
SecondHalfPrice, ThirdOneFree, ThirtyPercent: Promotion classes that offer different types of discounts.
Store: Manages the list of products, processes orders, and calculates total costs.
Functions
start(store, product_list): Displays the store menu, handles user selections, and calls appropriate functions.
convert_order(store, product_list): Manages the ordering process, prompting for product selection and quantities, and processing the cart.
main(): Initializes the store, sets up products and promotions, and launches the store application.
Setup Instructions
Prerequisites
Python 3.x
Virtual Environment (recommended)
Installation
Clone the repository:

bash
Code kopieren
git clone <repository-url>
cd store-application
Install dependencies: Install any additional dependencies using:

bash
Code kopieren
pip install -r requirements.txt
Run the Application:

bash
Code kopieren
python main.py
Usage
Start the Application: Run main.py to start the store application.
Choose an Option:
Press 1 to list all products.
Press 2 to view the total quantity of items in stock.
Press 3 to make an order. You will be prompted to choose products, quantities, and proceed to checkout.
Press 4 to exit the application.
Example Usage
List Products:

plaintext
Code kopieren
Available products:
  1. MacBook Air M2 - $1450, Quantity: 100
  2. Bose QuietComfort Earbuds - $250, Quantity: 500
  3. Google Pixel 7 - $500, Quantity: 250
  ...
Order Products:

Select a product by number, enter the quantity, and continue.
Enter an empty response to proceed to checkout.
The total cost, including promotions and shipping if applicable, will be displayed.
Testing
Run test_product.py to verify the functionality of products and store logic:

bash
Code kopieren
pytest test_product.py
Example Promotions
Second Half Price: Buy two, get the second one at half price.
Third One Free: Buy three, get the third one free.
Thirty Percent: Flat 30% discount on the product.
License
This project is open-source and licensed under the MIT License.
