class QuadraticKey:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def parse(input_str: str):
        if input_str == '':
            raise ValueError('String is empty')

        parts = input_str.split(',')
        args_cnt = len(parts)
        if args_cnt != 3:
            raise ValueError('Cannot parse two comma-separated integers '
                             f'(actual count is {args_cnt})')

        values = []
        for part in parts:
            values.append(int(part.strip()))

        return QuadraticKey(*values)
