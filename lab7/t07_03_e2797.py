size: int = 200003
count: int
keys: list[str]

EMPTY = "EMPTY"
N: int = 31


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def hash_(key: str) -> int:
    h = 0
    for ch in key:
        h = h * N + ord(ch)
    return h % size


def init():
    global keys, count
    count = 0
    keys = [EMPTY for _ in range(size)]


def rehash():
    global size, keys

    old_keys = keys
    old_size = size

    size = size * 2 + 1
    while not is_prime(size):
        size += 2

    init()

    for i in range(old_size):
        if old_keys[i] != EMPTY:
            set_(old_keys[i])


def set_(key: str) -> None:
    global count

    if count > 0.7 * size:
        rehash()

    i = hash_(key)

    while keys[i] != EMPTY:
        if keys[i] == key:
            return
        i = (i + 1) % size

    keys[i] = key
    count += 1


if __name__ == '__main__':
    n = int(input())
    numbers = input().split()

    init()

    for num in numbers:
        set_(num)

    print(count)