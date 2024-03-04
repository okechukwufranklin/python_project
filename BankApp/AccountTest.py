import unittest
from unittest import TestCase
from BankApp.Account import Account


class MyTestCase(unittest.TestCase):
    def test_ThatBalance_Can_Be_Checked(self):
        frankAccount = Account(0,"franklin","1234",1)
        self.assertEqual(0, frankAccount.CheckBalance("1234"))


    def test_money_can_be_deposited(self):
        frankAccount = Account(0, "franklin", "1234", 1)
        self.assertEqual(0, frankAccount.CheckBalance("1234"))
        frankAccount.deposit(1000)
        self.assertEqual(1000,frankAccount.CheckBalance("1234"))


    def test_money_can_be_deposited_and_withdraw(self):
        frankAccount = Account(0, "franklin", "1234", 1)
        self.assertEqual(0, frankAccount.CheckBalance("1234"))
        frankAccount.deposit(1000)
        self.assertEqual(1000,frankAccount.CheckBalance("1234"))
        frankAccount.withdraw(500,"1234")
        self.assertEqual(500,frankAccount.CheckBalance("1234"))

    def test_money_can_be_deposited_and_withdraw_and_again(self):
        frankAccount = Account(0, "franklin", "1234", 1)
        self.assertEqual(0, frankAccount.CheckBalance("1234"))
        frankAccount.deposit(1000)
        self.assertEqual(1000, frankAccount.CheckBalance("1234"))
        frankAccount.withdraw(500, "1234")
        self.assertEqual(500, frankAccount.CheckBalance("1234"))
        frankAccount.deposit(1000)
        self.assertEqual(1500,frankAccount.CheckBalance('1234'))
        frankAccount.withdraw(500,'1234')
        self.assertEqual(1000,frankAccount.CheckBalance('1234'))



    def test_negative_number(self):
        frankAccount = Account(0, "franklin", "1234", 1)
        self.assertEqual(0, frankAccount.CheckBalance("1234"))

        with self.assertRaises(ValueError):
            frankAccount.deposit(-1000)




