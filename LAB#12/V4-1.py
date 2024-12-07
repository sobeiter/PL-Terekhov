# -- Coding UTF-8 --

def sum(N):
    if N < 10:
        return N
    else:
        return N % 10 + sum(N // 10)

N = int(input('Введите натуральное число: '))
result = sum(N)
print(f'Сумма цифр числа {N} равна {result}')
