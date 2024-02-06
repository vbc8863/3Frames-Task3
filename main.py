
from product_configurator import Product, ProductConfigurator

def get_user_input(prompt):
    return input(prompt).strip()

def display_product(product):
    print(f"Product ID: {product['product_id']}, Category: {product['category']}, Description: {product['description']}")

def search_products(configurator):
    print("\nAvailable categories: Books, Electronics, Clothing") 
    category = get_user_input("Enter the product category (leave blank to search all categories): ").strip()

    if category.lower() not in ["books", "electronics", "clothing"]:
        print("Invalid category. Please choose from the available categories.")
        return

    query = get_user_input("Enter the search query: ").strip()

    results = configurator.search_products(query, category)
    
    if results:
        print("Search Results:")
        for product in results:
            display_product(product)
    else:
        print("No matching products found.")

    configurator.clear_search_results()

def main():
    configurator = ProductConfigurator()

    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Search Products")
        print("3. Exit")

        choice = get_user_input("Enter your choice (1-3): ")

        if choice == "1":
            configurator.add_product()
        elif choice == "2":
            search_products(configurator)
        elif choice == "3":
            configurator.save_to_file()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
