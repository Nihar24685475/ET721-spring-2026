"""
Nihar patel
lab 9, unit testing
Feb 26,2026
"""
import unittest
from employee import *

class TestEmployee(unittest.TestCase):
    #create a test template (instance of the class)
    def setUp(self):
        self.employee1 = Employee("Peter","Pan",80000)

    #test if email format is working properly
    def test_emailemployee(self):
        self.assertEqual(self.employee1.emailemployee, "Peter_Pan@email.org")
     
        # update information
        self.employee1.first = "Will"
        self.assertEqual(self.employee1.emailemployee, "Will_Pan@email.org")

    #test raise
    def test_apply_raise(self):
        self.assertEqual(self.employee1.salary, 80000)

        #increase salary
        self.employee1.apply_raise()

        self.assertEqual(self.employee1.salary,84000)

if __name__ == "__main__":
    unittest.main()