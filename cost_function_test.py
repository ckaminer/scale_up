import unittest

from cost_function import CostFunction
from hypothesis_function import HypothesisFunction

class CostFunctionTest(unittest.TestCase):
    def test_takes_training_set_as_argument(self):
        example_ts = [{'i': 1, 'o': 5}, {'i': 2, 'o': 9}, {'i': 3, 'o': 13}, {'i': 4, 'o': 17}, {'i': 5, 'o': 21}]
        c = CostFunction(example_ts)
        self.assertEqual(example_ts, c.training_set)

    def test_returns_cost_when_slope_greater_than_one(self):
        example_ts = [{'i': 1, 'o': 5}, {'i': 2, 'o': 9}, {'i': 3, 'o': 13}, {'i': 4, 'o': 17}, {'i': 5, 'o': 21}]
        h = HypothesisFunction(.5, 3)
        c = CostFunction(example_ts)
        self.assertEqual(5.9375, c.cost(h))

    def test_returns_cost_when_slope_less_than_one(self):
        example_ts = [{'i': 4, 'o': 2}, {'i': 8, 'o': 3}, {'i': 12, 'o': 4}, {'i': 16, 'o': 5}, {'i': 20, 'o': 6}]
        h = HypothesisFunction(1, .3)
        c = CostFunction(example_ts)
        cost = c.cost(h)
        self.assertEqual(0.1833, float("%.4f" % cost))

if __name__ == '__main__':
    unittest.main()
