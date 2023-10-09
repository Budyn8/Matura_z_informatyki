def zadanie_1():
    text = open('./Dane_2305/slowa.txt', 'r').read().split('\n')
    odpowiedz = open('zadanie4_1.txt', 'w')

    for i in text:
        k = 0
        w = 0
        for j in i:
            if j == 'k':
                k += 1
            if j == 'w':
                w += 1
        if w == k:
            odpowiedz.write(i + '\n')


def zadanie_2():
    text = open('./Dane_2305/slowa.txt', 'r').read().split('\n')
    odpowiedz = open('zadanie4_2.txt', 'w')

    for x in text:
        w = 0
        a = 0
        k = 0
        c = 0
        j = 0
        e = 0
        for y in x:
            if y == 'w':
                w += 1
            if y == 'a':
                a += 1
            if y == 'k':
                k += 1
            if y == 'c':
                c += 1
            if y == 'j':
                j += 1
            if y == 'e':
                e += 1
        if a != 0:
            a //= 2
        odp = min(w, a, k, c, j, e)
        odpowiedz.write(str(odp) + ' ')


def zadanie_3():
    text = open('./Dane_2305/przyklad.txt', 'r').read().split('\n')
    odpowiedz = open('zadanie4_3.txt', 'w')

    for x in text:
        if x != '':
            count = 0
            char = ''
            for y in range(0, len(x)):
                if x[y] == 'w' and char == '':
                    char = 'w'

                if x[y] == 'a' and char == 'w':
                    char = 'wa'

                if x[y] == 'k' and char == 'wa':
                    char = 'wak'

                if x[y] == 'a' and char == 'wak':
                    char = 'waka'

                if x[y] == 'c' and char == 'waka':
                    char = 'wakac'

                if x[y] == 'j' and char == 'wakac':
                    char = 'wakacj'

                if x[y] == 'e' and char == 'wakacj':
                    count += 7
                    char = ''

            odp = len(x) - count
            odpowiedz.write(str(odp) + ' ')


if __name__ == '__main__':
    zadanie_1()
    zadanie_2()
    zadanie_3()
    