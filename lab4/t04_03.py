
"""
Знайдіть найменше 𝑥∈[0, 10], що
𝑓(𝑥) = 𝑥³ + 𝑥 + 1 > 5

Відповідь: x = 1.3787967001189827 (argument)
               1.3787967001189827 (value)
               1.3787967001295511 (neighbours)

"""


def argument(l, r, m, f, c, eps):
    return r - l > eps


def value(l, r, m, f, c, eps):
    return abs(f(m) - c) > eps


def neighbours(l, r, m, f, c, eps):
    return l != m and r != m


condition = argument


def solve(f, c, a, b):
    eps = 1e-10
    l = a
    r = b
    m = (l + r) / 2.0
    while condition(l, r, m, f, c, eps):
        if f(m) <= c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    return m


if __name__ == '__main__':

    f = lambda x: x**3 + x + 1.0
    print(solve(f, 5.0, 0.0, 10.0))



