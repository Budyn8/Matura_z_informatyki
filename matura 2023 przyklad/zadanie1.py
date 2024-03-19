def podpunkt_1():
    plansze = (open('./Dane_2203/szachy.txt', 'r')
               .read()
               .split('\n\n')
               )
    ilosc_pustych_kolumn_max = 0
    plansze_z_puste_kolumny = 0
    for as_plansza in plansze:
        if as_plansza == '':
            continue
        plansza = as_plansza.split('\n')
        puste_kolumny = ['.', '.', '.', '.', '.', '.', '.', '.']
        for wiersz in plansza:
            if wiersz == '':
                continue
            i = 0
            while i < 8:
                if wiersz[i] != '.' or puste_kolumny[i] != '.':
                    puste_kolumny[i] = 'A'
                i += 1
        ilosc_pustych_kolumn = puste_kolumny.count('.')
        if ilosc_pustych_kolumn != 0:
            plansze_z_puste_kolumny += 1
            if ilosc_pustych_kolumn > ilosc_pustych_kolumn_max:
                ilosc_pustych_kolumn_max = ilosc_pustych_kolumn

    return str(plansze_z_puste_kolumny) + ', ' + str(ilosc_pustych_kolumn_max)


def podpunkt_2():
    plansze = (open('./Dane_2203/szachy.txt', 'r')
               .read()
               .split('\n\n')
               )

    ilosc_rownowag = 0
    min_ilosc_bierek_na_planszy = 32

    for as_plansza in plansze:
        if as_plansza == '':
            continue
        plansza = as_plansza.split('\n')
        bierki = {
            'w' : 0,
            's' : 0,
            'g' : 0,
            'h' : 0,
            'k' : 0,
            'p' : 0
        }
        ilosc_bierek_na_planszy = 0
        for wiersz in plansza:
            if wiersz == '':
                continue
            i = 0
            while i < 8:
                if wiersz[i] != '.':
                    ilosc_bierek_na_planszy += 1
                if wiersz[i].islower():
                    bierki[wiersz[i]] += 1
                elif wiersz[i].isupper():
                    bierki[wiersz[i].lower()] -= 1
                i += 1

        rownowaga = True
        for bierka in bierki:
            if bierki[bierka] != 0:
                rownowaga = False

        if rownowaga:
            ilosc_rownowag += 1
            if min_ilosc_bierek_na_planszy > ilosc_bierek_na_planszy:
                min_ilosc_bierek_na_planszy = ilosc_bierek_na_planszy

    return str(ilosc_rownowag) + ', ' + str(min_ilosc_bierek_na_planszy)


def podpunkt_3():
    plansze = (open('./Dane_2203/szachy.txt', 'r')
               .read()
               .split('\n\n')
               )

    biala_czarnego = 0
    czarna_bialego = 0

    for as_plansza in plansze:
        if as_plansza == '':
            continue
        wiersze = as_plansza.split('\n')
        kolumny = ['', '', '', '', '', '', '', '']

        wk_nie_w_wierszu = True

        for wiersz in wiersze:
            if wiersz == '':
                continue
            i = 0
            while i < 8:
                kolumny[i] += wiersz[i]
                i += 1

        for wiersz in wiersze:
            bierki_w_wierszu = wiersz.replace('.', '')
            if 'Kw' in bierki_w_wierszu or 'wK' in bierki_w_wierszu:
                wk_nie_w_wierszu = False
                czarna_bialego += 1
                break
            if 'kW' in bierki_w_wierszu or 'Wk' in bierki_w_wierszu:
                wk_nie_w_wierszu = False
                biala_czarnego += 1
                break
        if wk_nie_w_wierszu:
            for kolumna in kolumny:
                bierki_w_kolumnie = kolumna.replace('.', '')
                if 'Kw' in bierki_w_kolumnie or 'wK' in bierki_w_kolumnie:
                    czarna_bialego += 1
                    break
                if 'kW' in bierki_w_kolumnie or 'Wk' in bierki_w_kolumnie:
                    biala_czarnego += 1
                    break
    return str(biala_czarnego) + ', ' + str(czarna_bialego)


if __name__ == '__main__':
    print(podpunkt_3())
