import json 
import readchar
from components import Income, primary_income, supplementary_income
from lists import occurrence_options

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
        "occurrence": occurrence_options[occurrence],
        "value": income_value
    }
    if income_type == 'primary':
        user.primary_income = income_info
    else:
        if not hasattr(user, 'supplementary_income'):
            user.supplementary_income = []
        user.supplementary_income.append(income_info)
    pass

def add_expenses():
    pass


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

