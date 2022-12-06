class Sport:
    def __init__(self,dyscyplina,lata_upr,zyciowka):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.zyciowka = zyciowka
        
    def infosport(self):
        return f'dycyplina: {self.dyscyplina}, lata uprawiania: {self.lata_upr}, życiówka: ' \
               f'{self.zyciowka}'
        
