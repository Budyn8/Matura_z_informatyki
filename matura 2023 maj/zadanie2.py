def przyklad_2():
    wejscie = (open('./Dane_2305/bin.txt')
               .read()
               .split('\n'))

    count = 0
    for line in wejscie:
        if line == '':
            break
        blocks = 1
        before = line[0]
        for i in line:
            if i != before:
                blocks += 1
                before = i
        if blocks <= 2:
            count += 1

    return count


def przyklad_3():
    najwieksza: str = '0'
    max_wielkosc: int = 1

    wejscie = (open('./Dane_2305/bin.txt')
               .read()
               .split('\n'))

    for line in wejscie:
        wielkosc = len(line)
        if max_wielkosc < wielkosc:
            najwieksza = line
            max_wielkosc = wielkosc
            continue
        if max_wielkosc == wielkosc:
            i = 0
            while i < wielkosc:
                if line[i] > najwieksza[i]:
                    najwieksza = line
                    max_wielkosc = wielkosc
                    break
                if line[i] < najwieksza[i]:
                    break
                i += 1

    return najwieksza


def przyklad_5():
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
    print( przyklad_2(), przyklad_3())
    for i in przyklad_5():
        print(i + '\n')
