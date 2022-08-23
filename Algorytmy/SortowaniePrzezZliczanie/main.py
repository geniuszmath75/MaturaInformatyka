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


def sort_by_counting(tab, n):
    minmax = minMax(tab)
    min = minmax[0]
    max = minmax[1]
    countersSize = max - min + 1
    counters = [0] * countersSize
    print("\nStworzono tablicę liczników: ")
    for x in range(countersSize):
        print(f"{x+min} = 0", end=", ")
    print()
    for x in range(n):
        counters[tab[x] - min] += 1
    print("Zliczono ilość elementów: ")
    for x in range(countersSize):
        print(f"{x+min} = {counters[x]}", end=", ")
    print()
    lastIndex = 0
    for x in range(countersSize):
        y = lastIndex
        while y < counters[x] + lastIndex:
            tab[y] = x + min
            y += 1
        lastIndex = y


print("Podaj ilość elementów tablicy:")
a = int(input())
tab = []
for i in range(a):
    print(f"Element tablicy nr. {i+1}:")
    tab.append(int(input()))
print("Oto twoja tablica:")
wypisz(tab)
sort_by_counting(tab, a)
print("Oto twoja tablica po sortowaniu:")
wypisz(tab)