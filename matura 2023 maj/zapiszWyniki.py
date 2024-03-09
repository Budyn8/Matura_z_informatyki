import zadanie2
import zadanie3


if __name__ == '__main__':
    wyniki2 = open('./wyniki2.txt', 'w')

    wyniki2.write("2.\t" + str(zadanie2.przyklad_2()) + "\n3.\t" + str(zadanie2.przyklad_3()))
    wyniki2.close()

    odp = (open('./wynik2_5.txt', 'w'))
    for i in zadanie2.przyklad_5():
        odp.write( i + '\n' )
    odp.close()

    wyniki3 = open('./wyniki3.txt', 'w')

    wyniki3.write(
        "1.\t" + str(zadanie3.przyklad_1()) +
        "\n2.\t" + zadanie3.przyklad_2() +
        "\n3.\t" + str(zadanie3.przyklad_3()) +
        "\n4.\t" + zadanie3.przyklad_4()
    )
    wyniki3.close()
