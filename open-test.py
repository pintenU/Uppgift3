import csv
import os
import locale

def load_data(filename): 
    products = []           #lista
    
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products
    
def get_product(id, products):
    return f"{products[id]['name']} \t {products[id]['price']}"
    
def view_products(products):
    #TODO: gör en nummerlista med enumerate (att använda index kommer inte fungera i längden)
    
    product_list = []
    for product in products:
        product_info = f"(#{product['id']}) {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)


#TODO: gör om så du slipper använda global-keyword (flytta inte "product = []")
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(view_products(products))
    
    id = int(input("vilken produkt vill du ta bort? "))




