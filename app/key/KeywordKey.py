from typing import List

from app.Alphabet import Alphabet


class KeywordKey:
    def __init__(self, sequence: List[int]):
        self.sequence = sequence

    @staticmethod
    def parse(input_str: str, alphabet: Alphabet):
        sequence = []

        for ch in input_str:
            try:
                sequence.append(alphabet.index(ch))
            except KeyError as e:
                raise ValueError(*e.args)

        return KeywordKey(sequence)
