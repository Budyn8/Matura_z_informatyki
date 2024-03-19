if __name__ == '__main__':
    n = 2021  # input
    d = 0
    i = 1

    while n > 0:
        d += (9 - (n % 10)) * i
        n = int(n / 10)
        i *= 10

    print(d)
