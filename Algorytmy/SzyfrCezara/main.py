#uniwersalne szyfrowanie
def check(char):
    if 'a' <= char <= 'z':
        return 0
    if 'A' <= char <= 'Z':
        return 1
    return 2


def caesar_code(key, tab):
    if not (-26 <= key <= 26):
        return

    tekst = ""

    for i in range(len(tab)):
        t = check(tab[i])
        char_unicode = ord(tab[i])
        if t < 2:
            if t == 0:
                a = 'a'
                z = 'z'
            else:
                a = 'A'
                z = 'Z'
            if key >= 0:
                if char_unicode + key <= ord(z):
                    char_unicode += key
                    tekst += chr(char_unicode)
                else:
                    char_unicode += key - 26
                    tekst += chr(char_unicode)
            else:
                if char_unicode + key >= ord(a):
                    char_unicode += key
                    tekst += chr(char_unicode)
                else:
                    char_unicode += key + 26
                    tekst += chr(char_unicode)
    print(tekst)

if __name__ == '__main__':
    tab = input("Podaj zdanie do zaszyfrowania: ")
    str_key = input("Podaj klucz z przedziału [-26..26]: ")
    key = int(str_key)

    print("Po zaszyfrowaniu: ")
    caesar_code(key, tab)

    print("Po rozszyfrowaniu: ")
    caesar_code(-key, tab)

