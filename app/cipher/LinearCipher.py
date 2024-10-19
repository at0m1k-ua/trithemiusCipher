from app.Alphabet import Alphabet
from app.key.LinearKey import LinearKey


class LinearCipher:
    def __init__(self, alphabet: Alphabet):
        self.__alphabet = alphabet

    def encrypt(self, text: str, key: LinearKey):
        result = ''
        for i, ch in enumerate(text):
            k = key.a*i + key.b
            result += self.__alphabet.shift_char(ch, k)

        return result

    def decrypt(self, text: str, key: LinearKey):
        result = ''
        for i, ch in enumerate(text):
            k = -key.a*i - key.b
            result += self.__alphabet.shift_char(ch, k)

        return result
