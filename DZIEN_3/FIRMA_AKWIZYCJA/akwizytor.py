from decimal import Decimal

class Akwizytor:

    """
    pracownik, którego wynagrodzenie jest wyłącznie prowizją od sprzedaży
    """

    def __init__(self,imie,nazwisko,nr_ubezp,sprzedaz,prowizja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_ubezp = nr_ubezp
        self._sprzedaz = sprzedaz
        self._prowizja = prowizja

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def nr_ubezp(self):
        return self._nr_ubezp

    @property
    def sprzedaz(self):
        return self._sprzedaz

    @sprzedaz.setter
    def sprzedaz(self,kwota):
        if kwota < Decimal('0.00'):
            raise ValueError('wartość sprzedaży nie może być ujemna')
        self._sprzedaz = kwota

    @property
    def prowizja(self):
        return self._prowizja

    @prowizja.setter
    def prowizja(self,procent):
        if not(Decimal('0.0')<procent<Decimal('30.0')):
            raise ValueError('prowizja musi zawierać się w przedziale od 0 do 30 procent')
        self._prowizja = procent

    def zarobek(self):
        return self.sprzedaz*(self.prowizja/Decimal('100.0'))

    def __repr__(self):
        """
        reprezentacja tesktowa obiektu
        :return:
        """
        return f'Akwizytor: {self.imie} {self.nazwisko}\n numer ubezpieczenia {self.nr_ubezp}\n' \
               f'prowizja: {self.prowizja} %\n' \
               f'sprzedaz: {self.sprzedaz} zł'



