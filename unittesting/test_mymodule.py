import unittest

from mymodule import add, multiply

class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)

if __name__ == "__main__":
    unittest.main()
