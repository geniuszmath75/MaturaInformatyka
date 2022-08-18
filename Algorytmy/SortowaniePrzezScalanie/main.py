def wypisz(tab):
    for x in tab:
        print(x, end=', ')

def merge(tab, n, m, r):
    lsize = m - n + 1
    rsize = r - m

    left = [0] * lsize
    right = [0] * rsize

    for i in range(lsize):
        left[i] = tab[n + i]
    for j in range(rsize):
        right[j] = tab[m + j + 1]

    leftIndex = 0
    rightIndex = 0
    currIndex = n
    while leftIndex < lsize and rightIndex < rsize:
        if left[leftIndex] <= right[rightIndex]:
            tab[currIndex] = left[leftIndex]
            leftIndex += 1
        else:
            tab[currIndex] = right[rightIndex]
            rightIndex += 1
        currIndex += 1

    while leftIndex < lsize:
        tab[currIndex] = left[leftIndex]
        currIndex += 1
        leftIndex += 1
    while rightIndex < rsize:
        tab[currIndex] = right[rightIndex]
        currIndex += 1
        rightIndex += 1

def sort_by_merge(tab, l, r):
    if r > l:
        m = int((r + l) / 2)
        sort_by_merge(tab, l, m)
        sort_by_merge(tab, m+1, r)
        merge(tab, l, m, r)

print("Podaj liczbę elementów tablicy:", end=' ')
n = int(input())
tab = []

for i in range(0, n):
    print(f"Element tablicy nr {i+1}:", end=' ')
    tab.append(int(input()))

print("Oto twoja tablica: ")
wypisz(tab)

sort_by_merge(tab, 0, n-1)

print("\nPosortowana tablica: ")
wypisz(tab)