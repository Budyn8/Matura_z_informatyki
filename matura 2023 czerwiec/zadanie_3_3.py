import script_functions as af


def main( zawartosc_pliku ):
    max_ruznica_liczb = ""

    indeks = 0

    while indeks < len(zawartosc_pliku) - 2:
        liczba_1 = zawartosc_pliku[indeks]
        liczba_2 = zawartosc_pliku[indeks + 1]
        indeks_l = 0
        ruznica_liczb = ""

        while len(liczba_2) > indeks_l:
            if indeks_l >= len(liczba_1):
                while indeks_l < len(liczba_2):
                    ruznica_liczb += "0"

            if indeks_l >= len(liczba_2):
                while indeks_l < len(liczba_1):
                    ruznica_liczb += "0"


