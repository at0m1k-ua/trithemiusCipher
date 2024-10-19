from app.Alphabet import Alphabet
from app.cipher.KeywordCipher import KeywordCipher
from app.cipher.LinearCipher import LinearCipher
from app.cipher.QuadraticCipher import QuadraticCipher
from app.key.KeywordKey import KeywordKey
from app.key.LinearKey import LinearKey
from app.key.QuadraticKey import QuadraticKey


class CipherService:
    def __init__(self, alphabet: Alphabet):
        self.__ciphers = {
            LinearKey: LinearCipher(alphabet),
            QuadraticKey: QuadraticCipher(alphabet),
            KeywordKey: KeywordCipher(alphabet)
        }

    def encrypt(self, text: str, key):
        return self.__cipher_for_key(key).encrypt(text, key)
    
    def decrypt(self, text: str, key):
        return self.__cipher_for_key(key).decrypt(text, key)
    
    def __cipher_for_key(self, key):
        key_type = type(key)
        if key_type not in self.__ciphers:
            raise KeyError(f'Unknown key type {key_type}')
        
        return self.__ciphers[key_type]
