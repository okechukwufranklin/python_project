import unittest
from unittest import TestCase
from BankApp.Bank import Bank


class MyTestCase(unittest.TestCase):
    def test_that_costumer_can_be_registered(self):
        frankBank = Bank("Frank")
        # frankBank.generate_account_number(self)
        frankBank.register_customer("franklin", "okechukwu", "1234")
        self.assertEqual(1, frankBank.check_number_of_accounts())  # add assertion here
    def test_that_costumer_can_Deposit_and_checkBalance(self):
        frankBank = Bank("Frank")
        # frankBank.generate_account_number(self)
        frankBank.register_customer("franklin", "okechukwu", "1234")
        self.assertEqual(1, frankBank.check_number_of_accounts())
        # accountNumber = frankBank.generate_account_number()
        # frankBank.deposit(1000,accountNumber)
        # self.assertEqual(1000,frankBank.check_balance("1234",accountNumber))




if __name__ == '__main__':
    unittest.main()

