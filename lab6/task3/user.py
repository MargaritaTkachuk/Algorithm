
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

size: int = 11
count: int
authors: list[str]
titles: list[list[str]]

EMPTY = "EMPTY"
DELETED = "DELETED"

N: int = 31

def hash_(author: str) -> int:
    h = 0
    for i in range(len(author)):
        h = h * N + ord(author[i])
    return h % size

def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def rehash():
    global size
    size = size * 2 + 1
    while not is_prime(size):
        size += 2
    _authors = authors
    _titles = titles
    init()
    for i in range(len(_authors)):
        if _authors[i] not in (EMPTY, DELETED):
            for title in _titles[i]:
                addBook(_authors[i], title)

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global count, authors, titles
    count = 0
    authors = [EMPTY for _ in range(size)]
    titles = [[] for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global count
    if count > 0.7 * size:
        rehash()

    i = hash_(author)
    j = -1
    while authors[i] != EMPTY:
        if authors[i] == author:
            if title not in titles[i]:
                titles[i].append(title)
            return
        if j == -1 and authors[i] == DELETED:
            j = i
        i = (i + 1) % size
    if j == -1:
        j = i
        count += 1
    authors[j] = author
    titles[j] = [title]


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    i = hash_(author)
    while authors[i] != EMPTY:
        if authors[i] == author:
            for j in range(len(titles[i])):
                if titles[i][j] == title:
                    return True
        i = (i + 1) % size
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global count
    i = hash_(author)
    while authors[i] != EMPTY:
        if authors[i] == author:
            for j in range(len(titles[i])):
                if titles[i][j] == title:
                    titles[i].remove(title)
                    if len(titles[i]) == 0:
                        authors[i] = DELETED
                       # count -= 1
                    return True
        i = (i + 1) % size
    return False


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    i = hash_(author)
    while authors[i] != EMPTY:
        if authors[i] == author:
            return sorted(titles[i])
        i = (i + 1) % size
    return []

if __name__ == '__main__':
    init()
    print(authors)
    print(titles)
