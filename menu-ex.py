import curses 

def main(stdscr): 
    curses.curs_set(0)
    
    items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"] 
    current_row = 0 

    def print_menu(stdscr, selected_row): 
        stdscr.clear() 
        h, w = stdscr.getmaxyx() 
        
        for idx, row in enumerate(items): 
            x = w // 2 - len(row) // 2 
            y = h // 2 - len(items) // 2 + idx 
            
            if idx == selected_row: 
                stdscr.attron(curses.color_pair(1)) 
                stdscr.addstr(y, x, row) 
                stdscr.attroff(curses.color_pair(1)) 
            
            else: 
                stdscr.addstr(y, x, row) 
        
        stdscr.refresh() 
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) 

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
    
curses.wrapper(main)