def wypisz(tab):
    for x in tab:
        print(x, end=", ")

def sort_by_insert(tab):
    n = len(tab)
    pom = 0
    t = 0
    for i in range(1, n):
        pom = tab[i]
        j = i - 1

        while j >= 0 and tab[j] > pom:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = pom

print("Podaj wielkość tablicy:")
a = int(input())
tab = []

for i in range(a):
    print(f"Element tablicy nr. {i+1}:")
    tab.append(int(input()))

print("Oto twoja tablica:")
wypisz(tab)

sort_by_insert(tab)

print("\nPosortowana tablica:")
wypisz(tab)