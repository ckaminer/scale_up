import math
from hypothesis_function import HypothesisFunction
from cost_function import CostFunction

class LinearRegression:
    def __init__(self, training_set):
        self.training_set = training_set

    def update_theta_zero(self, alpha, hypothesis):
        grad_desc_zero = 0
        for pair in self.training_set:
            decrease = hypothesis.result(pair["i"]) - pair["o"]
            # decrease = hypothesis.theta_0 + (hypothesis.theta_1 * pair["i"]) - pair["o"]
            grad_desc_zero = grad_desc_zero + decrease
        new_theta = hypothesis.theta_0 - ((grad_desc_zero * alpha) / len(self.training_set))
        return new_theta

    def update_theta_one(self, alpha, hypothesis):
        grad_desc_one = 0
        for pair in self.training_set:
            decrease = (hypothesis.result(pair["i"]) - pair["o"]) * pair["i"]
            # decrease = (hypothesis.theta_0 + (hypothesis.theta_1 * pair["i"]) - pair["o"]) * pair["i"]
            grad_desc_one = grad_desc_one + decrease
        new_theta = hypothesis.theta_1 - ((grad_desc_one * alpha) / len(self.training_set))
        return new_theta

    def update_thetas(self, alpha, hypothesis):
        theta_0 = self.update_theta_zero(alpha, hypothesis)
        theta_1 = self.update_theta_one(alpha, hypothesis)
        return HypothesisFunction(theta_0, theta_1)

    def find_best_fit(self, hypothesis, alpha, threshold, n):
        current_hypothesis = hypothesis
        for i in range(n):
            if CostFunction(self.training_set).cost(current_hypothesis) < threshold:
                break
            else:
                current_hypothesis = self.update_thetas(alpha, current_hypothesis)

        return {"b": current_hypothesis.theta_0, "m": current_hypothesis.theta_1}


red_sox_ts = [{'i': 999, 'o': 546}, {'i': 963, 'o': 525}, {'i': 1010, 'o': 549}, {'i': 825, 'o': 389}, {'i': 975, 'o': 506}]
lr = LinearRegression(red_sox_ts)
# h = HypothesisFunction(1, .5)
h = HypothesisFunction()
print lr.find_best_fit(h, .5, 2, 3)


# example_ts = [{'i': 1, 'o': 5}, {'i': 2, 'o': 9}, {'i': 3, 'o': 13}, {'i': 4, 'o': 17}, {'i': 5, 'o': 21}]
# # example_ts = [{'i': 4, 'o': 2}, {'i': 8, 'o': 3}, {'i': 12, 'o': 4}, {'i': 16, 'o': 5}, {'i': 20, 'o': 6}]
# lr = LinearRegression(example_ts)
# h = HypothesisFunction()
# print lr.find_best_fit(h, .05, .02, 500000)
