#lambda, oneliner
print((lambda e:e**2-1)(6))
x = lambda u,m:u+m**2

print(x(4,7))

def umx(u,m):
    return u+m**2

print(umx(2,3))

def policz(n,m):
    return lambda a:a*n+m

print(policz(9,3)(4))

nb = [56,112,0,-89,3,7,9,11,101,-90,12,-44]


#stwórz nową listę o nazwie parzyste i wypełnij ją wszystkim parzystymi wartościami z listy nb
#funkcja filter(funkcja,dane) -> funckcja -> f. przekazująca warunek, dane do filtrowania

parzysta = list(filter(lambda x:x%2==0,nb))
print(parzysta)

def warunek(x):
    return x%2==0

parzysta = list(filter(warunek,nb))
print(parzysta)

#stwórz nową listę cube i wypełnij ją wszytskimi wartościami z listy nb podniesionymi do potęgi trzeciej
cube = list(map(lambda x:x**3,nb))
print(cube)
