#Add Unit Test
import unittest
from main.main import BowlingStatisticsProgram

class TestStringMethods(unittest.TestCase):
    
    def test_two(self):
        windowObject = BowlingStatisticsProgram()
        self.assertEqual(windowObject.test(2), 4, "Supposed to equal")
    def test_not_two(self):
        windowObject = BowlingStatisticsProgram()
        self.assertNotEqual(windowObject.test(2), 5, "Not supposed to equal")
        
if __name__ == '__main__':
    unittest.main()