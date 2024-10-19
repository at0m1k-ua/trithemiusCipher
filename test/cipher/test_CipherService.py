from unittest import TestCase

from app.Alphabet import Alphabet
from app.cipher.CipherService import CipherService
from app.key.KeyService import KeyService


class CipherServiceTest(TestCase):

    def setUp(self):
        self.__alphabet = Alphabet(['abcdefghijklmnopqrstuvwxyz'])
        self.__cipher_service = CipherService(self.__alphabet)

    def test_cipher_service_performs_linear_cipher(self):
        self.__cipher_service_encrypts_and_decrypts_as_expected(
            'edcba',
            '2, 1',
            'linear',
            'fghij'
        )

    def test_cipher_service_performs_quadratic_cipher(self):
        self.__cipher_service_encrypts_and_decrypts_as_expected(
            'edcba',
            '3, 2, 1',
            'quadratic',
            'opqrs'
        )

    def test_cipher_service_performs_keyword_cipher(self):
        self.__cipher_service_encrypts_and_decrypts_as_expected(
            'fedcba',
            'abc',
            'keyword',
            'fffccc'
        )

    def __cipher_service_encrypts_and_decrypts_as_expected(self,
                                                           original,
                                                           key_string,
                                                           cipher_type,
                                                           expected):
        key = KeyService.parse(key_string, cipher_type, self.__alphabet)
        encrypted = self.__cipher_service.encrypt(original, key)
        self.assertEqual(expected, encrypted)

        decrypted = self.__cipher_service.decrypt(encrypted, key)
        self.assertEqual(original, decrypted)
