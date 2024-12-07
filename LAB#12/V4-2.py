# -- Coding UTF-8 --

import math

def prime(n, d=2):
    if d*d > n:
        return 'YES'
    
    if n%d == 0:
        return 'NO'
    
    return prime(n, d+1)

n = int(input('Ведите натуральное число: '))
print(prime(n))