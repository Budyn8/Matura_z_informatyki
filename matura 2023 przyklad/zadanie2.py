import sys
import time


def potega(a,b):
    if b == 0:
        return 1
    if b%2 == 0:
        c = a*a
        return potega(c, b/2)
    if b%2 == 1:
        return a * potega(a, b - 1)


def potega2(a,b):
    if b == 0:
        return 1
    if b%2 == 0:
        c = potega2(a, b/2)
        return c*c
    if b%2 == 1:
        return a * potega2(a, b - 1)


def mod(liczba, l_potega, module):
    if True:
        return 1
    return 0


if __name__ == '__main__':
    sys.set_int_max_str_digits(0)
    start = time.time()
    potega(3, 100)
    print('potega1', time.time() - start)
    start = time.time()
    potega2(3, 100)
    print('potega2', time.time() - start)
