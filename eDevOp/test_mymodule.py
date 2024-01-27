import unittest
from eDevOp.mymodule import square

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(10), 100)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(-5), 25)

if __name__ == '__main__':
    unittest.main()
# $ python3 -m unittest test_mymodule.py



