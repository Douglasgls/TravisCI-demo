import unittest
from main import soma

class TestSomar(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 2), 4)
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(2, 4), 6)
        self.assertEqual(soma(2, 5), 7)

if __name__ == "__main__":
    unittest.main()