# -*- coding: utf-8 -*-

import strategies

class SequenceSolver:

    def __init__(self, sequence):
        self.sequence = sequence

    def solve(self):
        for strategy in StrategiesFactory():
            try:
                return strategy.solve(self.sequence)
            except:
                pass

 
class StrategiesFactory:

    def __init__(self):
        self.index = 0
        self.strategies = StrategiesFactory.create_all()

    def create_all():
        strategy_list = []
        for strategy in strategies.BaseStrategy.__subclasses__():
            strategy_list.append(strategy())
        return strategy_list

    def __iter__(self):
        return self

    def __next__(self):
        try:
            strategy = self.strategies[self.index]
            self.index += 1
            return strategy
        except:
            raise StopIteration()

