from colored import fg, attr, bg
import json
import components


print("Welcome to the Budget Tracker.")


class User:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return vars(self)
    
def load_users(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return {name: (info if isinstance(info, dict) else {}) for name, info in data.items()}
    except FileNotFoundError:
        print("Could not find user.")
        return {}
    
def save_users(users,filename):
    with open(filename, "w") as file:
        json.dump(users, file, indent=4)

filename = "users.json"
users_data = load_users(filename)

saved_users = [] 

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
else:
    pass


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
            print(f"{fg('red')}Invalid input{attr('reset')}, please select a number from 1-8.")



print("Thankyou for using Budget Tracker!")
