




# Expense Tracker

Thankyou for taking the time to look at the terminal application submission for T1A3, my Expense Tracker.

### Source control repository

https://github.com/Brett-Russell96/BrettRussell_T1A3_expense_tracker

### Styling guidellines

For this application I have made my best effort to adhere to the Python PEP 8 styling guidelines this is evident in the following:

* Indentation
* Maximum Line Length
* Imports
* Whitespace in Expressions and Statements
* Commenting
* Naming Conventions
* Code Layout
* Error Handling
* Use of Compound Statements
* Parentheses

## Features

This application contains a variety of different features including:

#### display_menu

A function which makes use of the readchar package, as well as a while True loop and multiple local variables. These are usded to create a menu display where users may use arrow keys and the enter key in order to make a selection.  
This function is used commonly in the app.

#### File Handling Systems

This application uses multiple functions in order to create an external file, take user input, and use that input to add, adjust and remove data from that file. This is done with functions such as:
* load_users
* save_users
* new_user_creation
* save_user_data
* delete_user
These function all make use of various conditional statements and loops designed to create an external JSON file to house user profile data, allow for new data to be stored and saved in that file and to delete stored data which is no longer necessary. As well as local variables and loops, these functions also make use of the following global variables:
* saved_users
* filename
* users_data
All of these functions and variables are imported to and regularly used in the apps main logic.

#### Income Data Systems 
These functions come into two categories; those that are used to store data, and those that are used to display data. 

**add_income** and **add_expenses** are used to store data, they do this by taking a user selection which assigns a value to a predetermined variable, for instance add_income uses the income_type variable, the value of this variable determines which dictionary the input data will be stored in. They also use the variable 'occurrence' the value of this will affect dictionary data as well as the way it is calculated later. After assigning a value to 'occurrence', the next step is to implement a while True loop to assess the users input value as it must be numerical. Once this condition is met, the input data and occurrence value are both assigned into key/value pairs and stored in the users external profile dictionary.

**generate_income_info** and **generate_expense_info**


