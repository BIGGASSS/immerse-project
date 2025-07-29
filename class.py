class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def getBalance(self):
        return self.balance
    def desposit(self, value):
        self.balance += value
    def withdraw(self, value):
        if value > self.balance:
            print("Not enough balance!")
        else:
            self.balance -= value

bankaccount = BankAccount(1000)
print(bankaccount.getBalance())
bankaccount.desposit(1000)
print(bankaccount.getBalance())
bankaccount.withdraw(1000)
print(bankaccount.getBalance())
