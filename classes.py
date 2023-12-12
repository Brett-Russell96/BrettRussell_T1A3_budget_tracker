class PrimaryIncome:
    def __init__(self, amount=0, occurence=""):
        self.amount = amount
        self.occurencee = occurence

    def to_dict(self):
        return {"amount": self.amount, "occurence": self.occurence}
    
    