def jest_polaczony(x, y):
    if x*2 == y or x*2 + 1 == y:
        return True
    if x > y:
        return False
    return jest_polaczony(x*2, y) or jest_polaczony(x*2 + 1, y)


def main():
    dane = (open('./Dane_2212/pary.txt')
            .read()
            .split('\n'))
    for para in dane:
        if para != '':
            liczby = para.split(' ')
            if jest_polaczony(int(liczby[0]), int(liczby[1])):
                print(liczby[0], liczby[1])


if __name__ == '__main__':
    main()
