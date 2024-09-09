import csv
import os
import locale
from time import sleep


def load_data(filename): 
    products = [] 
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(        #list
                {                    #dictionary
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products

#gör en funktion som hämtar en produkt

def get_product(products, id):
    if id < 0 or id > len(products):
        return "Produkten hittas inte"
    else:
        return f"{products[id]['name']} {products[id]['desc']}"
    
    
def remove_product(products, id):
    print(id)
    temp_product = None

    for product in products:
        if product["id"] == id:
            temp_product = product
            break  # Avsluta loopen så snart produkten hittas

    if temp_product:
        products.remove(temp_product)
        return f"Product: {id} {temp_product['name']} was removed"
    else:
        return f"Product with id {id} not found"


def get_products(products):
    product_list = []
    for product in products:
        product_info = f"{product['id']} {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)


#TODO: gör om så du slipper använda global-keyword (flytta inte "product = []")
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')
products = load_data('db_products.csv')


while True:
    try:
        os.system('cls')
        print("\n")
        print(get_products(products))
        
        id = int(input("Ta bort produkt (ange nummer): ")) 

        print(remove_product(products, id))
        sleep(0.2)
    except:
        print("Sweet summer child du behöver skriva siffror")
        
    
