"""
Nihar patel
lab 9, unit testing
Feb 26,2026
"""

from calculation import *
import unittest

#example 1 : simple unit testing
#unit
def addtwonumber(a,b):
    return a+b

#unit test
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumber(1,2), 3) 
        # test that when pass 1 and 2, the return of the function is 3

        # #Example 2: unit testinf calculatin.py file
    def test_subtraction(self):
        self.assertEqual(subtracttwonumber(6,2), 4)
        self.assertEqual(subtracttwonumber(4,6), -2)
        self.assertEqual(subtracttwonumber(5), 5)
        self.assertEqual(subtracttwonumber(), 0)

    #unit test for multiplication function
    def test_multiplythreenumber(self):
        self.assertEqual(multiplythreenumber(1,2,3,), 6)
        self.assertEqual(multiplythreenumber(1,-2,3,), -6)
        self.assertEqual(multiplythreenumber(1,-2,-3,), 6)
        self.assertEqual(multiplythreenumber(-1,-2,-3,), -6)

    #unit test for division function
    def test_division(self):
        self.assertEqual(dividetwonumber(6,3), 2)
        self.assertAlmostEqual(dividetwonumber(10,3), 3.3333, places=4)

    #unit test for division by zero
    def test_divisionbyzero(self):
        # assetion none (not returning) or some known return value
        self.assertIsNone(dividetwonumber(10,0))
    
    #unit test for value error
        self.assertIsNone(dividetwonumber(10,"a"))
        self.assertIsNone(dividetwonumber("peter",2))

    #unit test for other possible errors by mocking
    def test_unepected_exception(self):
        #inspect an exception to occur
        with self.assertRaises(Exception):
            #passing no values to function
            dividetwonumber()

if __name__ == "__main__":
    unittest.main()

