import json 

import readchar
from colored import fg, bg, attr

from user import User
from lists import occurrence_options, basic_options, home_expense_options
from lists import food_expense_options, transport_expense_options, other_expense_options

COLOR_GREEN = fg('green')
COLOR_RED = fg('red')
COLOR_BLUE = fg('blue')
RESET_COLOR = attr('reset')
COLOR_YELLOW = fg('yellow')

saved_users = [] 
filename = "users.json"   


def display_menu(options, title="menu"):
    current_selection = 0

    while True:
        print("\033[H\033[J", end="")

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


def load_users(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return {name: (info if isinstance(info, dict) else {}) for name, info in data.items()}
    except FileNotFoundError:
        print("Welcome to the Expense Tracker!")
        return {}
    

users_data = load_users(filename)


def save_users(users, filename):
    with open(filename, "w") as file:
        json.dump(users, file, indent=4)


def user_selection_menu(saved_users):
    user_names = [user.name for user in saved_users]
    user_menu_options = user_names + ["New User"]
    selected_option = display_menu(user_menu_options, "Select User")
    return selected_option


def switch_user(saved_users):
    user_names = [user.name for user in saved_users] + ["Main Menu"]
    selected_option = display_menu(user_names, f"{COLOR_YELLOW}Select User{RESET_COLOR}")
    return selected_option


def new_user_creation():
    create_new_user = display_menu(basic_options, f"{COLOR_YELLOW}Would you like to create a new user?{RESET_COLOR}")
    if create_new_user == 0:
        while True:
            user_name = input("Please enter a name (press 'q' to return): ")
            if user_name.lower() == 'q':
                return None
            elif user_name.strip():
                new_user = User(user_name)
                return new_user
            else:
                print(f"{COLOR_RED}Name field cannot be empty, please enter a name.{RESET_COLOR}")
    else:
        return None


def save_user_data(users_data, user, filename):
    users_data[user.name] = user.to_dict()
    with open(filename, 'w') as file:
        json.dump(users_data, file, indent=4)


def generate_income_info(income_data):
    income_info = ""
    for income_type, details in income_data.items():
        amount = int(details['amount'])
        occurrence = details['occurrence']
        if income_type == "Total Expenses":
            color = COLOR_RED
        elif amount > 0:
            color = COLOR_GREEN
        elif amount == 0:
            color = COLOR_BLUE
        else:
            color = COLOR_RED
        income_info += f"{income_type}: {color}${amount}{RESET_COLOR} ({occurrence})\n "
    return income_info


def generate_expense_info(category_data):
    expense_info = ""
    for expense_type, details in category_data.items():
        amount = int(details['amount'])
        occurrence = details['occurrence']
        if amount == 0:
            color = COLOR_BLUE
        else:
            color = COLOR_RED
        expense_info += f"{expense_type}: {color}${amount}{RESET_COLOR} ({occurrence})\n     "
    return expense_info.rstrip()


def add_income(user, income_type):
    occurrence = display_menu(occurrence_options, "How often do you receive this income source?")

    if occurrence_options[occurrence] == "Previous Section":
        return
    
    while True:
        income_value_input = input("Enter the value of the income (press q to return): ")
        if income_value_input.lower() == 'q':
            return
        try:
            income_value = float(income_value_input)
            income_info = {
                "amount": income_value,
                "occurrence": occurrence_options[occurrence]
            }

            if income_type == 'primary':
                user.primary_income = income_info
            else: 
                user.supplementary_income = income_info
            save_user_data(users_data, user, filename)
            break
        except ValueError:
            print(f"{COLOR_RED}Invalid input, please use only numbers.{RESET_COLOR}")
    

def add_expenses(user, expense_category):
    while True:
        match expense_category:
            case "home":
                options = home_expense_options
            case "food":
                options = food_expense_options
            case "transport":
                options = transport_expense_options
            case "other":
                options = other_expense_options

        option = display_menu(options, f"{COLOR_YELLOW}Select an expense:{RESET_COLOR}")        
        if option == len(options) - 1:
            break
        
        expense_name = options[option]

        occurrence = display_menu(occurrence_options, "How frequent is this expense?")
        if occurrence_options[occurrence] == "Previous Section":
            return
        
        while True:
            expense_value_input = input("Enter the value of the expense (press 'q' to return): ")
            if expense_value_input.lower() == 'q':
                return
            try:
                expense_value = float(expense_value_input)
                user.expense[expense_category][expense_name] = {
                    "amount": expense_value,
                    "occurrence": occurrence_options[occurrence]
                }
                save_user_data(users_data, user, filename)
                break
            except ValueError:
                print(f"{COLOR_RED}Invalid input, please use only numbers.{RESET_COLOR}")
            

def calculate_finance(user, time_frame):
    conversion = {
        "Weekly": {"Weekly": 1, "Fortnightly": 0.5, "Monthly": 12 / 52},
        "Fortnightly": {"Weekly": 2, "Fortnightly": 1, "Monthly": 12 / 26},
        "Monthly": {"Weekly": 52 / 12, "Fortnightly": 26 / 12, "Monthly": 1}
    }
    total_income = 0
    total_expense = 0

    for income in [user.primary_income, user.supplementary_income]:
        if income['amount'] > 0:
            total_income += income['amount'] * conversion[time_frame][income['occurrence']]
    
    for category, expenses in user.expense.items():
        for expense in expenses.values():
            if expense['amount'] > 0:
                total_expense += expense['amount'] * conversion[time_frame][expense['occurrence']]
    
    remaining_funds = total_income - total_expense

    user.total_income = {"amount": total_income, "occurrence": time_frame}
    user.total_expense = {"amount": total_expense, "occurrence": time_frame}
    user.remaining_funds = {"amount": remaining_funds, "occurrence": time_frame}

    return total_income, total_expense, remaining_funds
    

def delete_user(current_user, saved_users, users_data, filename):
    user_names = [user.name for user in saved_users] + ["Main Menu"]
    selected_option = display_menu(user_names, f"{COLOR_YELLOW}Select a user to delete{RESET_COLOR}")
    
    if selected_option == len(saved_users):
        return current_user
    user_to_delete = saved_users[selected_option]

    confirmation = display_menu(basic_options, f"{COLOR_RED}Deleting {user_to_delete.name} will remove all of their stored data. Are you sure you want to continue?{RESET_COLOR}")
    if confirmation == 0:
        saved_users.pop(selected_option)
        users_data.pop(user_to_delete.name)

        save_users(users_data, filename)
        print(f"User {user_to_delete.name} has been deleted.")

        if user_to_delete != current_user:
            input("Press any key to return to the main menu.")
            return current_user
        else:
            if not saved_users:
                user_name = input("Please enter a name: ")
                new_user = User(user_name)
                saved_users.append(new_user)
                users_data[user_name] = new_user.to_dict()
                save_users(users_data, filename)
                return new_user
            else:
                selected_user_index = user_selection_menu(saved_users)
                return saved_users[selected_user_index]
    else:
        return current_user
    