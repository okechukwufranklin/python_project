class Account:
    def __init__(self, balance, name, pin, number):
        self.balance = balance
        self.name = name
        self.pin = pin
        self.number = number

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def CheckBalance(self, pin):
        if self.pin != pin:
            raise ValueError
        return self.balance

    def deposit(self, amount):
        if amount < 1:
           raise ValueError
        self.balance += amount

    def withdraw(self,amount,pin):
        if self.pin != pin:
            raise ValueError
        if amount > self.balance:
            raise ValueError
        if amount < 1:
            raise ValueError
        self.balance -= amount

