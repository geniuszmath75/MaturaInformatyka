#rekurencyjnie
def horner_diagram(wsp, st, x):
    if st == 0:
        return wsp[0]
    return x * horner_diagram(wsp, st-1, x) + wsp[st]

"""#iteracyjnie
def horner_diagram2(wsp, st, x):
    result = wsp[0]
    i = 1
    for i in range(st):
        result = result * x + wsp[i]
        i += 1
    return result"""


if __name__ == '__main__':
    i = 0

    degree = int(input("Podaj stopień wielomianu: "))

    factors = []

    for i in range(degree + 1):
        x = int(input(f"Podaj współczynnik stojący przy potędze {degree - i}: "))
        factors.append(x)
        i += 1

    argument = int(input("Podaj argument: "))
    print(f"W( {argument} ) = {horner_diagram(factors, degree, argument)} \n")