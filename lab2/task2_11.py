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
# result: sum_{i = 1}^{n} (i + sum_{k = 1}^{i} k)
''' optimization g(n): sum_{i = 1}^{n} (i + sum_{k = 1}^{i} k) = 
                       = n (n + 1) / 2 + sum_{i = 1}^{n} sum_{k = 1}^{i} k = 
                       = n (n + 1) / 2 + sum_{i = 1}^{n} i (i + 1) / 2 = 
                       = n (n + 1) / 2 + 1/2 sum_{i = 1}^{n} i^2 + 1/2 sum_{i = 1}^{n} i =
                       = n (n + 1) / 2 + n (n + 1)(2n + 1) / 12 + n (n + 1) / 4    
'''
def g_optimized(n):
    return 3/4 * n * (n + 1) + n * (n + 1) * (2 * n + 1) / 12

# complexity: O(1)