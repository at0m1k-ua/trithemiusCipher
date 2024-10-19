from unittest import TestCase

from app.Alphabet import Alphabet
from app.cipher.QuadraticCipher import QuadraticCipher
from app.key.QuadraticKey import QuadraticKey


class QuadraticCipherTest(TestCase):
    def test_quadratic_cipher_encrypts_and_decrypts_as_expected(self):
        alphabet = Alphabet(['abcdefghijklmnopqrstuvwxyz'])
        key = QuadraticKey(3, 2, 1)
        cipher = QuadraticCipher(alphabet)
        original_string = 'edcba'
        expected_string = 'opqrs'

        encrypted_string = cipher.encrypt(original_string, key)
        self.assertEqual(expected_string, encrypted_string)

        decrypted_string = cipher.decrypt(encrypted_string, key)
        self.assertEqual(original_string, decrypted_string)
