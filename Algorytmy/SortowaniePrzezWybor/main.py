def wypisz(tab):
    for el in tab:
        print(el, end=" | ")

def sort_by_choice(tab):
    n = len(tab)
    index = 0
    i = 0

    for i in range(n - 1):
        index = i
        for j in range(i+1, n):
            if tab[j] < tab[index]:
                index = j
        if i != index:
            tab[index], tab[i] = tab[i], tab[index]

print("Podaj ilość elementów tablicy: ")
a = int(input())
tab = []
for i in range(a):
    print(f"Element tablicy nr. {i+1}")
    tab.append(int(input()))

print("Oto twoja tablica: ")
wypisz(tab)
sort_by_choice(tab)
print("\nOto twoja tablica po sortowaniu: ")
wypisz(tab)

