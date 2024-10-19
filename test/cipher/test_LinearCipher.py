from unittest import TestCase

from app.Alphabet import Alphabet
from app.cipher.LinearCipher import LinearCipher
from app.key.LinearKey import LinearKey


class LinearCipherTest(TestCase):
    def test_linear_cipher_encrypts_and_decrypts_as_expected(self):
        alphabet = Alphabet(['abcdefghijklmnopqrstuvwxyz'])
        key = LinearKey(2, 1)
        cipher = LinearCipher(alphabet)
        original_string = 'edcba'
        expected_string = 'fghij'

        encrypted_string = cipher.encrypt(original_string, key)
        self.assertEqual(expected_string, encrypted_string)

        decrypted_string = cipher.decrypt(encrypted_string, key)
        self.assertEqual(original_string, decrypted_string)
