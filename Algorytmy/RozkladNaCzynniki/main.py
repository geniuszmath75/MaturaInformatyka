from math import sqrt
def factors():
    k = 2
    print("Podaj liczbe: ")
    n = int(input())
    print(f'Czynniki pierwsze liczby {n}:')
    while n > 1 and k <= int(sqrt(n)):
        while n % k == 0:
            print(f'{k} ')
            n /= k
        k += 1

factors()



