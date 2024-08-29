
import os
import csv
import locale
import curses 


def get_product_names(products):
    product_names = []
    for id in products:
        product_names.append(products[id]["name"])
    
    return product_names

def load_data(filename):
    products = {}
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['description']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
             # Add the product details to the dictionary
            products[id] = {
                "name": name,
                "description": desc,
                "price": price,
                "quantity": quantity
            }
    
    return products

def main(stdscr): 
    curses.curs_set(0)
    
    items = get_product_names(products)
    current_row = 0 

    def print_menu(stdscr, selected_row): 
        stdscr.clear() 
        # h, w = stdscr.getmaxyx() 
        
        for idx, row in enumerate(items): 
            x = 1
            y = 1 + idx
            # center menu:
            # x = w // 2 - len(row) // 2 
            # y = h // 2 - len(items) // 2 + idx 
            
            if idx == selected_row: 
                stdscr.attron(curses.color_pair(1)) 
                stdscr.addstr(y, x, row) 
                stdscr.attroff(curses.color_pair(1)) 
            
            else: 
                stdscr.addstr(y, x, row) 
        
        stdscr.refresh() 
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE) 

    print_menu(stdscr, current_row)
        
    while True: 
        key = stdscr.getch() 
        
        if key == curses.KEY_UP and current_row > 0: 
            current_row -= 1 
        
        elif key == curses.KEY_DOWN and current_row < len(items) - 1: 
            current_row += 1 
        
        elif key == ord('\n'): 
            stdscr.addstr(0, 0, f"You selected '{items[current_row]}'") 
            stdscr.refresh() 
            stdscr.getch() 
            break 
        
        print_menu(stdscr, current_row)
    
    
os.system('cls')

# Sätt språkinställning till svenska (Sverige) används för att skriva ut formaterad valuta
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')
curses.wrapper(main)