import script_functions as af


def main( zawartosc_pliku ):
    balanced = [0, 0]

    for line in zawartosc_pliku :
        if line == '':
            continue

        balance = af.check_balance(line)

        if balance < 2:
            balanced[balance] += 1

    return balanced


if __name__ == "__main__":
    dane = open("./DANE_E/przyklad.txt", 'r')
    if dane:
        tekst = dane.read()
        tekst = tekst.split('\n')

        print(main(tekst))
