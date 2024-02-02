if __name__ == '__main__':
    number: int = 67

    odpowiedz = 1
    before = number%2
    number = (number - before)/2

    while number > 0 :
        temp = number%2
        if before != temp:
            odpowiedz += 1
            before = temp
        number = (number - temp)/2

    print( odpowiedz )