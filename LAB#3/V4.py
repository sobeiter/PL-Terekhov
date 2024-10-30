# -- Coding: UTF-8 --
def el():
    a = int(input('Расстояние между рядами: '))
    b = int(input('Расстояние между отверстиями в ряду: '))
    l = int(input('Длина свободного конца шнурка: '))
    N = int(input('Количество отверстий в ряду: '))

    if N > 1:
        length = 2*l+(a+b)*((2*N)-2)+a
    else:
        length = 2*l+a
    return length
    
print('-- Итоговая длина шнурка:', el())
