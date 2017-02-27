import random

class HypothesisFunction:
    def __init__(self, theta_0 = random.uniform(-1,1), theta_1 = random.uniform(-1,1)):
        self.theta_0 = theta_0
        self.theta_1 = theta_1

    def result(self, x):
        y = self.theta_0 + (self.theta_1 * x)
        return y


# h = HypothesisFunction()
# print h.result(1000)
