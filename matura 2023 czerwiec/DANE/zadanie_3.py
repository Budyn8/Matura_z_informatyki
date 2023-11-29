def check_balance(line):
    count = [0, 0]

    for num in line:
        count[int(num)] += 1

    balance = count[0] - count[1]

    if balance < 0:
        balance *= -1

    return balance


def podpunkt_1(file_lines):

    balanced = [0, 0]

    for line in file_lines:
        if line == '':
            continue

        balance = check_balance(line)

        if balance < 2:
            balanced[balance] += 1

    return balanced


def podpunkt_2(file_content):

    liczby = []

    for line in file_content:

        lenght = len(line)

        if lenght == 8 and check_balance(line) < 2:
            liczby.append(line)

    return liczby


if __name__ == '__main__':

    dane = open("./DANE_E/przyklad.txt", 'r')

    if dane:
        text = dane.read()
        text = text.split('\n')

        wynikf = open('./wynik3.txt', 'w')

        wynik_1 = podpunkt_1(text)
        wynik_2 = podpunkt_2(text)
