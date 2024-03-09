if __name__ == '__main__':
    n: int = 245

    b = 0
    memo = 0

    while n > 0:
        if n%2 != memo:
            b+=1
            memo=n%2
        n = (n-memo)/2

    print( b )