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
    match main_choice:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            continue
        case _:
            print("Invalid input, please select a number from 1-8.")



print("Thankyou for using Budget Tracker!")
