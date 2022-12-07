from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class GlownyAkwizytor:

    def __repr__(self):
        return 'ile zarobi głowny akwizytor?'

    def zarobek(self):
        return Decimal('12_000_000.00')

k = GlownyAkwizytor()
s = AkwizytorNaEtacie("Jan","Kowalski","444-44-44",Decimal('168900.00'),Decimal('4.57'),Decimal(4350.00))
c = Akwizytor("Olga","Kot","4545335-565",Decimal('231000.00'),Decimal('7.21'))

wyplaty = [c,s,k]
for wp in wyplaty:
    print(wp)
    print(f'{wp.zarobek():,.2f}\n')
