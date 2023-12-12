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
    print("8. Exit application")
    choice = input("Please select a number from the above menu: ")
    return choice


main_choice = ""

while main_choice != "8":
    main_choice = main_menu()
    if main_choice == "1":
        pass
    elif main_choice == "2":
        pass
    elif main_choice == "3":
        pass
    elif main_choice == "4":
        pass
    elif main_choice == "5":
        pass
    elif main_choice == "6":
        pass
    elif main_choice == "7":
        pass
    elif main_choice == "8":
        continue
    else:
        print("Invalid input, please select a number from 1-8.")



print("Thankyou for using Budget Tracker!")
