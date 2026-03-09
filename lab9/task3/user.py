"""
Проведіть аналіз швидкодії реалізованих алгоритмів сортування
для різних типів та розмірів масивів (не відсортований масив
згенерований випадковим чином, масив відсортований за зростанням,
масив відсортований за спаданням елементів).
"""

N = 10000     # Кількість елементів масиву.
              # Використовується у головній програмі для генерування
              # масиву з випадкових чисел


def bubble_sort(array):
    """ Сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    """
    n = len(array)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"

    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for i in range(n - 1, 0, -1):
        flag = True
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            break


def selection_sort(array):
    """ Сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(n - 1, 0, -1):
        max_index = 0
        for j in range(1, i + 1):
            if array[max_index] < array[j]:
                max_index = j
        array[j], array[max_index] = array[max_index], array[j]


def insertion_sort(array):
    """ Сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(1, n):
        el = array[i]
        pos = i
        while pos > 0:
            if array[pos - 1] > el:
                array[pos] = array[pos - 1]
            else:
                break
            pos -= 1
        array[pos] = el


def merge_sort(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    if len(array) == 1 or len(array) == 0:
        return
    m = len(array) // 2
    arr_left = array[:m]
    arr_right = array[m:]
    merge_sort(arr_left)
    merge_sort(arr_right)
    i = 0
    j = 0
    k = 0
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] < arr_right[j]:
            array[k] = arr_left[i]
            i += 1
        else:
            array[k] = arr_right[j]
            j += 1
        k += 1

    while i < len(arr_left):
        array[k] = arr_left[i]
        i += 1
        k += 1

    while j < len(arr_right):
        array[k] = arr_right[j]
        j += 1
        k += 1


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

def quick_sort(array):
    """ Швидке сортування

        :param array: Масив (список однотипових елементів)
        :return: None
        """
    left = 0
    right = len(array) - 1
    q_sort(array, left, right)

