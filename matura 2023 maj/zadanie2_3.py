def main():

    najwieksza: str = '0'
    max_wielkosc: int = 1

    wejscie = (open( './Dane_2305/bin.txt' )
               .read()
               .split('\n'))

    for line in wejscie:
        wielkosc = len( line )
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
                i+=1

    return najwieksza


if __name__ == '__main__':
    print(main())