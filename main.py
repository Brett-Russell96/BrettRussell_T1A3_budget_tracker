from colored import fg, bg, attr

from functions import display_menu, save_users, switch_user
from functions import user_selection_menu, new_user_creation, save_user_data
from functions import add_income, add_expenses, generate_expense_info
from functions import generate_income_info, calculate_finance, delete_user
from functions import saved_users, users_data, filename
from user import User
from lists import main_menu_options, add_income_options, add_expenses_options, calculate_average_options


COLOR_YELLOW = fg('yellow')
COLOR_BLUE = fg('blue')
RESET_COLOR = attr('reset')





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

    user_expense_info = (
        "Home Expenses:\n     {home}\n"
        "Food Expenses:\n     {food}\n"
        "Transport Expenses:\n     {transport}\n"
        "Other Expenses:\n     {other}"
    ).format(
        home=home_expense_info,
        food=food_expense_info,
        transport=transport_expense_info,
        other=other_expense_info
    )

    main_prompt = (
        "{yellow}Expense Tracker{reset}\n"
        "Current User: {blue}{user}{reset}\n"
        "{finance_info}\n"
        "{yellow}Main Menu{reset}"
    ).format(
        yellow=COLOR_YELLOW, 
        reset=RESET_COLOR, 
        blue=COLOR_BLUE, 
        user=current_user.name, 
        finance_info=user_finance_info
    )

    selected_option = display_menu(main_menu_options, main_prompt)

    match selected_option:

        case 0:
             while True:
                add_income_prompt = f"Income Data: (exit menu to refresh)\n {user_income_info}\n{COLOR_YELLOW}Select an option:{RESET_COLOR}"

                selected_sub_option = display_menu(add_income_options, add_income_prompt)
                if selected_sub_option in [0, 1]:
                    income_type = 'primary' if selected_sub_option == 0 else 'supplementary'
                    add_income(current_user, income_type)
                    save_user_data(users_data, current_user, filename)
                else: 
                    break

        case 1:
            while True:
                selected_sub_option = display_menu(add_expenses_options, f"{COLOR_YELLOW}Select an option:{RESET_COLOR}")
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
                calculate_average_prompt = f"Current Financial Data: (exit menu to refresh)\n\n {user_income_info}\n {user_expense_info}\n\n{COLOR_YELLOW}How would you like to calculate your finances?{RESET_COLOR}"

                selected_sub_option = display_menu(calculate_average_options, calculate_average_prompt)
                if selected_sub_option == len(calculate_average_options) - 1:
                    break
                else:
                    time_frame = calculate_average_options[selected_sub_option]
                    total_income, total_expense, remaining_funds = calculate_finance(current_user, time_frame)
                    save_user_data(users_data, current_user, filename)
                    break
 
        case 3:
            new_user = new_user_creation()
            if new_user:
                saved_users.append(new_user)
                users_data[new_user.name] = new_user.to_dict()
                save_users(users_data, filename)
                current_user = new_user
             
        case 4:
            selected_user_index = switch_user(saved_users)
            if selected_user_index < len(saved_users):
                    current_user = saved_users[selected_user_index]
            else:
                continue
        case 5:
            current_user = delete_user(current_user, saved_users, users_data, filename)

    if selected_option == len(main_menu_options) -1:
        break



print(f"{COLOR_YELLOW}Thankyou for using Expense Tracker!{RESET_COLOR}")
