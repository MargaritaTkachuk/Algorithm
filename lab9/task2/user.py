
"""
Реалізуйте швидкий алгоритм сортування QuickSort.
"""

N = 1000000  # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


def q_sort(array, left, right):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    if left >= right:
        return
    i = left
    j = right
    el = array[i + (j - i) // 2]
    while True:
        while array[i] < el:
            i += 1
        while array[j] > el:
            j -= 1
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]

        i += 1
        j -= 1
    q_sort(array, left, j)
    q_sort(array, j + 1, right)

def sort(array):
    left = 0
    right = len(array) - 1
    q_sort(array, left, right)



