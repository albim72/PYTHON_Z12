def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f'Element listy - indeks: {i} -> wartość {j}')
        
def czytaj_slownik(dict):
    for x,y in dict.items():
        print(f'klucz -> {x}: wartość: {y}')
