from random import random

from BankApp.Account import Account

import random


class Bank:
    def __init__(self, name):
        self.accounts = []
        self.name = name

    def register_customer(self, first_name, last_name, pin):
        name = first_name + last_name
        account_number = self.generate_account_number()
        my_account = Account(name, 0, pin, account_number)
        self.accounts.append(my_account)
        return my_account

    def generate_account_number(self):
        return random.randint(10000000, 99999999)

    def check_number_of_accounts(self):
        return len(self.accounts)

    def deposit(self, amount, account_number):
        my_account = self.find_account(account_number)
        my_account.deposit(amount)

    def find_account(self, account_number):
        for account in self.accounts:
            if account_number == account.get_number():
                return account
        return None

    def check_balance(self, pin, account_number):
        account = self.find_account(account_number)
        return account.check_balance(pin)
