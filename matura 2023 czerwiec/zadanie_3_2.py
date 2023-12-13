import script_functions as af


def main(zawartosc_pliku ):
    liczby = []

    for line in zawartosc_pliku :

        lenght = len(line)

        if lenght == 8 and af.check_balance(line) < 2:
            liczby.append(line)

    return liczby


if __name__ == "__main__":
    dane = open("./DANE_E/przyklad.txt", 'r')
    if dane:
        tekst = dane.read()
        tekst = tekst.split('\n')

        print(main(tekst))
