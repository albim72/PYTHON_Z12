from pojazd import Pojazd

mp = Pojazd()
odl = 456
lt = 41
cena_l = 7.8
print(f'spalanie [l/100km]: {mp.spalanie100(odl,lt):.3f}')
print(f'koszt przejazdu na trasie {odl} km = {mp.koszt_przejazdu(odl,lt,cena_l):.2f} zł')

