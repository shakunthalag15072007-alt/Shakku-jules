import unittest
from addition import add


class TestAddition(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)
        self.assertAlmostEqual(add(-1.5, 2.5), 1.0)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
