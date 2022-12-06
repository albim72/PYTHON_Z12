import math
#n! = 1*2*...*n
#double max - 1.8E+308,  min - 2.4E-324
#n??? n= 170

def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik

try:
    n = int(input("podaj wartość n /argumentu funckji silnia/: "))
    print(f'silnia z n = {n} wynosi: {silnia(n)}')
except ValueError as v:
    print(v)
