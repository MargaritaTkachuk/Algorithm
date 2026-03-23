import sys
sys.set_int_max_str_digits(0)

def mult_karatsuba(a, b):
    if a < 10 or b < 10:
        return a * b
    n = max(len(str(a)), len(str(b)))
    m = n // 2
    k = 10 ** m
    a1 = a // k
    a0 = a % k
    b1 = b // k
    b0 = b % k
    z2 = mult_karatsuba(a1, b1)
    z0 = mult_karatsuba(a0, b0)
    z1 = mult_karatsuba(a1 + a0, b1 + b0) - z2 - z0
    return z2 * (10 ** (2 * m)) + z1 * (10 ** m) + z0


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(mult_karatsuba(a, b))