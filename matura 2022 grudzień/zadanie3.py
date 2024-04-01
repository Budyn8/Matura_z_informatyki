LICZBY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def liczby_pierwsze(x):
    pierwsze = [False, False]
    i = 2
    while i < x:
        pierwsze.append(True)
        i += 1
    i = 2
    while i < x:
        if pierwsze[i]:
            j = i + i
            while j < x:
                pierwsze[j] = False
                j += i
        i += 1
    return pierwsze


def zapis_szesnastkowy(x):
    if x < 16:
        return LICZBY[x]
    y = x % 16
    return LICZBY[y] + zapis_szesnastkowy(int((x - y) / 16))


def podpunkt_2():
    liczba_pierwszych = 0
    dane = open('./Dane_2212/liczby.txt').read().split('\n')
    pierwsze = liczby_pierwsze(1000001)
    for liczba in dane:
        if liczba != '':
            if pierwsze[int(liczba) - 1]:
                liczba_pierwszych += 1
    return liczba_pierwszych


def podpunkt_3():
    anws = [0, 0, 0, 1000000]
    p_pierwsze = []
    i = 1000001
    j = 0
    pierwsze = liczby_pierwsze(i)
    while j < i:
        if pierwsze[j]:
            p_pierwsze.append(j)
        j += 1
    dane = open('./Dane_2212/liczby.txt').read().split('\n')
    dane.pop(len(dane) - 1)

    for liczba in dane:
        liczba = int(liczba)
        p_index = 0
        count = 0
        while liczba > p_pierwsze[p_index]:
            if pierwsze[liczba - p_pierwsze[p_index]]:
                count += 1
            p_index += 1

        if count % 2 == 0:
            count /= 2
        else:
            count = (count + 1) / 2

        if count > anws[1]:
            anws[0] = liczba
            anws[1] = int(count)
        elif count < anws[3]:
            anws[2] = liczba
            anws[3] = int(count)
    return anws


def podpunkt_4():
    dane = open('./Dane_2212/liczby.txt').read().split('\n')
    dane.pop(len(dane) - 1)
    liczby_anws = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0
    }

    for i in dane:
        szesnastkowo = zapis_szesnastkowy(int(i))
        j = len(szesnastkowo)
        while j > 0:
            liczby_anws[szesnastkowo[j - 1]] += 1
            j -= 1
    return liczby_anws


if __name__ == '__main__':
    odp = podpunkt_2()
    print('2.\t', odp)
    odp = podpunkt_3()
    print('3.\t', odp[0], odp[1], odp[2], odp[3])
    odp = podpunkt_4()
    print('4.')
    for a in odp:
        print(a, ':', odp[a])
