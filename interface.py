import json
import tkinter as tk
from tkinter import messagebox

class ProductConfigurator:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.products = []
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

    def search_products(self, query, category=None):
        results = []
        query = query.lower()
        for product in self.products:
            if (category is None or category.lower() == product['category'].lower()) and \
               (query in product['category'].lower() or \
               query in product['description'].lower() or \
               any(query in detail.lower() for detail in product['details'])):
                results.append(product)

        return results

class ProductConfiguratorUI:
    def __init__(self, configurator):
        self.configurator = configurator
        self.root = tk.Tk()
        self.root.title("Product Configurator")

        self.query_var = tk.StringVar()

        self.create_ui()

    def create_ui(self):
        # Labels and Entry Fields
        tk.Label(self.root, text="Search Product:").grid(row=0, column=0, padx=10, pady=5)
        search_entry = tk.Entry(self.root, textvariable=self.query_var, width=30, font=('Arial', 14))
        search_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)
        search_entry.focus()

        tk.Button(self.root, text="Search", command=self.search_products).grid(row=1, column=0, columnspan=3, pady=10)

    def search_products(self):
        query = self.query_var.get()
        results = self.configurator.search_products(query)
        if results:
            messagebox.showinfo("Search Results", "\n".join([f"{result['category']}: {result['description']}" for result in results]))
        else:
            messagebox.showinfo("Search Results", "No matching products found.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    configurator = ProductConfigurator()
    ui = ProductConfiguratorUI(configurator)
    ui.run()
