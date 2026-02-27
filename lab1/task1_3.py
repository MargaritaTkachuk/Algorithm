def a(n, k):
    k += 1         # 4
    i = n          # 2
    while i > 0:   # 3 * (n + 1)
        i -= 1     # 4 * n

# k += 1 <=> k = k + 1

# n = 0 -> while condition: 1,     loop block: 0
# n = 1 -> while condition: 2,     loop block: 1
# n = 2 -> while condition: 3,     loop block: 2
# n     -> while condition: n + 1, loop block: n

# sum = 7n + 9


def b(n, k):
    i = n           # 2
    while i > 1:    # 3 * (m + 1)
        k += 1      # 4 * m
        i //= 2     # 4 * m

# n = 2^m -> m = log2(n)

# n = 1, m = 0 -> loop block: 0
# n = 2, m = 1 -> loop block: 1
# n = 4, m = 2 -> loop block: 2
# n = 8, m = 3 -> loop block: 3
# n    , m     -> loop block: m

# sum = 11m + 5 = 11 log2(n) + 5

def c(n, k):
    i = 0              # 2
    while i < n:       # 3 * (n/2 + 1)
        j = 0          # 2 * n/2
        while j < n:   # 3 * n/2 * (n/2 + 1)
            k += 1     # 4 * n/2 * n/2
            j += 2     # 4 * n/2 * n/2
        i += 2         # 4 * n/2


# sum = 11/4 * n^2 + 6n + 5


def d(n, k):
    i = 0                 # 2
    while i < n:          # 3 * (n + 1)
        j = 0             # 2 * n
        while j < i * i:  # 5 * (1 + 2 + 5 + 10 + ... + ((n - 1)^2 + 1)) = 5 * ((1 + 4 + 9 + ... + (n - 1)^2) + n) = 5 * ((n * (n - 1) * (2n - 1) / 6)) + n)
            k += 1        # 4 * (1 + 4 + 9 + ... + (n - 1)^2) = 4 * (n * (n - 1) * (2n - 1) / 6)
            j += 1        # 4 * (1 + 4 + 9 + ... + (n - 1)^2) = 4 * (n * (n - 1) * (2n - 1) / 6)
        i += 1            # 4 * n

# sum = 13/6 * (n * (n - 1) * (2n - 1)) + 14n + 5


def e(n, k):
    i = 1             # 2
    while i < n:      # 3 * (m + 1)
        j = 1         # 2 * m
        while j < n:  # 3 * m * (m + 1)
            k += 1    # 4 * m * m
            j *= 2    # 4 * m * m
        i *= 2        # 4 * m

# n = 2^m -> m = log2(n)

# sum = 11m^2 + 12m + 5 = 11 log2(n)^2 + 12 log2(n) + 5


def f(n, k):
    i = 1             # 2
    while i < n:      # 3 * (m + 1)
        j = i         # 2 * m
        while j < n:  # 3 * ((m + 1) + m + (m - 1) + ... + 1) = 3/2 * (m + 2) * (m + 1)
            k += 1    # 4 * (m + (m - 1) + (m - 2) + 1) = 2 * (m + 1) * m
            j *= 2    # 4 * (m + (m - 1) + (m - 2) + 1) = 2 * (m + 1) * m
        i *= 2        # 4 * m

# n = 2^m -> m = log2(n)

# sum = 11/2 * m^2 + 35/2 * m + 5 = 11/2 log2(n)^2 + 35/2 log2(n) + 5