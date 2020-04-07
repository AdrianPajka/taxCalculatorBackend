class Calculator:
    def __init__(self, obj):
        self.amount = float(obj["value"])
        self._lower_tax_percent = 0.1775
        self._higher_tax_percent = 0.32

    def tax_reducing_amount(self):
        if self.amount <= 8000:
            return 1420
        elif self.amount >= 8001 and self.amount<= 13000:
            return 1420 - (871.70*(self.amount-8000)/5000)
        elif self.amount >= 13001 and self.amount<= 85528:
            return 548.30
        elif self.amount >= 85529 and self.amount<= 127000:
            return 548.30 - (548.30*(self.amount-85528)/41472)
        else:
            return 0

    @property
    def calculate_tax(self):
        if self.amount<= 85528:
            tax = self._lower_tax_percent * self.amount - self.tax_reducing_amount()
            return 0 if tax <= 0 else round(tax,2)
        elif self.amount > 85.528 and self.amount <= 1000000:
            downgradeAmount = self.amount-85528
            return round(15181.22 + self._higher_tax_percent*downgradeAmount-self.tax_reducing_amount(),2)
        else:
            downgradeAmount = self.amount - 85528
            return round(15181.22 + self._higher_tax_percent * downgradeAmount - self.tax_reducing_amount()+ 0.04*(self.amount - 85528), 2)

