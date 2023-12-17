import json 
import readchar
from classes import Income, User, primary_income, supplementary_income
from lists import occurrence_options, basic_options, home_expense_options, food_expense_options, transport_expense_options, other_expense_options



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



def load_users(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return {name: (info if isinstance(info, dict) else {}) for name, info in data.items()}
    except FileNotFoundError:
        print("Welcome to the Budget Tracker!")
        return {}
    


def save_users(users,filename):
    with open(filename, "w") as file:
        json.dump(users, file, indent=4)



def user_selection_menu(saved_users):
    user_names = [user.name for user in saved_users]
    user_menu_options = user_names + ["New User"]
    selected_option = display_menu(user_menu_options, "Select User")
    return selected_option



def new_user_creation():
    create_new_user = display_menu(basic_options, "Would you like to create a new user?")
    if create_new_user == 0:
        user_name = input("Please enter a name: ")
        new_user = User(user_name)
        return new_user
    else:
        return None



def save_user_data(users_data, user, filename):
    users_data[user.name] = user.to_dict()
    with open(filename, 'w') as file:
        json.dump(users_data, file, indent=4)



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
            break
        except ValueError:
            print("Invalid input, please use only numbers.")
    
    income_info = {
        "amount": income_value,
        "occurrence": occurrence_options[occurrence]
    }

    if income_type == 'primary':
        user.primary_income = income_info
    else: 
        user.supplementary_income = income_info




def add_expenses(user, expense_catagory):
    while True:
        match expense_catagory:
            case 'home':
                option = display_menu(home_expense_options, "Select an expense:")
                if option == len(home_expense_options) - 1:
                    break
    
            case 'food':
                option = display_menu(food_expense_options, "Select an expense")
                if option == len(food_expense_options) - 1:
                    break

            case 'transport':
                option = display_menu(transport_expense_options, "Select an expense")
                if option == len(transport_expense_options) - 1:
                    break

            case 'other':
                option = display_menu(other_expense_options, "Select an expense")
                if option == len(other_expense_options) - 1:
                    break
                

            

def calculate_average():
    pass


def create_budget():
    pass


def new_user():
    pass


def switch_user():
    pass


def delete_user():
    pass

