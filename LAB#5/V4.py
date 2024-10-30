# -- Coding: UTF-8 --
x = float(input('Введите расстояние X (км): '))
y = float(input('Введите расстояние Y (км): '))

def day(x, y):
    d = 1
    while x < y:
        x += x/10
        d += 1
    return d

print('Номер дня:', day(x, y))
