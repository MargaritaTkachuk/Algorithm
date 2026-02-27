def f(n):
    sum = 0                     # O(1)
    for i in range(1, n + 1):   # O(n)
        sum = sum + i           # O(n)
    return sum                  # O(1)

# complexity: O(n)
# result: sum_{i = 1}^{n} i

def f_optimized(n):
    return n * (n + 1) / 2      # O(1)

# complexity: O(1)

