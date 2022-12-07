import math
#n! = 1*2*...*n
#double max - 1.8E+308,  min - 2.4E-324
#n??? n= 170
import sys
from negvalue import NagativeValue

sys.set_int_max_str_digits(1000000)
sys.setrecursionlimit(0x1000000)
def silnia(n):
    if n<0:
        raise NagativeValue(n)
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik


def silnia_rek(n):
    if n<0:
        raise NagativeValue(n)
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość n /argumentu funckji silnia/: "))
    print(f'silnia z n = {n} wynosi: {silnia(n)}')
    print(f'silnia rekurencyjna z n = {n} wynosi: {silnia_rek(n)}')
except NagativeValue as v:
    print(v)
