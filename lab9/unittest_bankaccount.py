"""
Nihar patel
lab 9, unit testing
Feb 26,2026
"""

import unittest
from bankaccount import *

class TestBankAccount(unittest.TestCase):

    # create default account before each test
    def setUp(self):
        self.account1 = BankAccount("Peter", 1000)

    # test initial balance
    def test_initial_balance(self):
        self.assertEqual(self.account1.get_balance(), 1000)

    # test deposit
    def test_deposit(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.get_balance(), 1500)

    # test withdraw
    def test_withdraw(self):
        self.account1.withdraw(300)
        self.assertEqual(self.account1.get_balance(), 700)

    # test withdraw more than balance
    def test_over_withdraw(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(2000)

    # test multiple transactions
    def test_multiple_transactions(self):
        self.account1.deposit(500)
        self.account1.withdraw(200)
        self.account1.deposit(100)
        self.account1.withdraw(50)
        self.assertEqual(self.account1.get_balance(), 1350)


if __name__ == "__main__":
    unittest.main()