def check_balance(line):
    count = [0, 0]

    for num in line:
        count[int(num)] += 1

    balance = count[0] - count[1]

    if balance < 0:
        balance *= -1

    return balance


if __name__ == "__main__":
    print(check_balance("100110"))
