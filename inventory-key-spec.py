class Product:
    def __init__(self, name, desc, price, quantity):
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity
    
    
class Inventory:
    def __init__(self):
        self.products = []
        
    def add_product(self, name, desc, price, quantity):
        self.products.append(Product(name, desc, price, quantity))
        
    def view_product(self):
        return 
        
    #TODO: Skapa check_inventory (visa produkter)
    #TODO: Skapa add_item-metod för produkter
    #TODO: Skapa remove-metod för produkter
    #TODO: (Överkurs) Skapa sparfunktion som sparar i en fil
    #TODO: (Överkurs) Gör så man kan lägga in produkter i programmet och hantera lagret med terminalen
    #TODO: (Frivillig) Skapa en metod som visar produkten som ni har mest av