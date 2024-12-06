# -- Coding UTF-8 --

import math

def check(x, y, center_x, center_y, rad):
    dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
    if dist < rad:
        print(f'Точка ({x}, {y}) лежит внутри окружности')
    else:
        print(f'Точка ({x}, {y}) лежит вне окружности')

center_x = float(input('Введите координату X центра окружности: '))
center_y = float(input('Введите координату Y центра окружности: '))
rad = float(input('Введите радиус окружности: '))
p1 = float(input('Введите координату X точки P: '))
p2 = float(input('Введите координату Y точки P: '))
f1 = float(input('Введите координату X точки F: '))
f2 = float(input('Введите координату Y точки F: '))
l1 = float(input('Введите координату X точки L: '))
l2 = float(input('Введите координату Y точки L: '))

count = 0
if check(p1, p2, center_x, center_y, rad):
    count += 1
if check(f1, f2, center_x, center_y, rad):
    count += 1
if check(l1, l2, center_x, center_y, rad):
    count += 1

check(p1, p2, center_x, center_y, rad)
check(f1, f2, center_x, center_y, rad)
check(l1, l2, center_x, center_y, rad)

print(f'Количество точек, лежащих внутри окружности: {count}.')