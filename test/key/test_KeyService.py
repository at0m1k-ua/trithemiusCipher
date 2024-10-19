from unittest import TestCase

from app.Alphabet import Alphabet
from app.key.KeyService import KeyService
from app.key.KeywordKey import KeywordKey
from app.key.LinearKey import LinearKey
from app.key.QuadraticKey import QuadraticKey


class KeyServiceTest(TestCase):
    def test_parse_keyword_key(self):
        alphabet = Alphabet(['abcde'])
        key = KeyService.parse('cba', 'keyword', alphabet)
        self.assertEqual(KeywordKey, type(key))

    def test_parse_linear_key(self):
        key = KeyService.parse('1, 2', 'linear', Alphabet([]))
        self.assertEqual(LinearKey, type(key))

    def test_parse_quadratic_key(self):
        key = KeyService.parse('1, 2, 3', 'quadratic', Alphabet([]))
        self.assertEqual(QuadraticKey, type(key))
