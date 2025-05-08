# Inventory Management System for a Multi-Store Chain
# A multi-store retail chain wants to build an inventory management system to track products across all its stores. The system should allow the following operations

# problem: 
# 1) Add a new product: Each product has a unique ID, name, price, and stock levels in each store.
# 2) Search for a product: Search for a product by ID or name and display its details, including the stock level in each store.
# 3) Transfer stock: Transfer stock of a product from one store to another and update the inventory.
# 4) Find low-stock products: Identify products that have a stock level below a given threshold in any store.
# 5) Generate a sales report: Generate a report that lists all sold products with their sales data (quantity sold, revenue generated) for a specific period.

# Example Input/Output:
# Add product: {ID: 101, Name: "Laptop", Price: 750, Stock: {"Store1": 20, "Store2": 15}}
# Low-stock products (threshold: 10): ["Mouse", "Keyboard"]
# Sales report: [{Product: "Laptop", Quantity: 5, Revenue: 3750}]

import pdb
products = [{'ID': 1, 'Name': 'Laptop', 'Price': 750, 'Stock': {'Store1': 20, 'Store2': 15}}, {'ID': 2, 'Name': 'Computer', 'Price': 850, 'Stock': {'Store1': 12, 'Store2': 10}}]

# for i in range(1,3):
#     product_id = i
#     product_name = input("Enter product name: ")
#     product_price = input("Enter product price: ")
#     product_stock_store1 = input("Enter product stock at store 1: ")
#     product_stock_store2 = input("Enter product stock at store 2: ")
#     products.append({
#                     "ID": int(product_id), 
#                     "Name": product_name, 
#                     "Price": int(product_price), 
#                     "Stock": {"Store1": int(product_stock_store1), "Store2": int(product_stock_store2)}
#                 })
# print(products)

# print("Search Product by id or name")
# key = input("Enter unique id or name ")

# for product in products:
#     if str(product["ID"]) == key or product["Name"].lower() == key.lower():
#         print(product)
#         break

print("Transfer stock")
for product in products:
    print(product["Stock"])
