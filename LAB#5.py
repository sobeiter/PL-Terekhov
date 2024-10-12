# -- Coding: UTF-8 --
x = float(input('Расстояние X (км): '))
y = float(input('Расстояние Y (км): '))

def day(x, y):
    d = 1
    while x < y:
        x += x/10
        d += 1
    return d

print('Номер дня:', day(x, y))