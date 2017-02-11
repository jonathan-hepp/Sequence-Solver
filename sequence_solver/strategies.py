import string

class BaseStrategy:

    def solve(self, sequence, debug):
        raise NotImplemented()


class DiffTableStrategy(BaseStrategy):

    def solve(self, sequence, debug=False):
        levels = self.__calculate_difference({0 : sequence}, sequence)
        if debug:
            print(levels)
        return self.__calculate_next_item(levels)

    def __calculate_difference(self, levels, sequence):
        new_sequence = []
        for i in range(1, len(sequence)):
            new_sequence.append(sequence[i] - sequence[i-1])
        levels[len(levels)] = new_sequence
        if len(new_sequence) == 1:
            raise Exception("Unsolvable sequence")
        return levels if self.__all_elements_equal(new_sequence) else self.__calculate_difference(levels, new_sequence)

    def __all_elements_equal(self, sequence):
        return len(set(sequence)) <= 1

    def __calculate_next_item(self, levels):
        next_item = 0
        for sequence in levels.values():
            next_item += sequence[-1]
        return next_item


class AlphabetSubstitutionStrategy(BaseStrategy):
    __alphabet = {l : string.ascii_lowercase.index(l)+1 for l in string.ascii_lowercase}
    __diffTableStrategy = DiffTableStrategy()

    def solve(self, sequence, debug=False):
        new_sequence = [string.ascii_lowercase.index(l.lower())+1 for l in sequence]
        return string.ascii_lowercase[(self.__diffTableStrategy.solve(new_sequence, debug)-1) % len(string.ascii_lowercase)]

