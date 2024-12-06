# -- Coding UTF-8 --

while True:
    try:
        N = int(input('Введите размер матрицы (N): '))
        if N > 0:
            break
        else:
            print('Ошибка: размер матрицы должен быть положительным числом.')
    except ValueError:
        print('Ошибка: введите целое число.')

A = []

for i in range(N):
    while True:
        row_input = input(f'Введите {i+1}-ю строку по {N} элемента(ов), разделяя элементы пробелом:\n')
        elements = row_input.split()

        if len(elements) == N:
            try:
                row = list(map(int, elements))
                A.append(row)
                break
            except ValueError:
                print('Ошибка: все элементы должны быть целыми числами.')
        else:
            print(f'Ошибка: должно быть введено {N} элемента(ов).')

for i in range(N):
    for j in range(N):
        if A[i][j] > 0:
            A[i][j] = 1
        elif A[i][j] < 0:
            A[i][j] = 0

print('\nПреобразованная матрица:')
for row in A:
    print(' '.join(map(str, row)))