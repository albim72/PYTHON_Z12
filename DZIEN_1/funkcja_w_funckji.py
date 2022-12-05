#przykład 1

def witaj(imie):
    return f"miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik konkursu {imie}, liczba punktów = {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Leon",67))

#przykład 2

def rejestracja(oplata):
    def lista():
        return "Brawo! jesteś na liście zawodników"
    def brak():
        return "Brak wpłaty. Masz 3 dni na zapałacenie. Inczej zostaniesz skeślony z listy"
    def error():
        return "zły kod opłaty, podaj 1 - wpłata, 2 - brak"
    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(6)())
