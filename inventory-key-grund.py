class Product:
    def __init__(self):
        self.products = [
            {
                "name": "Mobiltelefon",
                "desc": "En fin mobil",
                "price": 10000,
                "quantity": 2
            },
            {
                "name": "Dator",
                "desc": "En fin dator",
                "price": 20000,
                "quantity": 7
            },
            {
                "name": "iPad",
                "desc": "En fin ipad",
                "price": 12000,
                "quantity": 11
            }
            ]
        
    def check_inventory(self):
        return self.products 
        

get_products = Product()
products = get_products.check_inventory()

def list_inventory():
    for i in range(len(products)):
        print(products[i]["name"])


list_inventory()

    
    
    
        
    #TODO: Skapa check_inventory (visa produkter)
    #TODO: Skapa add_item-metod för produkter
    #TODO: Skapa remove-metod för produkter
    #TODO: (Överkurs) Skapa sparfunktion som sparar i en fil
    #TODO: (Överkurs) Gör så man kan lägga in produkter i programmet och hantera lagret med terminalen