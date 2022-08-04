class CompoundInterest:
    def __init__(self, principal_amount, annual_rate, number_of_years):
        self.principal_amount = principal_amount
        self.annual_rate = annual_rate/100
        self.number_of_years = number_of_years
        self.n = 12
        
    def investment_return(self, monthly=False):
        if monthly:
            self.number_of_years = 1/12
            
        exponent = self.n * self.number_of_years
        parenthesis = 1 + (self.annual_rate/self.n)
        
        amount = self.principal_amount*parenthesis**exponent
        if monthly:
            return amount
        return round(amount, 2)
    
    def investment_return_w_monthly_contributions(self, amount_per_month):
        total_months = range(self.number_of_years*12)
        for _ in total_months:
            self.principal_amount += amount_per_month
            self.principal_amount = self.investment_return(monthly=True)    
            
        return round(self.principal_amount, 2)
        

