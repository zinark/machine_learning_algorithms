class Perceptron(object):

    def __init__(self, activation_value):
        self.activation_value = activation_value

    def process(self, x_list, w_list):
        n = len(x_list)
        summation = 0.
        for i in range(n):
            x = x_list[i]
            w = w_list[i]
            summation += x * w

        if summation >= self.activation_value:
            return 1.
        return 0.

