#задаем массив вещественных чисел и проверяем его
try:
    array = [float(x) for x in input("Введите числа в любом порядке, через пробел: ").split()]
except ValueError:
    print('В введенной последовательности чисел ошибка')

# сортируем массив методом быстрой сортировки
def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1) #использует неотсортированный массив, начальный индекс и конечный индекс
    return array #возвращает отсортированный массив

# функция принимает неотсортированный массив, начальный и конечный индекс массива, разбивает массив на подмассивы
def quick_sort_helper(array, low, high):
    if low < high:
        split_point = partition(array, low, high) #переменная split_point вызывает функцию partition
        quick_sort_helper(array, low, split_point - 1)#рекурсивно вызываем функцию для одной части массива
        quick_sort_helper(array, split_point + 1, high)#рекурсивно вызываем функцию для второй части массива

# функция сравнивает левую метку и правую метку со значением опорного элемента
def partition(array, low, high):
    pivot_value = array[low] #зададим переменную опорная метка и присваиваем ей первое значение в массиве
    left_mark = low + 1 #задаем переменную левая метка, это будет второй элемент в массиве
    right_mark = high #задаем переменную правая метка, это будет последний элемент массива
    done = False #переменная для завершения цикла while not done

    while not done: #цикл работает, пока done не примет значение True
        while left_mark <= right_mark and array[left_mark] <= pivot_value: #цикл передвижения левой метки
            left_mark += 1
        while right_mark >= left_mark and array[right_mark] >= pivot_value: # цикл передвижения правой метки
            right_mark -= 1

        if right_mark < left_mark: #если значение правой метки пересечет значение левой метки, то цикл прерывается
            done = True
        else:
            array[left_mark], array[right_mark] = array[right_mark], array[left_mark]# в противном случае, меняеи местами значания левой и правой метки

    array[low], array[right_mark] = array[right_mark], array[low]# если цикл прерывается, то меняются местами значение опорной точки и правого элемента
    return right_mark


print("Исходный массив: ", array)
result = quick_sort(array)
print("Отсортированный массив:", result)

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

