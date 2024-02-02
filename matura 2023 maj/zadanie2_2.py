def main():
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


if __name__ == '__main__':
    print(main())