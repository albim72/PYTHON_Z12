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
