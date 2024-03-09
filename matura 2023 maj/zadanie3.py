def przyklad_1():
    pi = (open('./Dane_2305/pi.txt')
          .read()
          .split('\n'))
    dlugosc = len(pi) - 1
    i = 0
    count = 0
    while i < dlugosc:
        if int(pi[i] + pi[i + 1]) > 90:
            count += 1
        i += 1
    return count


def przyklad_2():
    pi = (open('./Dane_2305/pi.txt')
          .read()
          .split('\n'))
    counter = []
    dlugosc = len(pi) - 1

    for i in range(0, 100):
        counter.append(0)

    i = 0
    while i < dlugosc:
        counter[int(pi[i] + pi[i + 1])] += 1
        i += 1

    i = 0
    max_val = 0
    max_num = 0

    min_val = 0
    min_num = 0

    while i < 100:
        if counter[i] > max_num:
            max_val = i
            max_num = counter[i]
        if counter[i] < min_num:
            min_val = i
            min_num = counter[i]
        i += 1

    if max_val < 10:
        max_val = '0' + str(max_val)
    if min_val < 10:
        min_val = '0' + str(min_val)

    return str(min_val) + " " + str(min_num) + "\n\t" + str(max_val) + " " + str(max_num)


def przyklad_3():
    pi = (open("./Dane_2305/pi.txt", 'r')
          .read()
          .split('\n'))

    count = 0
    dlugosc = len(pi) - 6
    i = 0

    while i < dlugosc:
        rosnaca = True
        malejaca = False
        rosnaca_malejaca = True
        for j in range(0, 5):
            if rosnaca and pi[i + j] > pi[i + j + 1]:
                malejaca = True
            if malejaca and pi[i + j] < pi[i + j + 1]:
                rosnaca_malejaca = False
                break
        if rosnaca_malejaca:
            count += 1
        i += 1

    return count


def przyklad_4():
    pi = (open('./Dane_2305/pi.txt')
          .read()
          .split('\n'))

    dlugosc = 0
    index = 0

    max_dlugosc = 0
    max_index = 0

    dlugosc_pi = len(pi) - 2
    i = 0
    rosnacy = True
    malejacy = False

    while i < dlugosc_pi:
        dlugosc += 1

        if rosnacy and pi[i] > pi[i + 1]:
            malejacy = True
            rosnacy = False

        if malejacy and pi[i] < pi[i + 1]:
            malejacy = False
            rosnacy = True
            if max_dlugosc < dlugosc:
                max_index = index
                max_dlugosc = dlugosc
            dlugosc = 0
            index = i
            i -= 1
        i += 1
    return str(max_dlugosc) + "\n\t" + ''.join(pi[max_index:max_index + max_dlugosc])


if __name__ == '__main__':
    print( przyklad_1(), przyklad_2(), przyklad_3(), przyklad_4() )
