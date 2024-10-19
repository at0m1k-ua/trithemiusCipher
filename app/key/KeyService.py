import abc

from app.Alphabet import Alphabet
from app.key.KeywordKey import KeywordKey
from app.key.LinearKey import LinearKey
from app.key.QuadraticKey import QuadraticKey


class KeyService:
    @staticmethod
    def parse(input_str: str, key_type: str, alphabet: Alphabet):
        types = {
            'linear': LinearKey,
            'quadratic': QuadraticKey,
            'keyword': KeywordKey,
        }

        if key_type not in types:
            raise ValueError('No such key type')

        if key_type == 'keyword':
            return KeywordKey.parse(input_str, alphabet)

        return types[key_type].parse(input_str)
