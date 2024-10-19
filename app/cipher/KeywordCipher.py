from app.Alphabet import Alphabet
from app.key.KeywordKey import KeywordKey


class KeywordCipher:
    def __init__(self, alphabet: Alphabet):
        self.__alphabet = alphabet

    def encrypt(self, text: str, key: KeywordKey):
        result = ''
        sequence = key.sequence
        sequence_len = len(sequence)
        for i, ch in enumerate(text):
            k = sequence[i % sequence_len]
            result += self.__alphabet.shift_char(ch, k)

        return result

    def decrypt(self, text: str, key: KeywordKey):
        result = ''
        sequence = key.sequence
        sequence_len = len(sequence)
        for i, ch in enumerate(text):
            k = -sequence[i % sequence_len]
            result += self.__alphabet.shift_char(ch, k)

        return result
