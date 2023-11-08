def podpunkt_1(file_lines):

    balanced = [0, 0]

    for line in file_lines:
        if line == '':
            continue
        count = [0, 0]

        for num in line:
            count[int(num)] += 1

        balance = count[0] - count[1]

        if balance < 0:
            balance *= -1

        if balance < 2:
            balanced[balance] += 1

    return balanced

def podpunkt_2(file_content):

    liczby = []
    max_lenght = 0

    for line in file_content:

        lenght = len(line)

        if lenght > max_lenght:
            max_lenght = lenght
            liczby = [line]
            continue

        liczby += line

    return 0


if __name__ == '__main__':

    dane = open("./DANE_E/anagram.txt", 'r')

    if dane:
        text = dane.read()
        text = text.split('\n')
        wynikf = open('./wynik3.txt', 'w')
        wynik = podpunkt_1(text)
        wynikf.write(str(wynik[0]) + " " + str(wynik[1]))
