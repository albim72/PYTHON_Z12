class Samochod:
    def __init__(self,marka,model,rocznik,cena,rata):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.cena = cena
        self.rata = rata

    @staticmethod
    def salon(miasto):
        return f"salon zakupu: {miasto}"

    @classmethod
    def obliczanieraty(cls,cena,lmiesiac):
        return cls("Opel","Insignia",2019,56000,1.3*cena/lmiesiac)


sm = Samochod("Opel","Insignia",2019,48000,1289)
sm2 = Samochod.obliczanieraty(57800,48)
print(sm.salon("Toruń"))
print(sm.rata)

m1 = sm2.salon("Kraków")
print(m1)
print(sm2.rata)



