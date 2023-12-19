import json
from functions import display_menu, load_users, save_users, user_selection_menu, new_user_creation, save_user_data, add_income, add_expenses, generate_expense_info, generate_income_info, calculate_finance, saved_users, users_data, filename
from classes import User
from lists import main_menu_options, add_income_options, add_expenses_options, calculate_average_options, create_budget_options, basic_options
from colored import fg, bg, attr
import readchar




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
    current_user_data = users_data[current_user.name]

    user_finance_info = generate_income_info({
        "Total Income": current_user_data['total_income'],
        "Total Expenses": current_user_data['total_expense'],
        "Remaining Funds": current_user_data['remaining_funds']
    })

    user_income_info = generate_income_info({
        'Primary Income': current_user_data['primary_income'],
        'Supplementary Income': current_user_data['supplementary_income']
    })

    home_expense_info = generate_expense_info(current_user_data['expense']['home'])
    food_expense_info = generate_expense_info(current_user_data['expense']['food'])
    transport_expense_info = generate_expense_info(current_user_data['expense']['transport'])
    other_expense_info = generate_expense_info(current_user_data['expense']['other'])

    user_expense_info = f"Home Expenses:\n     {home_expense_info}\n Food Expenses:\n     {food_expense_info}\n Transport Expenses:\n     {transport_expense_info}\n Other Expenses:\n     {other_expense_info}"

    main_prompt = f"Budget Tracker\n {user_finance_info}\nMain Menu"

    selected_option = display_menu(main_menu_options, main_prompt)

    match selected_option:

        case 0:
             while True:
                add_income_prompt = f"Income Data: (exit menu to refresh)\n {user_income_info}\nSelect an option:"

                selected_sub_option = display_menu(add_income_options, add_income_prompt)
                if selected_sub_option in [0, 1]:
                    income_type = 'primary' if selected_sub_option == 0 else 'supplementary'
                    add_income(current_user, income_type)
                    save_user_data(users_data, current_user, filename)
                else: 
                    break

        case 1:
            while True:
                selected_sub_option = display_menu(add_expenses_options, "Select an option:")
                match selected_sub_option:
                    case 0:
                        add_expenses(current_user, "home")
                    case 1:
                        add_expenses(current_user, "food")                     
                    case 2:
                        add_expenses(current_user, "transport")                       
                    case 3:
                        add_expenses(current_user, "other")                        
                    case 4:
                        break
                    
        case 2:
            while True:
                calculate_average_prompt = f"Current Financial Data: (exit menu to refresh)\n\n {user_income_info}\n {user_expense_info}\n\nHow would you like to calculate your finances?"

                selected_sub_option = display_menu(calculate_average_options, calculate_average_prompt)
                if selected_sub_option == len(calculate_average_options) - 1:
                    break
                else:
                    time_frame = calculate_average_options[selected_sub_option]
                    total_income, total_expense, remaining_funds = calculate_finance(current_user, time_frame)
                    save_user_data(users_data, current_user, filename)
        case 3:
            while True:
                selected_sub_option = display_menu(create_budget_options, "What would you like to do?")
                if selected_sub_option == len(create_budget_options) - 1:
                    break
        case 4:
            while True:
                selected_sub_option = display_menu(basic_options, "Would you like to create a new user?")
                if selected_sub_option == len(basic_options) - 1:
                    break
        case 5:
            while True:
                selected_sub_option = display_menu(basic_options, "Would you like to change to another user?")
                if selected_sub_option == len(basic_options) - 1:
                    break
        case 6:
            while True:
                selected_sub_option = display_menu(basic_options, "Would you like to delete this user?")
                if selected_sub_option == len(basic_options) - 1:
                    break

    if selected_option == len(main_menu_options) -1:
        break



print("Thankyou for using Budget Tracker!")
