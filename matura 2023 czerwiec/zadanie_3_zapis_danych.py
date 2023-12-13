from zadanie_3_1 import main as podpunkt_1
from zadanie_3_2 import main as podpunkt_2


if __name__ == '__main__':

    dane = open("./DANE_E/przyklad.txt", 'r')

    if dane:
        tekst = dane.read()
        tekst = tekst.split('\n')

        plik_z_wynikiem = open('./wynik3.txt', 'w')

        wynik_1 = podpunkt_1(tekst)
        wynik_2 = podpunkt_2(tekst)

        wynik = '3.1\n\n'
        for index in wynik_1:
            wynik += str(index) + '\t'
        wynik += '\n\n3.2\n\n'
        for index in wynik_2:
            wynik += str(index) + '\t'

        plik_z_wynikiem.write(wynik)
