from functools import singledispatch
from decimal import Decimal

@singledispatch
def costam(s,t):
    print(f'{s}:{t}')

@costam.register(int)
def _(s,t):
    print(f"{s*2}:{t}")

@costam.register(float)
def _(s,e,t):
    print(f"{s/2*e}:{t}")


costam("ładny dzień","słońce świeci")
costam(25,"liczba całkowita")
costam(2.45,12.56,"liczba z ułamkiem")
