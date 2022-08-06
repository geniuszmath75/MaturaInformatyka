def bubble_sort(tab):

    n = len(tab)

    for i in range(n):
        for j in range(1, n - i):
            if tab[j - 1] > tab[j]:
                tab[j - 1], tab[j] = tab[j], tab[j - 1]

    print(tab)

tab = [3, 2, 4, 3, 1, 2, 0]
print(f"Nieuporządkowane dane: {tab}")
print("Uporządkowane dane:", end=' ')
bubble_sort(tab)

