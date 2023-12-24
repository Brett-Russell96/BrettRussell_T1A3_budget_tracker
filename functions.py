import json

import readchar
from colored import fg, attr

from user import User
from lists import occurrence_options, basic_options, home_expense_options
from lists import food_expense_options, transport_expense_options
from lists import other_expense_options

COLOR_GREEN = fg('green')
COLOR_RED = fg('red')
COLOR_BLUE = fg('blue')
RESET_COLOR = attr('reset')
COLOR_YELLOW = fg('yellow')

saved_users = []
filename = "users.json"


# function allowing menu selection using keyboard inputs
def display_menu(options, title="menu"):
    current_selection = 0

    while True:
        # clears screen and resets cursor position
        print("\033[H\033[J", end="")

        print(title)
        # shows the current option based on index using -> as a marker
        for i, option in enumerate(options):
            prefix = "-> " if i == current_selection else "   "
            print(f"{prefix}{option}")

        try:
            key = readchar.readkey()
        except Exception as e:
            print(f"{COLOR_RED}Error reading key input: {e}{RESET_COLOR}")
            continue
        # sets keys used to make input decisions
        if key == readchar.key.UP and current_selection > 0:
            current_selection -= 1
        elif key == readchar.key.DOWN and current_selection < len(options) - 1:
            current_selection += 1
        elif key == readchar.key.ENTER:
            break

    return current_selection


# function for reading json file data an returning as a dictionary.
def load_users(filename):
    try:
        with open(filename, "r") as file:
            # reads json content to convert information to dictionary
            data = json.load(file)
            return {
                name: (info if isinstance(info, dict) else {})
                for name, info in data.items()
                }
    except FileNotFoundError:
        print(f"{COLOR_RED}File not found. Creating a new file.{RESET_COLOR}")
        return {}
    except json.JSONDecodeError:
        print(
            f"{COLOR_RED}Error reading the file. "
            f"Data may be corrupted.{RESET_COLOR}"
            )
        return {}


users_data = load_users(filename)


# saves data for a new user
def save_users(users, filename):
    try:
        with open(filename, "w") as file:
            json.dump(users, file, indent=4)
    except IOError as e:
        print(f"{COLOR_RED}Failed to save data: {e}{RESET_COLOR}")


def user_selection_menu(saved_users):
    user_names = [user.name for user in saved_users]
    user_menu_options = user_names + ["New User"]
    selected_option = display_menu(
        user_menu_options,
        f"{COLOR_YELLOW}Select User{RESET_COLOR}"
    )
    return selected_option


def switch_user(saved_users):
    user_names = [user.name for user in saved_users] + ["Main Menu"]
    selected_option = display_menu(
        user_names,
        f"{COLOR_YELLOW}Select User{RESET_COLOR}"
        )
    return selected_option


# function for creating users
def new_user_creation():
    create_new_user = display_menu(
        basic_options,
        f"{COLOR_YELLOW}Would you like to create a new user?{RESET_COLOR}"
        )
    if create_new_user == 0:
        while True:
            # takes input for username
            user_name = input(
                f"{COLOR_YELLOW}Please enter a name{RESET_COLOR} "
                f"{COLOR_BLUE}(press 'q' to return):{RESET_COLOR} "
            )
            if user_name.lower() == 'q':
                return None
            # checks to ensure user input isnt empty or a duplicate
            elif not user_name.strip():
                print(
                    f"{COLOR_RED}Name field cannot be empty, "
                    f"please enter a name.{RESET_COLOR}"
                    )
            elif any(user.name == user_name for user in saved_users):
                print(
                    f"{COLOR_RED}This username already exists. "
                    f"Please choose a different name.{RESET_COLOR}"
                    )
                # creates new user object
            else:
                new_user = User(user_name)
                return new_user
    else:
        return None


# saves new data and converts into user JSON dictionary
def save_user_data(users_data, user, filename):
    users_data[user.name] = user.to_dict()
    try:
        with open(filename, 'w') as file:
            json.dump(users_data, file, indent=4)
    except IOError as e:
        print(
            f"{COLOR_RED}Failed to save user data: "
            f"{e}{RESET_COLOR}"
        )
    except json.JSONDecodeError as e:
        print(
            f"{COLOR_RED}Failed to format user data as JSON: "
            f"{e}{RESET_COLOR}"
        )
    except Exception as e:
        print(
            f"{COLOR_RED}An unexpected error occurred: "
            f"{e}{RESET_COLOR}"
        )


# sets the interface display parameters for income data
def generate_income_info(income_data):
    income_info = ""
    for income_type, details in income_data.items():
        amount = int(details['amount'])
        occurrence = details['occurrence']
        if income_type == "Total Expenses":
            color = COLOR_RED if amount != 0 else COLOR_BLUE
        elif amount > 0:
            color = COLOR_GREEN
        elif amount == 0:
            color = COLOR_BLUE
        else:
            color = COLOR_RED
        income_info += (
            f"{income_type}: {color}${amount}{RESET_COLOR} "
            f"({occurrence})\n "
            )
    return income_info


# sets the interface display parameters for expense data
def generate_expense_info(category_data):
    expense_info = ""
    for expense_type, details in category_data.items():
        amount = int(details['amount'])
        occurrence = details['occurrence']
        if amount == 0:
            color = COLOR_BLUE
        else:
            color = COLOR_RED
        expense_info += (
            f"{expense_type}: {color}${amount}{RESET_COLOR} "
            f"({occurrence})\n     "
        )
    return expense_info.rstrip()


# function for taking user input to store income data
def add_income(user, income_type):
    occurrence = display_menu(
        occurrence_options,
        f"{COLOR_YELLOW}How often do you receive this income source?"
        f"{RESET_COLOR}")

    if occurrence_options[occurrence] == "Previous Section":
        return

    while True:
        # takes numerical input and converts to float data
        income_value_input = input(
            f"{COLOR_YELLOW}Enter the value of the income{RESET_COLOR} "
            f"{COLOR_BLUE}(press q to return):{RESET_COLOR} "
        )
        if income_value_input.lower() == 'q':
            return
        try:
            income_value = float(income_value_input)
            # sets how data is catagorised for storage
            income_info = {
                "amount": income_value,
                "occurrence": occurrence_options[occurrence]
            }
            # organises type of income data to be stored
            if income_type == 'primary':
                user.primary_income = income_info
            else:
                user.supplementary_income = income_info
            save_user_data(users_data, user, filename)
            break
        except ValueError:
            print(
                f"{COLOR_RED}Invalid input,"
                f"please use only numbers.{RESET_COLOR}"
                )


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

        option = display_menu(
            options,
            f"{COLOR_YELLOW}Select an expense:{RESET_COLOR}")
        if option == len(options) - 1:
            break

        expense_name = options[option]
        # sets occurrence value for later calculation
        occurrence = display_menu(
            occurrence_options,
            f"{COLOR_YELLOW}How frequent is this expense?{RESET_COLOR}")
        if occurrence_options[occurrence] == "Previous Section":
            return
        # takes input for expense data
        while True:
            expense_value_input = input(
                f"{COLOR_YELLOW}Enter the value of the expense{RESET_COLOR} "
                f"{COLOR_BLUE}(press 'q' to return):{RESET_COLOR} "
                )
            if expense_value_input.lower() == 'q':
                return
            try:
                # converts data type then stores new data
                expense_value = float(expense_value_input)
                user.expense[expense_category][expense_name] = {
                    "amount": expense_value,
                    "occurrence": occurrence_options[occurrence]
                }
                save_user_data(users_data, user, filename)
                break
            except ValueError:
                print(
                    f"{COLOR_RED}Invalid input,"
                    f"please use only numbers.{RESET_COLOR}"
                    )


def calculate_finance(user, time_frame):
    try:
        # values for conversion calculation
        conversion = {
            "Weekly": {
                "Weekly": 1,
                "Fortnightly": 0.5,
                "Monthly": 12 / 52
            },
            "Fortnightly": {
                "Weekly": 2,
                "Fortnightly": 1,
                "Monthly": 12 / 26
            },
            "Monthly": {
                "Weekly": 52 / 12,
                "Fortnightly": 26 / 12,
                "Monthly": 1
            }
        }
        total_income = 0
        total_expense = 0
        # accesses user income data
        for income in [user.primary_income, user.supplementary_income]:
            if income['amount'] > 0:
                # type of conversion which is performed
                income_calc = (
                    conversion[time_frame][income['occurrence']]
                )
                # amount being converted
                income_contribution = (
                    income['amount'] * income_calc
                )
                # sum of all converted amounts
                total_income += income_contribution
        # loop for accessing all expenses stored
        for category, expenses in user.expense.items():
            for expense in expenses.values():
                if expense['amount'] > 0:
                    expense_calc = (
                        conversion[time_frame][expense['occurrence']]
                    )
                    expense_contribution = (
                        expense['amount'] * expense_calc
                    )
                    total_expense += expense_contribution
        # basic calculation for remaining funds
        remaining_funds = total_income - total_expense
        # dictionary storage device for new data
        user.total_income = {
            "amount": total_income,
            "occurrence": time_frame}
        user.total_expense = {
            "amount": total_expense,
            "occurrence": time_frame
            }
        user.remaining_funds = {
            "amount": remaining_funds,
            "occurrence": time_frame
            }

        return total_income, total_expense, remaining_funds

    except KeyError as e:
        print(
            f"{COLOR_RED}Invalid time frame or occurrence: "
            f"{e}{RESET_COLOR}"
        )
    except TypeError as e:
        print(
            f"{COLOR_RED}Invalid data type in financial information: "
            f"{e}{RESET_COLOR}"
        )
    except Exception as e:
        print(
            f"{COLOR_RED}An unexpected error occured in finance calculation: "
            f"{e}{RESET_COLOR}"
        )


# function for deleting users as well as their dictionary data from json
def delete_user(current_user, saved_users, users_data, filename):
    user_names = [user.name for user in saved_users] + ["Main Menu"]
    selected_option = display_menu(
        user_names,
        f"{COLOR_YELLOW}Select a user to delete{RESET_COLOR}"
        )

    if selected_option == len(saved_users):
        return current_user
    user_to_delete = saved_users[selected_option]
    # warning prompt before deletion
    confirmation = display_menu(
        basic_options,
        f"{COLOR_RED}Deleting {user_to_delete.name} will remove all of "
        f"their stored data. Are you sure you want to continue?{RESET_COLOR}"
        )
    if confirmation == 0:
        try:
            # deletes user data
            saved_users.pop(selected_option)
            users_data.pop(user_to_delete.name)

            save_users(users_data, filename)
            print(f"User {user_to_delete.name} has been deleted.")
            # handles scenarios for after user deletion
            if user_to_delete != current_user:
                input("Press any key to return to the main menu.")
                return current_user
            else:
                # scenario for the last user being deleted
                if not saved_users:
                    user_name = input("Please enter a name: ")
                    if not user_name.strip():
                        print(
                            f"{COLOR_RED}Name field cannot be empty,"
                            f"please enter a name.{RESET_COLOR}"
                        )
                    else:
                        new_user = User(user_name)
                        saved_users.append(new_user)
                        users_data[user_name] = new_user.to_dict()
                        save_users(users_data, filename)
                        return new_user
                else:
                    # selection menu for if current user is deleted
                    selected_user_index = user_selection_menu(saved_users)
                    return saved_users[selected_user_index]
        except Exception as e:
            print(f"{COLOR_RED}Error while deleting user: {e}{RESET_COLOR}")
    else:
        return current_user
