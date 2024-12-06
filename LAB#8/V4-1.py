# -- Coding UTF-8 --

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def input_natural(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print('Ошибка: введите положительное число.')
            else:
                return value
        except ValueError:
            print('Ошибка: некорректный ввод.')

A = input_natural('Введите числитель первой дроби (A): ')
B = input_natural('Введите знаменатель первой дроби (B): ')
C = input_natural('Введите числитель второй дроби (C): ')
D = input_natural('Введите знаменатель второй дроби (D): ')

numerator = A * D
denominator = B * C

g = gcd(numerator, denominator)

if g > 1:
    numerator //= g
    denominator //= g

print(f'{numerator}/{denominator}')
