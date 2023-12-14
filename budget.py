from colored import fg, attr, bg
import curses
import json



print("Welcome to the Budget Tracker.")


class User:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return vars(self)
    
def load_users(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return {name: (info if isinstance(info, dict) else {}) for name, info in data.items()}
    except FileNotFoundError:
        print("Could not find user.")
        return {}
    
def save_users(users,filename):
    with open(filename, "w") as file:
        json.dump(users, file, indent=4)

filename = "users.json"
users_data = load_users(filename)

saved_users = [] 

for name, data in users_data.items():
    user = User(name)
    for key, value in data.items():
        setattr(user, key, value)
    saved_users.append(user)

if not saved_users:
    user_name = input("Please enter a name: ")
    new_user = User(user_name)
    saved_users.append(new_user)
    users_data[user_name] = new_user.to_dict()
    save_users(users_data, filename)
else:
    pass

def init_color_pairs():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

def print_main_menu(win, current_row):
    win.clear()

    title = "Welcome to the Budget Tracker."
    win.attron(curses.color_pair(1))
    win.addstr(1, 5, title)
    win.attroff(curses.color_pair(1))

    menu = ["Add Income", "Add Expenses", "Calculate Average", "Create a Budget", "Log an Expense", "New User", "Switch User", "Delete User", "Exit Application"]
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

def main_menu(stdscr):
    init_color_pairs()
    curses.curs_set(0)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0

    menu = ["Add Income", "Add Expenses", "Calculate Average", "Create a Budget", "Log an Expense", "New User", "Switch User", "Delete User", "Exit Application"]

    print_main_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break

        print_main_menu(stdscr, current_row)
    
    curses.endwin()
    return current_row

main_choice = ""

while main_choice != 8:
    main_choice = curses.wrapper(main_menu)
    match main_choice:
        case 0:
            pass
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            break



print("Thankyou for using Budget Tracker!")
