from unittest import TestCase

from app.key.QuadraticKey import QuadraticKey


class QuadraticKeyTest(TestCase):
    def test_linear_key_is_parsed_correctly(self):
        key = QuadraticKey.parse('2, 5, 7')
        self.assertEqual(2, key.a)
        self.assertEqual(5, key.b)
        self.assertEqual(7, key.c)

    def test_linear_key_raises_error_with_more_than_3_args(self):
        with self.assertRaises(ValueError):
            QuadraticKey.parse('2, 5, 6, 8')

    def test_linear_key_raises_error_with_less_than_3_args(self):
        with self.assertRaises(ValueError):
            QuadraticKey.parse('2, 5')

    def test_linear_key_raises_error_with_empty_args(self):
        with self.assertRaises(ValueError):
            QuadraticKey.parse('')
