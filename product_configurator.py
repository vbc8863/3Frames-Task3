# File: product_configurator.py

import json

class Product:
    def __init__(self, product_id, category, description, details):
        self.product_id = product_id
        self.category = category
        self.description = description
        self.details = details

class ProductConfigurator:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.products = []
        self.search_results = [] 
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                self.products = json.load(file)
        except FileNotFoundError:
            pass 

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.products, file, indent=2)

    def add_product(self):
        product_id = len(self.products) + 1
        category = input("Enter the product category: ")
        description = input("Enter the product description: ")
        details = input("Enter the product details (comma-separated): ").split(',')

        product = {
            'product_id': product_id,
            'category': category,
            'description': description,
            'details': details
        }

        self.products.append(product)
        
        print("Product added successfully!")

    def search_products(self, query, category=None):
        self.search_results = []
        query = query.lower()  
        for product in self.products:
            if (category is None or category.lower() == product['category'].lower()) and \
               (query in product['category'].lower() or \
               query in product['description'].lower() or \
               any(query in detail.lower() for detail in product['details'])):
                self.search_results.append(product)

        return self.search_results

    def clear_search_results(self):
        self.search_results = []

