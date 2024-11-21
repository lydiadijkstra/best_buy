# Store Application

This Python application is a simple store management system that allows users to:
- Browse products
- Check inventory
- Make purchases
- Apply promotions

The application supports various product types, including stocked, non-stocked, and limited-quantity items, with features to add promotions and calculate order totals.

---

## **Features**

1. **List Products**: Display all available products in the store.  
2. **Check Inventory**: Show the total quantity of stocked items.  
3. **Make an Order**: 
   - Allows users to select products and quantities.
   - Add products to a cart.
   - Check out with applied promotions and optional shipping costs.  
4. **Product Promotions**: Supports different types of discounts applied to products.

---

## **Project Structure**

```plaintext
__pycache__/                  # Cache folder for compiled Python files
main.py                       # Main script to run the store application
products.py                   # Defines Product classes and promotions
store.py                      # Implements the Store class for managing products and orders
test_product.py               # Contains tests for the Product and Store functionalities


Key Classes and Functions
Classes
Product: Base class representing a general product.
NonStockedProduct: Represents products that are always available, such as digital items.
LimitedProduct: Represents products with limited stock, such as shipping fees.
Promotion Classes:
SecondHalfPrice: Discounts the second product by 50%.
ThirdOneFree: Discounts every third product to free.
ThirtyPercent: Applies a 30% discount on a product.
Store: Manages the list of products, processes orders, and calculates total costs.
Functions
start(store, product_list): Displays the store menu, handles user selections, and calls appropriate functions.
convert_order(store, product_list): Manages the ordering process, prompting for product selection, quantities, and processing the cart.
main(): Initializes the store, sets up products and promotions, and launches the application.
Setup Instructions
Prerequisites
Python 3.x
Virtual Environment (recommended)
Installation
1. Clone the repository:

git clone <repository-url>
cd store-application

2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

python main.py

Usage
Start the Application: Run main.py to launch the store.
Choose an Option:
Press 1: List all products.
Press 2: View the total quantity of items in stock.
Press 3: Make an order.
Choose products, specify quantities, and proceed to checkout.
Press 4: Exit the application.
Example Usage
List Products

Available products:
  1. MacBook Air M2 - $1450, Quantity: 100
  2. Bose QuietComfort Earbuds - $250, Quantity: 500
  3. Google Pixel 7 - $500, Quantity: 250
  ...


Order Products
Select a product by number and enter the quantity.
Continue adding products or proceed to checkout by entering an empty response.
View the total cost, including promotions and shipping if applicable.
Testing
Run test_product.py to verify product and store functionalities:

pytest test_product.py

Example Promotions
Second Half Price: Buy two, get the second one at half price.
Third One Free: Buy three, get the third one free.
Thirty Percent: Flat 30% discount on the product.

License
This project is open-source and licensed under the MIT License.
