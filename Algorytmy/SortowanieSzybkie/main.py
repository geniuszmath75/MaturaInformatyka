def wypisz(tab, low, high):
    print()
    for x in range(low, high+1):
        print(tab[x], end=', ')
    print()
    print()

def quick_sort(tab, iLow, iHigh):
    if iLow >= iHigh or iLow < 0 or iHigh < 0:
        return
    pivot = tab[iLow]
    lowerNumsEndIndex = iLow + 1
    for i in range(iLow + 1, iHigh + 1):
        if tab[i] <= pivot:
            pom = tab[i]
            tab[i] = tab[lowerNumsEndIndex]
            tab[lowerNumsEndIndex] = pom
            lowerNumsEndIndex += 1

    pom = tab[iLow]
    tab[iLow] = tab[lowerNumsEndIndex - 1]
    tab[lowerNumsEndIndex - 1] = pom
    print(f"Podtablica {iLow}: {iHigh}")
    wypisz(tab, iLow, iHigh)
    quick_sort(tab, iLow, lowerNumsEndIndex - 2)
    quick_sort(tab, lowerNumsEndIndex, iHigh)

print("Podaj ilość elementów tablicy: ")
a = int(input())
tab = []

for i in range(a):
    print(f"Element tablicy nr. {i+1}: ")
    tab.append(int(input()))

print("\nOto twoja tablica:")
wypisz(tab, 0, a-1)
quick_sort(tab, 0, a-1)
print("\nPosortowana tablica: ")
wypisz(tab, 0, a-1)

