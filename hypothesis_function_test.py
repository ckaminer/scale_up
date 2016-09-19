import unittest

from hypothesis_function import HypothesisFunction

class HypothesisFunctionTest(unittest.TestCase):
    def test_has_two_theta_values(self):
        h = HypothesisFunction(2,3)
        self.assertEqual(2, h.theta_0)
        self.assertEqual(3, h.theta_1)

    def test_result_returns_intercept_when_x_is_zero(self):
        h = HypothesisFunction(2,3)
        self.assertEqual(2, h.result(0))

    def test_result_returns_y_value_for_given_x(self):
        h = HypothesisFunction(2,3)
        self.assertEqual(5, h.result(1))
        self.assertEqual(17, h.result(5))
        self.assertEqual(32, h.result(10))

if __name__ == '__main__':
    unittest.main()
