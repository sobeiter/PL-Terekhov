# -- Coding UTF-8 --

q = list(map(int, input('Введите элементы массива через пробел: ').split()))
odd = [x for x in q if x%2 != 0]

if odd:
    print('Отсортированный массив нечётных чисел:', *reversed(odd))
else:
    print('Нечётных чисел в массиве нет')