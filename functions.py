import json 
from components import Income, primary_income, supplementary_income
from budget import display_menu, occurrence_options

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

