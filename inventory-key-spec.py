import os
import locale

class Product:
    def __init__(self, name, desc, price, quantity):
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity
      
    def __str__(self):
        return f"{self.name} {self.desc} {locale.currency(self.price, grouping=True)} ({self.quantity})"

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
        
        print("\n")
        inventory_list = "\n".join(f"{idx}. {str(product)}" for idx, product in enumerate(self.products, 1))

        return f"Current Inventory:\n{inventory_list}"


    def change_product(self, id, name=None, desc="(n/a)", price=0, quantity=1):
        if name is None:
            return "No name provided"
        elif id < 0 or id >= len(self.products):
            return "Invalid product ID."
        else:
            product = self.products[id]
            product.name = name
            product.desc = desc
            product.price = price
            product.quantity = quantity
            return f"Product with #{id} updated successfully."
            
            
if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

    
    os.system("cls")
    
    inventory = Inventory()

    print(inventory.add_product("Smarty Watch","If you wanna feel better than everyone else",1000,2))
    print(inventory.add_product("eyePhone Pro 17","Made to break easily for your inconvienence",14000,3))
    print(inventory.add_product("Boomerang Pro Max","Made in Australia for the next generation of cowboys",549,17))
    print(inventory.add_product("A floating device","I'm hydrophobic man",1000,9))
    print(inventory.change_product(0, "SmartWatch","Just a plain ol' smartwatch from the 2021s",3000,1))

    print(inventory.view_inventory())
        
    #TODO: Skapa check_inventory (visa produkter)
    #TODO: Skapa add_item-metod för produkter
    #TODO: Skapa remove-metod för produkter
    #TODO: (Överkurs) Skapa sparfunktion som sparar i en fil
    #TODO: (Överkurs) Gör så man kan lägga in produkter i programmet och hantera lagret med terminalen
    #TODO: (Frivillig) Skapa en metod som visar produkten som ni har mest av