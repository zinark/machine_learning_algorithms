from termcolor import colored
from math import factorial

t = .2
h = .8
l = [
    t * t * t,
    t * t * h,
    t * h * t,
    t * h * h,

    h * t * t,
    h * t * h,
    h * h * t,
    h * h * h,
]

for i in l:
    print i

print sum(l)

print .032 * 3


def s_calc():
    k = factorial(12) / (factorial(9) * factorial(12 - 9))
    p = .8 ** 9 * .2 ** 3
    return k * p


def calc(n=1, k=0):
    p = factorial(n) / (factorial(k) * factorial(n - k))
    prob = 2 ** -n
    prob = 1
    return p * prob

print colored(calc(1, 0), "red")
print colored(calc(1, 1), "red")
print colored(calc(1, 2), "red")

