import sys

from BSE.Perceptron import Perceptron

sys.path.append("..")


def and_network():
    p = Perceptron(.75)
    xs = [
        ([1, 1], 1),
        ([0, 0], 0),
        ([0, 1], 0),
        ([1, 0], 0)
    ]
    w = [.5, .5]
    for x, y in xs:
        print x, ".", w, "=", p.process(x, w), "expected=", y


def or_network():
    p = Perceptron(.25)
    xs = [
        ([1, 1], 1),
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 1)
    ]
    w = [.5, .5]
    for x, y in xs:
        print x, ".", w, "=", p.process(x, w), "expected=", y


def not_network():
    p = Perceptron(-1)
    xs = [
        ([1], 0),
        ([0], 1)
    ]
    w = [-2]
    for x, y in xs:
        print x, ".", w, "=", p.process(x, w), "expected=", y


def xor_network():
    p_and = Perceptron(.75)
    w_and = [.5, .5]

    p = Perceptron(1)
    w = [1, -2, 1]

    xs = [
        ([1, 1], 0),
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 1)
    ]

    for x, y in xs:
        y_and = p_and.process(x, w_and)
        x_in = x + [y_and]
        y_out = p.process(x_in, w)
        print x_in, ".", w, "=", y_out, "expected=", y


xor_network()
