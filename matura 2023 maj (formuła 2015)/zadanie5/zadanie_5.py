import datetime


def zadanie_3():
    text = open('./Dane_2305/owoce.txt', 'r').read().split('\n')

    malina = owoc()
    truskawka = owoc()
    porzeczka = owoc()

    for i in text:
        if 'data' not in i and i != '':
            dane = i.split('\t')
            date = dane[0].split('.')
            data = datetime.date(int(date[2]), int(date[1]), int(date[0]))

            maliny = int(dane[1])
            truskawki = int(dane[2])
            porzeczki = int(dane[3])

            check_if(malina, maliny)
            check_if(truskawka, truskawki)
            check_if(porzeczka, porzeczki)

            pop_liczba_porzeczek = porzeczki

    print(f'maliny: {malina.max}\ntruskawki: {truskawka.max}\nporzeczki: {truskawka.max}')


def check_if(clasa, owoc):
    if clasa.pop_liczba < owoc:
        clasa.count += 1
    else:
        if clasa.count > clasa.max:
            clasa.max = clasa.count
            clasa.count = 0

    clasa.pop_liczba = owoc


class owoc:
    def __init__(self):
        self.count = 0
        self.pop_liczba = 0
        self.max = 0


def zadanie_4():
    pop_dzien = {
        'maliny' : 0,
        'truskawki' : 0,
        'porzeczki' : 0
    }

    p_m = 0
    m_t = 0
    t_p = 0

    for i in open('./Dane_2305/owoce.txt'):
        if 'data' not in i and i != '':
            text = i.strip('\n').split('\t')

            maliny = int(text[1])
            truskawki = int(text[2])
            porzeczki = int(text[3])

            pop_dzien['maliny'] += maliny
            pop_dzien['truskawki'] += truskawki
            pop_dzien['porzeczki'] += porzeczki

            min_owoc = min(pop_dzien, key=pop_dzien.get)

            if min_owoc == 'porzeczki':
                m_t += 1
                min_przetwor = min(pop_dzien['maliny'], pop_dzien['truskawki'])
                pop_dzien['maliny'] -= min_przetwor
                pop_dzien['truskawki'] -= min_przetwor

            if min_owoc == 'maliny':
                t_p += 1
                min_przetwor = min(pop_dzien['porzeczki'], pop_dzien['truskawki'])
                pop_dzien['porzeczki'] -= min_przetwor
                pop_dzien['truskawki'] -= min_przetwor

            if min_owoc == 'truskawki':
                p_m += 1
                min_przetwor = min(pop_dzien['maliny'], pop_dzien['porzeczki'])
                pop_dzien['maliny'] -= min_przetwor
                pop_dzien['porzeczki'] -= min_przetwor

    print(p_m, t_p, m_t)


def zadanie_5():
    pop_dzien = {
        'maliny': 0,
        'truskawki': 0,
        'porzeczki': 0
    }

    p_m = 0
    m_t = 0
    t_p = 0

    for i in open('./Dane_2305/owoce.txt'):
        if 'data' not in i and i != '':
            text = i.strip('\n').split('\t')

            maliny = int(text[1])
            truskawki = int(text[2])
            porzeczki = int(text[3])

            pop_dzien['maliny'] += maliny
            pop_dzien['truskawki'] += truskawki
            pop_dzien['porzeczki'] += porzeczki

            min_owoc = min(pop_dzien, key=pop_dzien.get)

            if min_owoc == 'porzeczki':
                min_przetwor = min(pop_dzien['maliny'], pop_dzien['truskawki'])
                m_t += min_przetwor
                pop_dzien['maliny'] -= min_przetwor
                pop_dzien['truskawki'] -= min_przetwor

            if min_owoc == 'maliny':
                min_przetwor = min(pop_dzien['porzeczki'], pop_dzien['truskawki'])
                t_p += min_przetwor
                pop_dzien['porzeczki'] -= min_przetwor
                pop_dzien['truskawki'] -= min_przetwor

            if min_owoc == 'truskawki':
                min_przetwor = min(pop_dzien['maliny'], pop_dzien['porzeczki'])
                p_m += min_przetwor
                pop_dzien['maliny'] -= min_przetwor
                pop_dzien['porzeczki'] -= min_przetwor

    print(p_m, t_p, m_t)


if __name__ == '__main__':
    zadanie_3()
    zadanie_4()
    zadanie_5()
