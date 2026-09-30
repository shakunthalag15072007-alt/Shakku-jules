import unittest
from hello import hello_shakunthala


class TestHello(unittest.TestCase):
    def test_hello_shakunthala(self):
        self.assertEqual(hello_shakunthala(), "Hello, Shakunthala!")


if __name__ == "__main__":
    unittest.main()
