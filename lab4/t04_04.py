
"""
На відрізку [1.6, 3] знайдіть корінь рівняння
sin 𝑥 = 𝑥 / 3

Відповідь: x = 2.2788626601162836 (argument)
               2.2788626600755384 (value)
               2.278862660075828 (neighbours)

"""

import math

def argument(l, r, m, f, c, eps):
    return r - l > eps


def value(l, r, m, f, c, eps):
    return abs(f(m) - c) > eps


def neighbours(l, r, m, f, c, eps):
    return l != m and r != m


condition = value


def solve(f, c, a, b):
    eps = 1e-10
    l = a
    r = b
    m = (l + r) / 2.0
    while condition(l, r, m, f, c, eps):
        if f(m) > c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    return m


if __name__ == '__main__':

    f = lambda x: 3 * math.sin(x) - x
    print(solve(f, 0, 1.6, 3.0))



