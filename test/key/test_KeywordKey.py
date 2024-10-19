from unittest import TestCase

from app.Alphabet import Alphabet
from app.key.KeywordKey import KeywordKey


class KeywordKeyTest(TestCase):
    def test_right_keyword_is_parsed_correctly(self):
        alphabet = Alphabet(['abcdefghijklmnopqrstuvwxyz'])
        key = KeywordKey.parse('edcbabc', alphabet)
        self.assertEqual(
            [4, 3, 2, 1, 0, 1, 2],
            key.sequence
        )

    def test_unknown_character_throws_error(self):
        alphabet = Alphabet(['abcde'])
        with self.assertRaises(ValueError):
            KeywordKey.parse('abcfe', alphabet)
