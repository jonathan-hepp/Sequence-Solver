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


class SpecialCasesStrategy(BaseStrategy):

    def solve(self, sequence, debug=False):
        if self.__is_fibonacci(sequence):
            return sequence[-2] + sequence[-1]
        raise Exception("Unsolvable sequence")

    def __is_fibonacci(self, sequence):
        return all(map(lambda x: x == 0 or abs(round(x*1.618) - x*1.618) < 1.0 / x, sequence)) and self.__is_fibonacci_ordered(sequence)

    def __is_fibonacci_ordered(self, sequence):
        for i in range(1, len(sequence)-1):
            if sequence[i+1] != sequence[i-1] + sequence[i]:
                return False
        return True


