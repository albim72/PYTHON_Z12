#napisz klasę która będzie tworzyć krotkę na podstawie zadanych watości tak że przyjmi tylko wartości dodatnie lub 0
#wartości ujemne odrzuci, ale podliczy je

class DodatniaKrotka(tuple):
    def __new__(cls, *liczby):
        licznik_odrzuconych =0
        liczby_dodatnie = []

        for x in liczby:
            if x>=0:
                liczby_dodatnie.append(x)
            else:
                licznik_odrzuconych += 1

        instancja = super().__new__(cls,tuple(liczby_dodatnie))
        instancja.licznik_odrzuconych = licznik_odrzuconych
        return instancja

ldod = DodatniaKrotka(-5,8,9,0,12,-3,-44,2,3,-1,9,0,10,-3)
print(ldod)
print(type(ldod))

print(ldod.licznik_odrzuconych)
