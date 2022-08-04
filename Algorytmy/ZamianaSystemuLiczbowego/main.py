def from_decimal_to_any(n, p):
    if n > 0:
        from_decimal_to_any(n // p, p)
        if n % p > 9:
            if n % p == 10:
                print('A')
            if n % p == 11:
                print('B')
            if n % p == 12:
                print('C')
            if n % p == 13:
                print('D')
            if n % p == 14:
                print('E')
            if n % p == 15:
                print('F')
        else:
            print(n % p)

if __name__ == '__main__':
    n = int(input("Podaj liczbę systemu: "))
    p = int(input("Podaj podstawę systemu: "))
    print(f"Liczba {n} w sytemie {p}: ")

    if n == 0:
        print(0)
    else:
        from_decimal_to_any(n, p)
