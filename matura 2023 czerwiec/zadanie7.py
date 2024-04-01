import datetime


def podpunkt_1():
    instalacje_array = (open('DANE/DANE_M/instalacje.txt', 'r')
                        .read()
                        .split('\n'))

    urzadzenia_array = (open('DANE/DANE_M/urzadzenia.txt', 'r')
                        .read()
                        .split('\n'))

    urzadzenia = {}
    instalacje = []

    i = len(instalacje_array) - 2
    while i > 0:
        instalacje.append(instalacje_array[i].split('\t'))
        i -= 1

    i = len(urzadzenia_array) - 2
    while i > 0:
        info = urzadzenia_array[i].split('\t')
        urzadzenia[info[0]] = info[3]
        i -= 1

    typy = {
        'Tablet': 0,
        'Phone': 0,
        'PC': 0
    }

    for i in instalacje:
        typy[urzadzenia[i[2]]] += 1

    return typy


def podpunkt_2():
    instalacje_array = (open('DANE/DANE_M/instalacje.txt', 'r')
                        .read()
                        .split('\n'))
    urzadzenia_array = (open('DANE/DANE_M/urzadzenia.txt', 'r')
                        .read()
                        .split('\n'))

    instalacje = []
    i = len(instalacje_array) - 2
    while i > 0:
        info = instalacje_array[i].split('\t')
        date = info[0].split('.')
        if date[2] == '2019' and date[1] == '02':
            instalacje.append(info[2])
        i -= 1

    urzadzenia = {}
    i = len(urzadzenia_array) - 2
    while i > 0:
        info = urzadzenia_array[i].split('\t')
        urzadzenia[info[0]] = info[2]
        i -= 1

    producenci = {}
    for i in instalacje:
        if urzadzenia[i] in producenci.keys():
            producenci[urzadzenia[i]] += 1
        else:
            producenci[urzadzenia[i]] = 1

    najwiecej_pobran = ['', 0]
    for i in producenci:
        if producenci[i] > najwiecej_pobran[1]:
            najwiecej_pobran = [i, producenci[i]]

    return najwiecej_pobran


def podpunkt_3():
    instalacje_array = (open('DANE/DANE_M/instalacje.txt', 'r')
                        .read()
                        .split('\n'))

    kraje_array = (open('DANE/DANE_M/kraje.txt', 'r')
                   .read()
                   .split('\n'))

    instalacje = {}
    i = len(instalacje_array) - 2
    while i > 0:
        info = instalacje_array[i].split('\t')
        if info[1] in instalacje.keys():
            instalacje[info[1]] += 1
        else:
            instalacje[info[1]] = 1
        i -= 1

    kraje = {}
    i = len(kraje_array) - 2
    while i > 0:
        info = kraje_array[i].split('\t')
        if int(info[2]) >= 1000000:
            kraje[info[0]] = [info[1], int(info[2])]
        i -= 1

    instalacje_na_osoby = {}
    for i in kraje:
        instalacje_na_osoby[kraje[i][0]] = (instalacje[i]*1000000)/kraje[i][1]

    top_piec = []
    for i in instalacje_na_osoby:
        if len(top_piec) != 6:
            top_piec.append([i, instalacje_na_osoby[i]])
        else:
            j = 4
            while j >= 0:
                if instalacje_na_osoby[i] > top_piec[j][1]:
                    temp = top_piec[j]
                    top_piec[j] = [i, instalacje_na_osoby[i]]
                    top_piec[j + 1] = temp
                    j -= 1
                else:
                    break
    return top_piec


def podpunkt_4():
    return 1


if __name__ == '__main__':
    anws = podpunkt_3()[0:5]
    for i in anws:
        print(i[0], i[1].__round__(2))
