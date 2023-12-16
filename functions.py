import json 
# from components import Income


def add_income(user, income_type):

    occurrence = input("How often do you recieve this income?(weekly/fortnightly/monthly)-> ")
    amount = float(input("Enter the amount of this income: "))

    income = income(amount, occurrence)

    if income_type == "primary":
        if not hasattr(user, 'primary_income'):
            user.primary_income = []
        user.primary_income.append(income.to_dict())
    elif income_type == "supplementary":
        if not hasattr(user, 'supplementary_income'):
            user.supplementary_income = []
        user.supplementary_income.append(income.to_dict())

    save_users({user.name: user.to_dict()}, 'users.json')

    return


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

