class User:
    def __init__(self, name):
        self.name = name
        self.primary_income = {"amount": 0.0, "occurrence": ""}
        self.supplementary_income = {"amount": 0.0, "occurrence": ""}
        self.costs = {
            "home": {
                "rent": {"amount": 0.0, "occurrence": ""},
                "mortgage": {"amount": 0.0, "occurrence": ""},
                "power": {"amount": 0.0, "occurrence": ""},
                "gas": {"amount": 0.0, "occurrence": ""},
                "water": {"amount": 0.0, "occurrence": ""},
                "internet": {"amount": 0.0, "occurrence": ""},
                "phone": {"amount": 0.0, "occurrence": ""}
            },
            "food": {
                "groceries": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "fast_food": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "eating_out": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""}
            },
            "transport": {
                "fuel": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "parking": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "public_transport": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "ride_sharing": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""}
            },
            "other": {
                "streaming_services": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "gym_membership": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
                "subscriptions": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""}
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



class Cost:
    def __init__(self, amount = 0, goal_amount = 0, occurrence = ""):
        self.amount = amount
        self.occurrence = occurrence
        self.goal_amount = goal_amount
    
    def to_dict(self):
        return{"amount": self.amount, "goal amount": self.goal_amount, "occurrence": self.occurrence}
rent = Cost(0, 0, "")

mortgage = Cost(0, 0, "")

power = Cost(0, 0, "")

gas = Cost(0, 0, "")

water = Cost(0, 0, "")

internet = Cost(0, 0, "")

phone = Cost(0, 0, "")
   
groceries = Cost(0, 0, "")

fast_food = Cost(0, 0, "")

eating_out = Cost(0, 0, "")

fuel = Cost(0, 0, "")

parking = Cost(0, 0, "")

public_transport = Cost(0, 0, "")

ride_sharing = Cost(0, 0, "")

streaming_services = Cost(0, 0, "")

gym_membership = Cost(0, 0, "")

subscriptions = Cost(0, 0, "")





