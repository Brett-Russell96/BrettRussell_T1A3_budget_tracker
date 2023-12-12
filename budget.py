from colored import fg, attr, bg
import json




print("Welcome to the Budget Tracker.")



def main_menu():
    print("1. Add income")
    print("2. Add expenses")
    print("3. Calculate average")
    print("4. Create a budget")
    print("5. Log an expense")
    print("6. New user")
    print("7. Switch user")
    choice = input("Please select a number from the above menu: ")
    return choice

main_choice = ""

main_menu()
