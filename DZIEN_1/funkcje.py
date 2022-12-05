#przykład 1

def gx(n):
    return n**3

g = 600
def px(a:int,b:int,c:int=3,y:float=1) -> float:
    # global g
    g = 100
    g = (a+b)*y**2+c*y + g + gx(b)
    return g

print(px(5,6,8,1))
print(px(5,6))
print(px(3,4,y=7))

print(g)

h:float

h = True
print(h)

def zewnetrzna():
    x = "lokalnie"
    def wewnetrzna():
        nonlocal x
        x= "nielokalnie"
        print(f"wewnętrzne {x}")
    wewnetrzna()
    print(f"zewnętrzne {x}")

zewnetrzna()
