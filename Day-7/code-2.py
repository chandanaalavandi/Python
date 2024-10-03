class BankAccount:
    def __init__(self,balance):
        self._balance = balance      #Private Variable

    def deposite(self,amount):
        self._balance += amount
    
    def get_balance(self):
        return self._balance
    
#creating an object
account = BankAccount (2000)
account.deposite(300)
print(account.get_balance())

#this code demonstrates object oriented programming concepts like:
#class,object,.......

