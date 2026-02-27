
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class Node:

    def __init__(self, key: str, value: list[str]):
        self.key: str = key
        self.value: list[str] = value
        self.next: Node | None = None


size: int = 1000003
slots: list[Node | None]

N: int = 31

def hash_(author: str) -> int:
    h = 0
    for i in range(len(author)):
        h = h * N + ord(author[i])
    return h % size

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots
    slots = [None for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    i = hash_(author)
    node = slots[i]

    while node is not None:
        if node.key == author:
            if title not in node.value:
                node.value.append(title)
            return
        node = node.next

    new_node = Node(author, [title])
    new_node.next = slots[i]
    slots[i] = new_node


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    i = hash_(author)
    node = slots[i]
    while node is not None:
        if node.key == author:
            if title in node.value:
                return True
        node = node.next
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    i = hash_(author)
    node = slots[i]
    prev = None

    while node is not None:
        if node.key == author:
            if title in node.value:
                node.value.remove(title)

                if not node.value:
                    if prev is None:
                        slots[i] = node.next
                    else:
                        prev.next = node.next

                return True
            return False

        prev = node
        node = node.next
    return False

def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    i = hash_(author)
    node = slots[i]

    while node is not None:
        if node.key == author:
            return sorted(node.value)
        node = node.next

    return []

