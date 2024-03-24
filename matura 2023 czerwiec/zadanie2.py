def czy_mniejszy(n, s, k1, k2):
    i = k1 - 1
    j = k2 - 1
    while j < n and i < n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return True
            else:
                return False

    if j < n:
        return True
    else:
        return False


def podpunkt_2():
    anws = open('./wynik2_2.txt', 'w')
    for i in range(1, 4):
        file = (open('./DANE/DANE_M/slowa' + str(i) + '.txt', 'r')
                .read()
                .split('\n'))
        file[2] = file[2].split(' ')
        if czy_mniejszy(int(file[0]) - 1, file[1], int(file[2][0]), int(file[2][1])):
            print('Tak')
            anws.write('Tak\n')
        else:
            print('Nie')
            anws.write('Nie\n')
    anws.close()


def podpunkt_3():
    slowo = 'kalafiorowa'
    n = len(slowo)
    T = [n]
    i = 1
    while i < n:
        k = 0
        j = len(T)
        while k < j:
            if czy_mniejszy(n, slowo, i, T[k]):
                T.insert(k, i)  # cant use that
                break
            if k + 1 == j:
                T.append(i)  # cant use that
            k += 1
        i += 1
    return T


def podpunkt_4():
    file = (open('./DANE/DANE_M/sufiks_4.txt', 'r')
            .read()
            .split('\n'))

    for line in file:
        values = line.split(' ')
        j = int(values[0])
        word = values[1]
        while j > 0:
            if czy_mniejszy(1,1,1,1):
                True
    return 1


if __name__ == '__main__':
    print(podpunkt_3())
