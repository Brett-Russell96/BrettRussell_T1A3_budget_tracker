from colored import fg, attr

from functions import display_menu, save_users, switch_user
from functions import user_selection_menu, new_user_creation, save_user_data
from functions import add_income, add_expenses, generate_income_info
from functions import generate_expense_info, calculate_finance, delete_user
from functions import saved_users, users_data, filename
from user import User
from lists import main_menu_options, add_income_options
from lists import add_expenses_options, calculate_average_options


COLOR_YELLOW = fg('yellow')
COLOR_RED = fg('red')
COLOR_BLUE = fg('blue')
RESET_COLOR = attr('reset')


# retrieves user data when the program is run
for name, data in users_data.items():
    try:
        user = User(name)
        for key, value in data.items():
            setattr(user, key, value)
        saved_users.append(user)
    except Exception as e:
        print(
            f"{COLOR_RED}Error retrieving user data for "
            f"{name}: {e}{RESET_COLOR}"
        )

# handles creating a new user if none exists
if not saved_users:
    while True:
        try:
            user_name = input(
                f"{COLOR_YELLOW}Please enter a name:{RESET_COLOR} "
            ).strip()
            if not user_name:
                print(
                    f"{COLOR_RED}Name field cannot be empty, "
                    f"please enter a name.{RESET_COLOR}"
                )
            else:
                new_user = User(user_name)
                saved_users.append(new_user)
                users_data[user_name] = new_user.to_dict()
                save_users(users_data, filename)
                current_user = new_user
                break
        except Exception as e:
            print(
                f"{COLOR_RED}Error creating a new user: {e}{RESET_COLOR}"
            )

else:
    # handles user selection or creation if a user exists
    while True:
        try:
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
        except Exception as e:
            print(
                f"{COLOR_RED}Error encountered during user selection: "
                f"{e}{RESET_COLOR}"
            )

# main loop for program logic
while True:
    try:
        current_user_data = users_data[current_user.name]
    except KeyError:
        print(f"{COLOR_RED}Error: User data not found.{RESET_COLOR}")
        continue
    # variables for financial data displayed in program interface
    user_finance_info = generate_income_info({
        "Total Income": current_user_data['total_income'],
        "Total Expenses": current_user_data['total_expense'],
        "Remaining Funds": current_user_data['remaining_funds']
    })

    user_income_info = generate_income_info({
        'Primary Income': current_user_data['primary_income'],
        'Supplementary Income': current_user_data['supplementary_income']
    })

    home_expense_info = generate_expense_info(
        current_user_data['expense']['home']
        )
    food_expense_info = generate_expense_info(
        current_user_data['expense']['food']
        )
    transport_expense_info = generate_expense_info(
        current_user_data['expense']['transport']
        )
    other_expense_info = generate_expense_info(
        current_user_data['expense']['other']
        )

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
    # prompt for main menu
    main_prompt = (
        "{yellow}Expense Tracker{reset}\n"
        " Current User: {yellow}{user}{reset}\n"
        " {finance_info}\n"
        "{yellow}Main Menu{reset}"
    ).format(
        yellow=COLOR_YELLOW,
        reset=RESET_COLOR,
        user=current_user.name,
        finance_info=user_finance_info
    )

    try:
        # function call for main menu selection
        selected_option = display_menu(main_menu_options, main_prompt)
    except Exception as e:
        print(f"{COLOR_RED}An error occured: {e}{RESET_COLOR}")
        continue

    match selected_option:
        # match case for all selection options
        case 0:
            # add income section
            while True:
                add_income_prompt = (
                    "{yellow}Income Data:{reset} "
                    "{blue}(exit menu to refresh){reset}\n"
                    " {income_info}\n"
                    "{yellow}Select an option:{reset}"
                ).format(
                    income_info=user_income_info,
                    yellow=COLOR_YELLOW,
                    blue=COLOR_BLUE,
                    reset=RESET_COLOR
                )

                selected_sub_option = display_menu(
                    add_income_options,
                    add_income_prompt
                )
                if selected_sub_option in [0, 1]:
                    income_type = (
                        'primary' if selected_sub_option == 0
                        else 'supplementary'
                    )
                    # functions called for add income
                    add_income(current_user, income_type)
                    save_user_data(users_data, current_user, filename)
                else:
                    break

        case 1:
            while True:
                # add expenses section
                add_expenses_prompt = (
                    "{yellow}Expense Data:{reset} "
                    "{blue}(exit menu to refresh){reset}\n\n"
                    " {expense_info}\n\n"
                    "{yellow}Select an option:{reset}"
                ).format(
                    expense_info=user_expense_info,
                    yellow=COLOR_YELLOW,
                    blue=COLOR_BLUE,
                    reset=RESET_COLOR
                )
                selected_sub_option = display_menu(
                    add_expenses_options,
                    add_expenses_prompt
                )
                # match case to handle function call based on category
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
                # calculate finances section
                try:
                    calculate_finance_prompt = (
                        "{yellow}Current Financial Data:{reset} "
                        "{blue}(exit menu to refresh){reset}\n\n"
                        " {income_info}\n"
                        "{expense_info}\n\n"
                        "{yellow}How would you like to "
                        "calculate your finances?{reset}"
                    ).format(
                        income_info=user_income_info,
                        expense_info=user_expense_info,
                        yellow=COLOR_YELLOW,
                        blue=COLOR_BLUE,
                        reset=RESET_COLOR
                    )
                    selected_sub_option = display_menu(
                        calculate_average_options,
                        calculate_finance_prompt
                    )
                    if selected_sub_option == 3:
                        break
                    else:
                        # timeframe variable for conversion calculation
                        time_frame = calculate_average_options[
                            selected_sub_option
                        ]
                        # function call for finance calculation
                        total_income, total_expense, remaining_funds = (
                            calculate_finance(current_user, time_frame)
                        )
                        save_user_data(users_data, current_user, filename)
                        break
                except Exception as e:
                    print(f"{COLOR_RED}Calculation error: {e}{RESET_COLOR}")
                    continue

        case 3:
            try:
                # new user section
                new_user = new_user_creation()
                if new_user:
                    saved_users.append(new_user)
                    users_data[new_user.name] = new_user.to_dict()
                    save_users(users_data, filename)
                    current_user = new_user
            except Exception as e:
                print(f"{COLOR_RED}Error creating user: {e}{RESET_COLOR}")

        case 4:
            # switch user section
            selected_user_index = switch_user(saved_users)
            if selected_user_index < len(saved_users):
                current_user = saved_users[selected_user_index]
            else:
                continue

        case 5:
            # delete user section
            try:
                current_user = delete_user(
                    current_user,
                    saved_users,
                    users_data,
                    filename
                )
            except Exception as e:
                print(f"{COLOR_RED}Error deleting user: {e}{RESET_COLOR}")

    if selected_option == len(main_menu_options) - 1:
        break


print(f"{COLOR_YELLOW}Thankyou for using Expense Tracker!{RESET_COLOR}")
