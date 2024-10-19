from unittest import TestCase

from app.Alphabet import Alphabet


class AlphabetTest(TestCase):
    def test_alphabets_set_shifts_chars(self):
        input_str = 'AbCdE123fg'
        expected_str = 'CdEaB123fg'

        actual_str = ''
        alphabet = Alphabet(['abcde', 'ABCDE'])
        for ch in input_str:
            actual_str += alphabet.shift_char(ch, 2)

        self.assertEqual(expected_str, actual_str)

    def test_alphabet_is_loaded_from_json(self):
        path = '../alphabet.json'
        alphabet = Alphabet.load_from_json(path)
        self.assertGreater(len(alphabet.sequences), 0)

    def test_index_raises_exception_when_char_does_not_exist(self):
        alphabet = Alphabet(['abcde'])

        with self.assertRaises(KeyError):
            self.assertFalse(alphabet.index('f'))

    def test_index_returns_index_when_char_exists(self):
        alphabet = Alphabet(['abcde'])
        self.assertEqual(2, alphabet.index('c'))

    def test_error_is_raised_when_multiple_char_is_specified(self):
        alphabet = Alphabet(['abcde'])

        with self.assertRaises(ValueError):
            alphabet.index('dog')
