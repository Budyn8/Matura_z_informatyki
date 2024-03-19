import sys
import time

if __name__ == '__main__':
    n = 23125454312  # input
    dl = 0

    m = 1
    while n > m * m:
        m += 1

    while n > 0:
        if m * m > n:
            m -= 1
        else:
            dl += 1
            n -= m * m

    print(dl)

