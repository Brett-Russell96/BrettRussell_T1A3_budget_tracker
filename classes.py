class User:
    def __init__(self, name):
        self.name = name
        self.total_income = {"amount": 0.0, "occurrence": ""}
        self.total_expense = {"amount": 0.0, "occurrence": ""}
        self.remaining_funds = {"amount": 0.0, "occurrence": ""}
        self.primary_income = {"amount": 0.0, "occurrence": ""}
        self.supplementary_income = {"amount": 0.0, "occurrence": ""}
        self.expense = {
            "home": {
                "Rent": {"amount": 0.0, "occurrence": ""},
                "Mortgage": {"amount": 0.0, "occurrence": ""},
                "Power": {"amount": 0.0, "occurrence": ""},
                "Gas": {"amount": 0.0, "occurrence": ""},
                "Water": {"amount": 0.0, "occurrence": ""},
                "Internet": {"amount": 0.0, "occurrence": ""},
                "Phone": {"amount": 0.0, "occurrence": ""}
            },
            "food": {
                "Groceries": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "Fast Food": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "Eating Out": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""}
            },
            "transport": {
                "Fuel": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "Parking": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "Public Transport": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "Ride Share": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""}
            },
            "other": {
                "Streaming Services": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "Gym Membership": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "Subscriptions": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""}
            }
        }

    def to_dict(self):
        return vars(self)



class Income:
    def __init__(self, amount = 0, occurrence = ""):
        self.amount = amount
        self.occurrence = occurrence
    

    def to_dict(self):
        return {"amount": self.amount, "occurrence": self.occurrence}
    
primary_income = Income(0, "")

supplementary_income = Income(0, "")



class Expense:
    def __init__(self, amount = 0, goal_amount = 0, occurrence = ""):
        self.amount = amount
        self.occurrence = occurrence
        self.goal_amount = goal_amount
    
    def to_dict(self):
        return{"amount": self.amount, "goal amount": self.goal_amount, "occurrence": self.occurrence}
rent = Expense(0, 0, "")

mortgage = Expense(0, 0, "")

power = Expense(0, 0, "")

gas = Expense(0, 0, "")

water = Expense(0, 0, "")

internet = Expense(0, 0, "")

phone = Expense(0, 0, "")
   
groceries = Expense(0, 0, "")

fast_food = Expense(0, 0, "")

eating_out = Expense(0, 0, "")

fuel = Expense(0, 0, "")

parking = Expense(0, 0, "")

public_transport = Expense(0, 0, "")

ride_sharing = Expense(0, 0, "")

streaming_services = Expense(0, 0, "")

gym_membership = Expense(0, 0, "")

subscriptions = Expense(0, 0, "")





