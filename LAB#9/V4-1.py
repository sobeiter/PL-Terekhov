# -- Coding UTF-8 --

import random # Для разнообразия, вместо ручного ввода :>

a = int(input("Введите количество строк: "))
b = int(input("Введите количество столбцов: "))

matrix = [[random.randint(1, 100) for _ in range(b)] for _ in range(a)]

print("Исходная матрица:")
for row in matrix:
    print(row)

row_sums = [sum(row) for row in matrix]

max_index = row_sums.index(max(row_sums))
min_index = row_sums.index(min(row_sums))

print(f'\nСтрока с наибольшей суммой: {max_index+1} | {matrix[max_index]}')
print(f'Сумма элементов:', row_sums[max_index])

print(f'\nСтрока с наименьшей суммой: {min_index+1} | {matrix[min_index]}')
print(f'Сумма элементов: {row_sums[min_index]}')
