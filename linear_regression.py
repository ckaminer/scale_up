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
            grad_desc_zero = grad_desc_zero + decrease
        new_theta = hypothesis.theta_0 - ((grad_desc_zero * alpha) / len(self.training_set))
        return new_theta

    def update_theta_one(self, alpha, hypothesis):
        grad_desc_one = 0
        for pair in self.training_set:
            decrease = (hypothesis.result(pair["i"]) - pair["o"]) * pair["i"]
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


# # Red Sox training set.  Hits/Runs from 2011-2016
# red_sox_ts = [{'i': 999, 'o': 546},  {'i': 963, 'o': 525},  {'i': 1010, 'o': 549},
#               {'i': 825, 'o': 389},  {'i': 975, 'o': 506},  {'i': 1024, 'o': 565}]
# rockies_ts = [{'i': 898, 'o': 519},  {'i': 1030, 'o': 593}, {'i': 992, 'o': 526},
#               {'i': 1088, 'o': 568}, {'i': 995, 'o': 518},  {'i': 1000, 'o': 596}]
# # Create new Regression instance with given training set
# lr = LinearRegression(red_sox_ts)
# # Create new hypothesis instance with random starting thetas
# h = HypothesisFunction()
# # Calculate and print best fit
# best_fit = lr.find_best_fit(h, .000001, .000005, 100)
# print best_fit
# # Use hypothesis function and best fit results to predict 2016 run totals
# result_fun = HypothesisFunction(best_fit["b"], best_fit["m"])
# # Sox recorded 1024 hits in 2016 and scored 565 runs
# print result_fun.result(1024)
