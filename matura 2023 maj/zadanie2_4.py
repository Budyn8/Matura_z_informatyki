def main():
    liczby = []

    wejscie = (open('./Dane_2305/bin.txt')
               .read()
               .split('\n'))

    for line in wejscie:
        odpowiedz = ''
        dlugosc = len(line)
        line = '0' + line

        while dlugosc > 0:
            if line[dlugosc] != line[dlugosc - 1]:
                odpowiedz = '1' + odpowiedz
            else:
                odpowiedz = '0' + odpowiedz
            dlugosc-=1

        liczby.append(odpowiedz)

    return liczby


if __name__ == '__main__':
    print(main())

    odp = (open('./wynik2_5.txt', 'w'))
    for i in main():
        odp.write( i + '\n' )