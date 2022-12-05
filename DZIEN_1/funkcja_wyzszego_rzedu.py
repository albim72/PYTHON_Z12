def filtrowanie(dane,test):
    plus = []
    for element in dane:
        if (test(element)):
            plus.append(element)
    return plus

def ekstra_liczba(n):
    return n>=100

lb = [99,34,-4,500,101,45,68,-46,150]

print(filtrowanie(lb,ekstra_liczba))


def mapowanie(dane,transformacja):
    mapa = []
    for element in dane:
        mapa.append(transformacja(element))
    return mapa

def add_five(n):
    return n+5

print(mapowanie(lb,add_five))
