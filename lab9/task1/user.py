"""
Реалізуйте алгоритм сортування злиттям.
"""

N = 1000000  # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    if len(array) == 1 or len(array) == 0:
        return
    m = len(array) // 2
    arr_left= array[:m]
    arr_right = array[m:]
    sort(arr_left)
    sort(arr_right)
    i = 0
    j = 0
    k= 0
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











#


