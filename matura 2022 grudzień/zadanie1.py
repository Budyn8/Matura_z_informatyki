def przyklad_1():
    dane = (open('./Dane_2212/mecz.txt')
            .read())
    anws = 0
    i = len(dane) - 1
    while i > 0:
        if dane[i] != dane[i - 1]:
            anws += 1
        i -= 1
    return anws


def przyklad_2():
    wynik_a = 0
    wynik_b = 0

    dane = (open('./Dane_2212/mecz.txt')
            .read())

    i = len(dane)
    j = 0
    while j < i:
        if wynik_a >= 1000 and wynik_b + 3 < wynik_a:
            return str(wynik_a) + ':' + str(wynik_b)
        elif wynik_b >= 1000 and wynik_a + 3 < wynik_b:
            return str(wynik_a) + ':' + str(wynik_b)
        else:
            if dane[j] == 'A':
                wynik_a += 1
            else:
                wynik_b += 1
        j += 1
    return 'Nikt nie wygrał'


def przyklad_3():

    dobre_passy = 0
    dlugosc_passy = 0
    najdluzsza_dobra_passa = [dlugosc_passy, 'A']
    dane = (open('./Dane_2212/mecz.txt')
            .read())

    i = len(dane) - 1
    j = 0

    while j < i:
        if dane[j] != dane[j + 1]:
            if dlugosc_passy + 1 >= 10:
                dobre_passy += 1
                if najdluzsza_dobra_passa[0] < dlugosc_passy + 1:
                    najdluzsza_dobra_passa = [dlugosc_passy + 1, dane[j]]
            dlugosc_passy = 0
        else:
            dlugosc_passy += 1
        j += 1
    return str(dobre_passy) + ',' + str(najdluzsza_dobra_passa[1]) + ',' + str(najdluzsza_dobra_passa[0])


if __name__ == '__main__':
    print('1.', przyklad_1())
    print('2.', przyklad_2())
    print('3.', przyklad_3())
