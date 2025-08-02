class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = account_balance
        initial_balance = 0
    def deposit(self,amount):
        amount += self.account_balance
    def withdraw(self,amount):
        if self.account_balance < amount:
            return False
        else:
            amount -= self.account_balance
            return True
        
    def display_balance(self):
        print(f"account balance is {self.account_balance:.2f}")



        
        
        
        