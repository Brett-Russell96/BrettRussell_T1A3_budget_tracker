class User:
    def __init__(self, name):
        self.name = name
        self.primary_income = {"amount": 0.0, "occurrence": ""}
        self.supplementary_income = {"amount": 0.0, "occurrence": ""}
        self.fixed_costs = {
            "rent": {"amount": 0.0, "occurrence": ""},
            "mortgage": {"amount": 0.0, "occurrence": ""},
            "power": {"amount": 0.0, "occurrence": ""},
            "gas": {"amount": 0.0, "occurrence": ""},
            "water": {"amount": 0.0, "occurrence": ""},
            "internet": {"amount": 0.0, "occurrence": ""},
            "phone": {"amount": 0.0, "occurrence": ""}
        }
        self.flexible_costs = {
            "groceries": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
            "fast_food": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
            "eating_out": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
            "fuel": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
            "parking": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
            "public_transport": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
            "ride_sharing": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
            "streaming_services": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
            "gym_membership": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
            "subscriptions": {"amount": 0.0, "goal_amount": 0.0, "occurrence": ""},
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



class FixedCost:
    def __init__(self, amount = 0, occurrence = ""):
        self.amount = amount
        self.occurrence = occurrence
    
    def to_dict(self):
        return{"amount": self.amount, "occurrence": self.occurrence}
    
rent = FixedCost(0, "")

mortgage = FixedCost(0, "")

power = FixedCost(0, "")

gas = FixedCost(0, "")

water = FixedCost(0, "")

internet = FixedCost(0, "")

phone = FixedCost(0, "")



class FlexibleCost:
    def __init__(self, amount = 0, goal_amount = 0, occurrence = ""):
        self.amount = amount
        self.occurrence = occurrence
        self.goal_amount = goal_amount
    
    def to_dict(self):
        return{"amount": self.amount, "goal amount": self.goal_amount, "occurrence": self.occurrence}
    
groceries = FlexibleCost(0, 0, "")

fast_food = FlexibleCost(0, 0, "")

eating_out = FlexibleCost(0, 0, "")

fuel = FlexibleCost(0, 0, "")

parking = FlexibleCost(0, 0, "")

public_transport = FlexibleCost(0, 0, "")

ride_sharing = FlexibleCost(0, 0, "")

streaming_services = FlexibleCost(0, 0, "")

gym_membership = FlexibleCost(0, 0, "")

subscriptions = FlexibleCost(0, 0, "")





