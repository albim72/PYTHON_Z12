class Pracownik:

    def __init__(self):
        print("pracownik został utworzony!")

    def info(self):
        print("pracownik firmy ABC...")

    def __del__(self):
        print("destruktor został wykonany, pracownik został usunięty!")

prac = Pracownik()
prac.info()
prac.info()
prac.info()
del prac
prac_2 = Pracownik()
prac_2.info()

# prac.info()

s = 999
print(s)
del s
# print(s)
