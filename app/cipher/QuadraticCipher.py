from app.Alphabet import Alphabet
from app.key.QuadraticKey import QuadraticKey


class QuadraticCipher:
    def __init__(self, alphabet: Alphabet):
        self.__alphabet = alphabet

    def encrypt(self, text: str, key: QuadraticKey):
        result = ''
        for i, ch in enumerate(text):
            k = key.a**2 + key.b*i + key.c
            result += self.__alphabet.shift_char(ch, k)

        return result

    def decrypt(self, text: str, key: QuadraticKey):
        result = ''
        for i, ch in enumerate(text):
            k = - (key.a**2 + key.b*i + key.c)
            result += self.__alphabet.shift_char(ch, k)

        return result
