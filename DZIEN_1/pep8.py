marka = "Jeep"
model = "Cherokee"
rocznik = "2020"

sam = "samochód -> marka: {}, model: {}, rocznik: {}"
print(sam.format(marka,model,rocznik))

#f-string
print(f"samochód marki {marka}, model: {model}, rocznik: {rocznik}")

konkurs = [
    ("Jan",67),
    ("Ala",63),
    ("Ola",55),
    ("Henio",89),
    ("Basia",86),
    ("Nadia",76),
    ("Maciej",44)

]

print(konkurs[2])
en = list(enumerate(konkurs))
print(en)

print("________________zestawienie wyników konkursowych_____________________")
for i,(imie,punkty) in enumerate(konkurs):
    print('no %d: %-9s: %.1f punktów' %(i+1,imie,punkty))

print(type(konkurs))

marki = ["audi","seat","bmw","toyota","landrover","reanult","cadillac"]

marki_parz = marki[::2]
marki_nieparz= marki[1::2]

print(marki_parz)
print(marki_nieparz)

tekst = "zimowa aura"
print(f"{tekst} <-> {tekst[::-1]}")
print(tekst[2:7])

kolory = {"biały","czarny","niebieski","zielony","czerwony","biały"}
print(kolory)
