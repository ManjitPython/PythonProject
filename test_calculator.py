import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)



if __name__ == '__main__':
    unittest.main()
