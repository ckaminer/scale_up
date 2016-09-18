class HypothesisFunction:
    def __init__(self, theta_0, theta_1):
        self.theta_0 = theta_0
        self.theta_1 = theta_1

    def result(self, x):
        y = self.theta_0 + (self.theta_1 * x)
        return y
