from akwizytor import Akwizytor
from decimal import Decimal

class AkwizytorNaEtacie(Akwizytor):

    """
    akwizytor, który dostaje wynagrodzenie ryczałtowe (pensja) i dodatkowo prowizję od sprzedaży
    """

    def __init__(self,imie,nazwisko,nr_ubezp,sprzedaz,prowizja,pensja):
        super().__init__(imie,nazwisko,nr_ubezp,sprzedaz,prowizja)
        self.pensja = pensja

    @property
    def pensja(self):
        return self._pensja

    @pensja.setter
    def pensja(self,kwota):
        if kwota<Decimal('0.00'):
            raise ValueError("wynagrodzenie ryczałtowe nie może być ujemne")
        self._pensja = kwota

    def zarobek(self):
        return super().zarobek()  + self.pensja

    def __repr__(self):
        return f'Etatowy: {super().__repr__()}\nryczałt:{self.pensja:.2f} zł'


