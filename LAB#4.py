# -- Coding: UTF-8 --
def main():
    s = 0
    n = int(input('Введите количество чисел: '))
    for i in range(n):
        a = int(input(f'Введите число №{i+1}: '))
        s += a
    return s
print(main())