import curses
import json
from functions import add_income, display_menu
from components import User
from colored import fg, bg, attr
import readchar




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
    "Delete Income",
    "Main Menu"
]

add_expenses_options = [
    "Add Home Expense",
    "Add Food Expense",
    "Add Travel Expense",
    "Add Other Expense",
    "Delete Expense",
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


saved_users = [] 


filename = "users.json"

    
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


def user_selection_menu(saved_users):
    user_names = [user.name for user in saved_users]
    user_menu_options = user_names + ["New User"]
    selected_option = display_menu(user_menu_options, "Select User")
    return selected_option


def new_user_creation():
    create_new_user = display_menu(new_user_options, "Would you like to create a new user?")
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




users_data = load_users(filename)

print("Welcome to the Budget Tracker.")



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
    current_user = new_user
else:
    while True:
        selected_user_index = user_selection_menu(saved_users)

        if selected_user_index < len(saved_users):
            current_user = saved_users[selected_user_index]
            break
        else:
            new_user = new_user_creation()
            if new_user:
                saved_users.append(new_user)
                users_data[new_user.name] = new_user.to_dict()
                save_users(users_data, filename)
                current_user = new_user
                break



while True:
    selected_option = display_menu(main_menu_options, "Main Menu")

    match selected_option:
        case 0:
            while True:
                selected_sub_option = display_menu(add_income_options, "Select an option:")
                if selected_sub_option in [0, 1]:
                    income_type = 'primary' if selected_option == 0 else 'supplementary'
                    add_income(current_user, income_type)
                    save_user_data(users_data, current_user, filename)
                elif selected_sub_option == 2:
                    pass
                elif selected_sub_option == 3:
                    break
        case 1:
            while True:
                selected_sub_option = display_menu(add_expenses_options, "Select an option:")
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
            while True:
                selected_sub_option = display_menu(new_user_options, "Would you like to create a new user?")
                if selected_sub_option == len(new_user_options) - 1:
                    break
        case 5:
            while True:
                selected_sub_option = display_menu(switch_user_options, "Would you like to change to another user?")
                if selected_sub_option == len(switch_user_options) - 1:
                    break
        case 6:
            while True:
                selected_sub_option = display_menu(delete_user_options, "Would you like to delete this user?")
                if selected_sub_option == len(delete_user_options) - 1:
                    break

    if selected_option == len(main_menu_options) -1:
        break



print("Thankyou for using Budget Tracker!")
