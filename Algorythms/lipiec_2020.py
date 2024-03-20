def odejmij_ulamek(p, q, ulamek):
    licznik = p*ulamek - q
    mianownik = q*ulamek
    # if mianownik/licznik % 1 == 0.0:
    #     mianownik /= licznik
    #     licznik = 1
    return [licznik, int(mianownik)]


# def zapis_egipski(p, q):
#     if q/p % 1 == 0:
#         return [int(q/p)]
#     ulamek_egipski = int(q/p) + 1
#     wynik = odejmij_ulamek(p, q, ulamek_egipski)
#
#     return [ulamek_egipski] + zapis_egipski(wynik[0], wynik[1])

def zapis_egipski(p, q):
    if p > 0:
        ulamek = (q/p).__ceil__()
        print(ulamek)
        wynik = odejmij_ulamek(p, q, ulamek)
        zapis_egipski(wynik[0], wynik[1])


def zapis_egipski_odp(p, q):
    if p > 0:
        ulamek = (q/p).__ceil__()
        print(ulamek)
        zapis_egipski_odp(p*ulamek - q, q*ulamek)


if __name__ == '__main__':
    zapis_egipski(8, 15)
