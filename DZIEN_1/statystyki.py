liczby = [6,78,90,1001,-999,34,0,178,199,987,-1090,1213,66,3,4,1,90,35,2]

def statystyki(dane):
    minimum = min(dane)
    maksimum = max(dane)
    rozstep = maksimum-minimum
    n = len(dane)
    suma = sum(dane)
    avg = suma/n
    return minimum,maksimum,rozstep,n,suma,avg

wynik = statystyki(liczby)
print(type(wynik))
print(wynik)

mini,maxi,roz,n,sm,av = statystyki(liczby)
print(f'wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp wartości: {roz},'
      f' liczba elementów: {n}, suma elementów: {sm}, średnia arytmetyczna: {av:.2f}')
