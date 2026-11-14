import unittest

from greet import greet


class GreetTests(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice")

    def test_bob(self):
        self.assertEqual(greet("Bob"), "Hello, Bob")

    def test_surrounding_spaces(self):
        self.assertEqual(greet("  Alice  "), "Hello, Alice")

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            greet("")

    def test_whitespace_input(self):
        with self.assertRaises(ValueError):
            greet(" \t\n\r ")


if __name__ == "__main__":
    unittest.main()
