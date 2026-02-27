def a(n):
    sum = 0
    for i in range(0, n + 1):
        sum = sum + i
    return sum

# complexity: O(n)

def b(n):
    sum = 0
    for i in range(0, n + 1):
        sum = sum + i * i
    return sum

# complexity: O(n)

def c(n, a):
    sum = 1
    power = 1
    for i in range(1, n + 1):
        power *= a
        sum += power
    return sum

# complexity: O(n)

def d(n):
    sum = 0
    for i in range(0, n + 1):
        power = 1
        for k in range(i):
            power *= i
        sum = sum + power
    return sum

# complexity: O(n^2)

def e(n):
    prod = 1
    for i in range(1, n + 1):
        prod /= 1 + i
    return prod

# complexity: O(n)

def f(n):
    prod = 1
    fac = 1
    for i in range(1, n + 1):
        fac *= i
        prod /= 1 + fac
    return prod

# complexity: O(n)

def g(n, a):
    prod = 1
    fac = 1
    power = 1
    for i in range(1, n + 1):
        fac *= i
        power *= a
        prod *= power / (1 + fac)
    return prod

# complexity: O(n)

def h(n, m):
    prod = 1
    for i in range(1, n + 1):
        power = 1
        for k in range(m):
            power *= i
        prod /= 1 + power
    return prod

# complexity: O(nm)

def i(n):
    prod = 1
    for i in range(1, n + 1):
        power = 1
        for k in range(i):
            power *= i
        prod /= 1 + power
    return prod

# complexity: O(n^2)
