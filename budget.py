import curses
import json
import functions
from colored import fg, bg, attr
import readchar

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

def display_menu(options, title = "menu"):
    current_selection = 0

    while True:
        print("\033[H\033[J", end = "")

        print(title)
        for i, option in enumerate(options):
            prefix = "-> " if i == current_selection else "   "
            print(f"{prefix}{option}")

        key = readchar.readkey()

        if key == readchar.key.UP and current_selection > 0:
            current_selection -= 1
        elif key == readchar.key.DOWN and current_selection < len(options) - 1:
            current_selection += 1
        elif key == readchar.key.ENTER:
            break

    return current_selection

main_menu_options = [
    "Add Income",
    "Add Expenses",
    "Calculate Average",
    "Create a Budget",
    "New User",
    "Switch User",
    "Delete User",
    "Exit Application"
]

add_income_options = [
    "Add Primary Income",
    "Add Supplementary Income",
    "Main Menu"
]

add_expenses_options = [
    "Add Home Expense",
    "Add Food Expense",
    "Add Travel Expense",
    "Add Other Expense",
    "Main Menu"
]

calculate_average_options = [
    "Weekly",
    "Fortnightly",
    "Monthly",
    "Main Menu"
]

create_budget_options = [
    "Create a Budget",
    "See Savings Goal",
    "Main Menu"
]

new_user_options = [
    "Yes",
    "No"
]

switch_user_options = [
    "Yes",
    "No"
]

delete_user_options = [
    "Yes",
    "NO"
]


while True:
    selected_option = display_menu(main_menu_options, "Main Menu")
    print(f"You selected: {main_menu_options[selected_option]}")

    match selected_option:
        case 0:
            while True:
                selected_sub_option = display_menu(add_income_options, "Select a type of income:")
                if selected_sub_option == len(add_income_options) - 1:
                    break
        case 1:
            while True:
                selected_sub_option = display_menu(add_expenses_options, "Select a type of expense:")
                if selected_sub_option == len(add_expenses_options) - 1:
                    break
        case 2:
            while True:
                selected_sub_option = display_menu(calculate_average_options, "How would you like to calculate your finances?")
                if selected_sub_option == len(calculate_average_options) - 1:
                    break
        case 3:
            while True:
                selected_sub_option = display_menu(create_budget_options, "What would you like to do?")
                if selected_sub_option == len(create_budget_options) - 1:
                    break
        case 4:
            
        

        
        


    
        
    if selected_option == len(main_menu_options) -1:
        break


print("Thankyou for using Budget Tracker!")
