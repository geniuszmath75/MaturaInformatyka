def wypisz(tab):
    for x in tab:
        print(x, end=", ")

def minMax(tab):
    min = tab[0]
    max = tab[0]
    for el in tab:
        if el > max:
            max = el
        if el < min:
            min = el
    array = []
    array.append(min)
    array.append(max)
    return array


def bucket_sort(tab, n):
    minmax = minMax(tab)
    yMin = minmax[0]
    yMax = minmax[1]
    buckets = [0] * (yMax - yMin + 1)
    print("Stworzono kubełki:")
    for x in range(yMax - yMin + 1):
        print(f"B {x+yMin}", end=", ")
    print()
    for x in range(n):
        buckets[tab[x] - yMin] += 1
    print("Zliczono elementy:")
    for x in range(yMax - yMin+1):
        print(f"B {x + yMin} = {buckets[x]}", end=", ")
    print()
    lastIndex = 0
    for x in range(yMax - yMin + 1):
        y = lastIndex
        while y < buckets[x] + lastIndex:
            tab[y] = x + yMin
            y += 1
        lastIndex = y

print("Podaj ilość elementów tablicy:")
a = int(input())
tab = []

for i in range(a):
    print(f"Element tablicy nr {i + 1}:")
    tab.append(int(input()))

print("Oto twoja tablica:")
wypisz(tab)

bucket_sort(tab, a)

print("Posortowana tablica:")
wypisz(tab)