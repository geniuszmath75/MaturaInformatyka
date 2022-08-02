def if_palindrome(tab):
    i = 0
    j = len(tab) - 1

    while i < j:
        if tab[i] != tab[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    string = input("Podaj wyraz: ")
    if if_palindrome(string) == 1:
        print(f"Wyraz {string} jest palindromem.")
    else:
        print(f"Wyraz {string} nie jest palindromem.")


