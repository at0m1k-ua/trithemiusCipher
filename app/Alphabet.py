import json


class Alphabet:
    def __init__(self, sequences):
        self.sequences = sequences

    @staticmethod
    def load_from_json(filepath: str):
        with open(filepath, 'r') as file:
            alphabets = json.load(file)
            return Alphabet(alphabets)

    def shift_char(self, ch: str, step: int):
        self.__assert_is_one_char(ch)

        for case in self.sequences:
            if ch in case:
                new_index = (case.index(ch) + step) % len(case)
                return case[new_index]

        return ch

    def index(self, ch: str):
        self.__assert_is_one_char(ch)

        for sequence in self.sequences:
            if ch in sequence:
                return sequence.index(ch)

        raise KeyError(f'No character "{ch}" found in alphabet')

    @staticmethod
    def __assert_is_one_char(ch: str):
        if len(ch) > 1:
            raise ValueError("Char should have length = 1")
