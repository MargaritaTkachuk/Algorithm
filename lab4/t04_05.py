
"""
На відрізку [0, 2] знайдіть корінь рівняння
𝑥³ + 4𝑥² + 𝑥 − 6 = 0

Відповідь: x = 0.9999999999708962 (argument)
               1.0 (value)
               1.0 (neighbours)

"""


def argument(l, r, m, f, c, eps):
    return r - l > eps


def value(l, r, m, f, c, eps):
    return abs(f(m) - c) > eps


def neighbours(l, r, m, f, c, eps):
    return l != m and r != m


condition = neighbours


def solve(f, c, a, b):
    eps = 1e-10
    l = a
    r = b
    m = (l + r) / 2.0
    while condition(l, r, m, f, c, eps):
        if f(m) < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    return m


if __name__ == '__main__':

    f = lambda x: x**3 + 4*x**2 + x - 6.0
    print(solve(f, 0.0, 0.0, 2.0))



