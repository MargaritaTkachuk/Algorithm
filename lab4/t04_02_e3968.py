
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
        if f(m) < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    return m


if __name__ == '__main__':
    c = float(input())
    f = lambda x: x**2 + x**0.5
    res = solve(f, c, 0.0, 100000000.0)
    print(f"{res:.9f}")



