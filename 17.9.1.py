try:
    array = [float(x) for x in input("Введите числа в любом порядке, через пробел: ").split()]
except ValueError:
    print('В введенной последовательности чисел ошибка')


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, low, high):
    if low < high:
        split_point = partition(array, low, high)
        quick_sort_helper(array, low, split_point - 1)
        quick_sort_helper(array, split_point + 1, high)

def partition(array, low, high):
    pivot_value = array[low]
    left_mark = low + 1
    right_mark = high
    done = False

    while not done:
        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and array[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            array[left_mark], array[right_mark] = array[right_mark], array[left_mark]

    array[low], array[right_mark] = array[right_mark], array[low]
    return right_mark


print("Исходный массив: ", array)
result = quick_sort(array)
print("Результат сортировки:", result)

try:
    element = float(input('Введите число: '))
except ValueError:
        print('Это не число')

def binary_search(result, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if result[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < result[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(result, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(result, element, middle + 1, right)
print(binary_search(result, element, left, right))

