from unittest import TestCase

from app.key.LinearKey import LinearKey


class LinearKeyTest(TestCase):
    def test_linear_key_is_parsed_correctly(self):
        key = LinearKey.parse('2, 5')
        self.assertEqual(2, key.a)
        self.assertEqual(5, key.b)

    def test_linear_key_raises_error_with_more_than_2_args(self):
        with self.assertRaises(ValueError):
            LinearKey.parse('2, 5, 6')

    def test_linear_key_raises_error_with_less_than_2_args(self):
        with self.assertRaises(ValueError):
            LinearKey.parse('2')

    def test_linear_key_raises_error_with_empty_args(self):
        with self.assertRaises(ValueError):
            LinearKey.parse('')

    def test_inverted_property_inverts_key(self):
        original_key = LinearKey(5, 7)
        inverted_key = original_key.inverted
        self.assertEqual(-5, inverted_key.a)
        self.assertEqual(-7, inverted_key.b)
