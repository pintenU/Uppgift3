import locale

class Product:
    def __init__(self, category, name, price, quantity):
        self.category = category
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {locale.currency(self.price, grouping=True)}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, category, name, price, quantity):
        # Create a Product instance and add it to the inventory
        new_product = Product(category, name, price, quantity)
        self.products.append(new_product)
        return f"Added {new_product.name} to the inventory."

    def update_quantity(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                product.quantity += quantity
                return f"Updated {product.name} quantity to {product.quantity}"
        return "Product not found."

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return f"{product_name} has been removed from the inventory."
        return "Product not found."

    def display_inventory(self):
        if not self.products:
            return "Inventory is empty."
        inventory_list = "\n".join(str(product) for product in self.products)
        return f"Current Inventory:\n{inventory_list}"


# Example Usage
if __name__ == "__main__":
    
    locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  
    # Create an inventory instance
    inventory = Inventory()

    # Add products to inventory by passing details directly
    print(inventory.add_product("Electronics", "Laptop", 22000.00, 1, 10))
    print(inventory.add_product("Electronics", "Phone", 8000.00, 1, 20))

    # Display inventory
    print(inventory.display_inventory())

    # Update the quantity of a product
    print(inventory.update_quantity("Laptop", 5))

    # Display updated inventory
    print(inventory.display_inventory())

    # Remove a product
    print(inventory.remove_product("Phone"))

    # Display inventory after removal
    print(inventory.display_inventory())

    
#TODO: Skapa check_inventory (visa produkter)
#TODO: Skapa add_item-metod för produkter
#TODO: Skapa remove-metod för produkter
#TODO: Skapa sparfunktion
#TODO: (Frivillig) Skapa en metod som visar mest sålda produkt
        