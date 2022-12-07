#napisz klasę składającą słownik w oparciu o dwie listy lub krotki z kluczami i wartościami,
#dodatkowo dowzolone typy wartości to: int i float
#obsłuż potencjalne błędy wynikające z zadanych ograniczeń -> napisz dwie klasy wyjątków:
#InFloatValueError -> reakcja na zadaną wartość inną niż int i float
#KeyValueConstructError -> reakcja na niewłaściwą kolekcję definiującą klucz lub wartość słownika ->
#inna niż krotka lub lista....

from slownik import CustomIntFloatDictionary

test_1 = CustomIntFloatDictionary()
print(test_1)

# test_2 = CustomIntFloatDictionary({'a','b'},[34,6])
# print(test_2)

# test_3 = CustomIntFloatDictionary(('x','y','z'),(10,"twenty",30))
# print(test_3)

test_3 = CustomIntFloatDictionary(('x','y','z'),(True,20.08,30.3))
print(test_3)
