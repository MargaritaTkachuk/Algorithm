def f(n):
    sum = 0                     # O(1)
    for i in range(1, n + 1):   # O(n)
        sum = sum + i           # O(n)
    return sum                  # O(1)

# complexity: O(n)
# result: sum_{i = 1}^{n} i

def g(n):
    sum = 0                     # O(1)
    for i in range(1, n + 1):   # O(n)
        sum = sum + i + f(i)    # O(n^2)
    return sum                  # O(1)

# complexity: O(n^2)

def h(n):
    return f(n) + g(n)          # O(n^2)

# complexity: O(n^2)
# result: 2 sum_{i = 1}^{n} i + sum_{i = 1}^{n} sum_{k = 1}^{i} k

def h_optimized(n):
    return n * (n + 1) / 2 + 3/4 * n * (n + 1) + n * (n + 1) * (2 * n + 1) / 12

# complexity: O(1)
