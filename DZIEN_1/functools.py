from functools import partial

def potega(a,b):
    return a**b + 22

#funkcje częściowe
pot2 = partial(potega,b=2)
pot4 = partial(potega,b=4)
potega_of_5 = partial(potega,5)

print(potega(12,3))
print(pot2(4))
print(pot2(3))
print(potega_of_5(2))

print(pot2.func)
print(pot2.keywords)
print(potega_of_5.args)
