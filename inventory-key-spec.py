import os

class Product:
    def __init__(self, name, desc, price, quantity):
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity
      
    def __str__(self):
        return f"{self.name}: {self.desc} - ${self.price:.2f} ({self.quantity} in stock)"

    def __repr__(self):
        return self.__str__()
    
class Inventory:
    def __init__(self):
        self.products = []
        
    def add_product(self, name, desc, price, quantity):
        new_product = Product(name, desc, price, quantity)
        self.products.append(new_product)
        return f"Added {new_product.name} to the inventory."

    def view_inventory(self):
        if not self.products:
            return "Inventory is empty."
        inventory_list = "\n".join(str(product) for product in self.products)
        
        return f"Current Inventory:\n{inventory_list}"


if __name__ == "__main__":
    os.system("cls")
    
    inventory = Inventory()

    print(inventory.add_product("laptop","dsvf",1,1))
    print(inventory.view_inventory())
        
    #TODO: Skapa check_inventory (visa produkter)
    #TODO: Skapa add_item-metod för produkter
    #TODO: Skapa remove-metod för produkter
    #TODO: (Överkurs) Skapa sparfunktion som sparar i en fil
    #TODO: (Överkurs) Gör så man kan lägga in produkter i programmet och hantera lagret med terminalen
    #TODO: (Frivillig) Skapa en metod som visar produkten som ni har mest av