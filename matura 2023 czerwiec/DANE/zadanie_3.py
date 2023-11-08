def podpunkt1():

    dane = open("./DANE_E/anagram.txt", 'r')
    text = dane.read()

    linije = text.split('\n')
    zrownowarzona = [0, 0]

    for linija in linije:
        if linija == '':
            continue
        count = [0, 0]

        for num in linija:
            count[int(num)] += 1

        rownowaga = count[0] - count[1]

        if rownowaga < 0:
            rownowaga *= -1

        if rownowaga < 2:
            zrownowarzona[rownowaga] += 1

    return zrownowarzona


if __name__ == '__main__':
    wynikf = open('./wynik3.txt', 'w')
    wynik = podpunkt1()
    wynikf.write(str(wynik[0]) + " " + str(wynik[1]))