from math import sqrt

file = open("Dane_2205/liczby.txt", "r")

data = list(map(str.strip,file.readlines()))
counter = 0
first_equal = -1
for number in data:
    first = number[0]
    last = number[-1]
    if first == last:
        counter+=1
        if first_equal == -1:
            first_equal = int(number)
print(counter, first_equal)


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True
prime_table = []
for i in range(100001):
    if isPrime(i):
        prime_table.append(i)
print(prime_table)

def get_factors(n):
    factors = []
    while n != 1:
        for x in prime_table:
            while n%x == 0:
                factors.append(x)
                n = n/x
            if n==1:
                break
    return factors

max_factors = 0
max_unique_factors = 0
for number in data:
    number = int(number)
    factors = get_factors(number)
    unique_factors = len(set(factors))
    if len(factors) > max_factors:
        max_factors = len(factors)
        max_number = number
    if unique_factors > max_unique_factors:
        max_unique_factors = unique_factors
        max_number_unique = number
print(max_factors, max_number)
print(max_unique_factors, max_number)

data = list(map(int, data))
counter = 0
for x in data:
    for y in data:
        for z in data:
            if z % y == 0 and y % x == 0 and z != y and y != x:
                print(x, y, z)
                counter+=1

print(counter)
'''for x in data:
    for a in range(10000):
        tmp = x*a
        if tmp in data:
            for b in range(10000):
                tmp2 = tmp*b
                if tmp2 in data:
                    for c in range(10000):
                        tmp3 = tmp2*c
                        if tmp3 in data:
                            for e in range(2, 10000):
                                tmp4 = tmp3*e
                                if tmp4 in data:
                                    if x!= tmp and tmp != tmp2 and tmp2 !=tmp3 and tmp3!=tmp4:
                                        print(x, tmp, tmp2, tmp3, tmp4)
                                if tmp4 > data[-1]:
                                    break
                        if tmp3 > data[-1]:
                            break
                if tmp2 > data[-1]:
                    break
        if tmp > data[-1]:
            break'''

