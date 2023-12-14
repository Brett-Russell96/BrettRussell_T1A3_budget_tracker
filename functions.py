import json 
import components
import curses
import budget 

def add_income():
    def init_color_pairs():
        curses.start_color()
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    def print_income_menu(win, current_row):
        win.clear()

        title = "Add Income"
        win.attron(curses.color_pair(3))
        win.addstr(1, 5, title)
        win.attroff(curses.color_pair(3))

        menu = ["Add Primary Income", "Add Supplementary Income", "Main Menu"]
        for idx, row in enumerate(menu):
            x = 5
            y = 3 + idx * 2
            if idx == current_row:
                win.attron(curses.color_pair(2))
                win.addstr(y, x, row)
                win.attroff(curses.color_pair(2))
            else:
                win.addstr(y, x, row)
        win.refresh()

    def income_menu(stdscr):
        init_color_pairs()
        curses.curs_set(0)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        current_row = 0

        menu = ["Add Primary Income", "Add Supplementary Income", "Main Menu"]
        
        print_income_menu(stdscr, current_row)

        while True:
            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) -1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                break

            print_income_menu(stdscr, current_row)

        curses.endwin()
        return current_row
    
    menu_choice = ""

    while menu_choice != 2:
        main_choice = curses.wrapper(income_menu)
        match menu_choice:
            case 0:
                pass
            case 1:
                pass
            case 2:
                break
    
    


def add_expenses():
    pass


def calculate_average():
    pass


def create_budget():
    pass


def log_expense():
    pass


def new_user():
    pass


def switch_user():
    pass


def delete_user():
    pass

