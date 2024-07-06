#7-6-24
#first ever test case

import unittest
import Calculations

class testCalculations():

    def testSum(self):
        self.assertEqual(Calculations.getSum(6,5), 11, 'Sum is wrong')