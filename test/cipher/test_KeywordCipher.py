from unittest import TestCase

from app.Alphabet import Alphabet
from app.cipher.KeywordCipher import KeywordCipher
from app.key.KeywordKey import KeywordKey


class KeywordCipherTest(TestCase):
    def test_keyword_cipher_encrypts_and_decrypts_as_expected(self):
        alphabet = Alphabet(['abcdefghijklmnopqrstuvwxyz'])
        key = KeywordKey.parse('abc', alphabet)
        cipher = KeywordCipher(alphabet)
        original_string = 'fedcba'
        expected_string = 'fffccc'

        encrypted_string = cipher.encrypt(original_string, key)
        self.assertEqual(expected_string, encrypted_string)

        decrypted_string = cipher.decrypt(encrypted_string, key)
        self.assertEqual(original_string, decrypted_string)
