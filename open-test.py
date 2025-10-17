import csv
import os
import locale
from time import sleep


        #lista


def format_currency(value):
    return locale.currency(value,grouping=True)

def list_products(products):
    for idx, product in enumerate(products, 1):
        print(f"{idx}: {product['name']} {product['price']}")

def add_product(products):

    find_max = max(products, key=lambda id: id['id'] )
    max_id = find_max['id']
    
    new_id = max_id + 1


    name = input("Namn: ")
    desc = input("Beskrivning: ")
    price = float(input("Pris:  "))
    quantity = int(input("kvantitet: "))

    product = {}

    product['id'] = new_id
    product['name'] = name
    product['desc'] = desc
    product['price'] = price
    product['quantity'] = quantity

    products.append(product)

    return products

def save_products(filepath, products):

    csv_file_path = "db_products.csv"

# Write the products data to a CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "description", "price", "quantity"])
        writer.writeheader()  # Write the header row
        writer.writerows(products)  # Write the product data

    print(f"Data successfully saved to {csv_file_path}")
    return f"OK"

def change_product(placeholder, name, desc, price, quantity):

            print("du vill ändra produkt:", placeholder['name'])

            name = input("nytt namn: ")
            desc = input("ny beskrivning: ")
            price = float(input("nytt pris"))
            quantity = int(input("ny mängd"))

            placeholder['name'] = name
            placeholder['desc'] = desc
            placeholder['price'] = price
            placeholder['quantity'] = quantity
    
    

def remove_product(products):


    pass


def view_products(idx, products):
    product = products[idx - 1]
    print(f"product: {product['name']} {product['desc']} {product['quantity']}")
    return product

def load_data(filename): 
    products = [] 

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



os.system('cls')
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')


while True:
    list_products(products)
    print("Vill du visa en product(1) eller vill du lägga till en product(2) eller ändra produkt(3) eller ta bort produkt(4)")
    option = int(input())

    if option ==1:
        idx = int(input("Välj product med nummer: "))
        product = view_products(idx, products)
        input()

    elif option == 2:
        add_product(products)
        
    elif option == 3:
        try:
            index = input("vilken produkt (id) vill du ändra? ")
        except IndexError:
            print("Felaktigt index")

        if 1<= index <= len(products):
            placeholder = products[index -1]

        change_product(placeholder)
        

    elif option == 4:
        remove_product()

    elif option == 5:
        save_products(products)

    else:
        print("Felaktigt nummer")

