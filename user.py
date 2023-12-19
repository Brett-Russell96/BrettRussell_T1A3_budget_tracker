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
                "Groceries": {"amount": 0.0, "occurrence": ""},
                "Fast Food": {"amount": 0.0, "occurrence": ""},
                "Eating Out": {"amount": 0.0, "occurrence": ""}
            },
            "transport": {
                "Fuel": {"amount": 0.0, "occurrence": ""},
                "Parking": {"amount": 0.0, "occurrence": ""},
                "Public Transport": {"amount": 0.0, "occurrence": ""},
                "Ride Share": {"amount": 0.0, "occurrence": ""}
            },
            "other": {
                "Streaming Services": {"amount": 0.0, "occurrence": ""},
                "Gym Membership": {"amount": 0.0, "occurrence": ""},
                "Subscriptions": {"amount": 0.0,"occurrence": ""}
            }
        }

    def to_dict(self):
        return vars(self)







