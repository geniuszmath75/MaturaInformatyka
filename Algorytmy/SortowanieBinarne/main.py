def wypisz(tab):
    for x in tab:
        print(x, end=", ")


def binary_search(tab, element, left, r):
    print(f"Podtablica o indeksach l={left} i r={r}")
    if left >= r:
        if element >= tab[left]:
            print(f"ZNALEZIENIE NOWEJ POZYCJI = {left + 1}")
            return left + 1
        else:
            print(f"ZNALEZIENIE NOWEJ POZYCJI = {left}")
            return left
    sr = int((left + r) / 2)
    if tab[sr] == element:
        print(f"ZNALEZIENIE NOWEJ POZYCJI = {left + 1}")
        return left + 1
    if tab[sr] < element:
        return binary_search(tab, element, sr + 1, r)
    else:
        return binary_search(tab, element, left, sr - 1)


def sortuj_bin(tab, n):
    for x in range(1, n):
        element = tab[x]
        y = x - 1
        print("\nRozpoczęcie wyszukiwania binarnego nowej")
        print(f"pozycji dla elementu o wartości = {element}")
        pos = binary_search(tab, element, 0, y)
        while y >= pos:
            tab[y + 1] = tab[y]
            y -= 1
        if x != y + 1:
            print(f"\nKrok {x - 1}: Przenoszenie elementu"
                  f" o wartośći {element} z pozycji {x} na pozycję {pos}")
        else:
            print(f"\nKrok {x - 1}: Element o wartości {element} "
                  f"pozostaje na pozycji {x}")
        tab[pos] = element
        wypisz(tab)


print("Podaj wielkość tablicy:")
a = int(input())
tablica = []

for i in range(a):
    print(f"Element tablicy nr. {i + 1}:")
    tablica.append(int(input()))

print("Oto twoja tablica:")
wypisz(tablica)
print("\n")

sortuj_bin(tablica, a)

print("\nPosortowana tablica:")
wypisz(tablica)
