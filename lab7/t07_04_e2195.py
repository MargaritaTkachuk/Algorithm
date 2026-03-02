size = 200003
keys = [None] * size
used = [0] * size

N_HASH = 31


def hash_(key: str) -> int:
    h = 0
    for ch in key:
        h = h * N_HASH + ord(ch)
    return h % size


def init():
    global keys, used
    keys = [None] * size
    used = [0] * size


def set_(key: str):
    i = hash_(key)
    while keys[i] is not None:
        if keys[i] == key:
            return
        i = (i + 1) % size
    keys[i] = key


def find_and_mark(key: str) -> bool:
    i = hash_(key)
    while keys[i] is not None:
        if keys[i] == key:
            used[i] = 1
            return True
        i = (i + 1) % size
    return False


def vocabulary_used_all() -> bool:
    for i in range(size):
        if keys[i] is not None and used[i] == 0:
            return False
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())

    init()

    for _ in range(n):
        set_(input().strip().lower())

    text_lines = [input().lower() for _ in range(m)]
    text = " ".join(text_lines)

    words = []
    current = ""

    for ch in text:
        if 'a' <= ch <= 'z':
            current += ch
        else:
            if current:
                words.append(current)
                current = ""

    if current:
        words.append(current)

    unknown_found = False

    for w in words:
        if not find_and_mark(w):
            print("Some words from the text are unknown.")
            unknown_found = True
            break

    if not unknown_found:
        if vocabulary_used_all():
            print("Everything is going to be OK.")
        else:
            print("The usage of the vocabulary is not perfect.")