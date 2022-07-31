# iteracyjnie
def NWD(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

# rekurencyjnie
def NWD_rekurencja(a, b):
    if b != 0:
        return NWD(b, a%b)
    return a

if __name__ == "__main__":
    a = 18
    b = 0
    print(f'NWD {a} i {b}: {NWD(a, b)}')
    print(f'NWD {a} i {b}: {NWD_rekurencja(a, b)}')