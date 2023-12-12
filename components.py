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
        super().__init__(amount, occurrence)
        self.goal_amount = goal_amount
    
    def to_dict(self):
        return{"amount": self.amount, "goal amount": self.goal_amount, "occurrence": self.occurrence}
    


