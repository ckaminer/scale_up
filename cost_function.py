import math
from hypothesis_function import HypothesisFunction

class CostFunction:
    def __init__(self, training_set):
        self.training_set = training_set

    def cost(self, hypothesis):
        length = len(self.training_set)
        normalizer = 1 / (2.0 * (length + 1))
        sum = 0
        for pair in self.training_set:
            diff = hypothesis.result(pair["i"]) - pair["o"]
            sum = sum + math.pow(diff, 2)
        return sum * normalizer
