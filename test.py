import pytest
from unittest.mock import patch

from functions import delete_user, calculate_finance
from user import User


# Test is for delete_user function
@patch('functions.display_menu', side_effect=[0, 0, 1])
@patch('functions.user_selection_menu', return_value=0)
@patch('functions.save_users')
@patch('builtins.input', return_value="new_user")
def test_delete_user(
    mock_input,
    mock_save_users,
    mock_user_selection_menu,
    mock_display_menu
):
    current_user = User("user1")
    second_user = User("user2")
    users = [current_user, second_user]
    users_data = {
        "user1": {
            "name": "user1"
        },
        "user2": {
            "name": "user2"
        }
    }
    updated_current_user = delete_user(
        current_user,
        users,
        users_data,
        'dummy_path.json'
    )
# Tests to see if user1 has been deleted
# ensures user1 is no longer in users list
    assert "user1" not in users_data
    assert all(user.name != "user1" for user in users)
# Tests fnction behaviour nased on remaining users
    if len(users) == 1:
        # Checks if the choice is offered between second_user and
        # creating a new user when only one user remains after deletion
        assert updated_current_user in [second_user, User("new_user")]
    elif not users:
        # Checks to see if a new user is created when none remain
        assert updated_current_user.name == "new_user"


# Test for calculate_finance function
# This function sets up the user data for test
def setup_user():
    user = User("TestUser")
    user.primary_income = {"amount": 1000, "occurrence": "Monthly"}
    user.supplementary_income = {"amount": 500, "occurrence": "Fortnightly"}
    user.expense = {
        "home": {"Rent": {"amount": 600, "occurrence": "Monthly"}},
        "food": {"Groceries": {"amount": 300, "occurrence": "Weekly"}}
    }
    return user


# First test covers monthy calculation
def test_calculate_finance():
    user = setup_user()
    total_income, total_expense, remaining_funds = calculate_finance(
                                                        user,
                                                        "Monthly"
                                                    )

    expected_income = 1000 + (500 * (26 / 12))
    expected_expense = 600 + (300 * (52 / 12))
    expected_remaining = expected_income - expected_expense

    # tests total_income calculation vs expected result
    assert total_income == expected_income
    # tests total_expense calculation vs expected result
    assert total_expense == expected_expense
    # tests remaining_funds calculation vs expected result
    assert remaining_funds == expected_remaining


def test_calculate_finance_fortnightly_case():
    user = setup_user()
    total_income, total_expense, remaining_funds = calculate_finance(
                                                        user,
                                                        "Fortnightly"
                                                    )

    expected_income = (1000 * (12 / 26)) + 500
    expected_expense = (600 * (12 / 26)) + (300 * 2)
    expected_remaining = expected_income - expected_expense

    # tests total_income calculation vs expected result
    assert total_income == expected_income
    # tests total_expense calculation vs expected result
    assert total_expense == expected_expense
    # tests remaining_funds calculation vs expected result
    assert remaining_funds == expected_remaining


if __name__ == "__main__":
    pytest.main()
