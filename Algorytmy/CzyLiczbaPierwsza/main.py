from math import sqrt
def czyPierwsza(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = -1
    if czyPierwsza(n):
        print("Liczba", n, "jest pierwsza.")
    else:
        print("Liczba", n, "nie jest pierwsza.")
