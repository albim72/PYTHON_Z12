import json

osoba = '{"imie":"Jan","nazwisko":"Kot","miasto":"Kraków","wiek":41}'

print(osoba)
print(type(osoba))

osoba_dict = json.loads(osoba)
print(osoba_dict)
print(type(osoba_dict))
print(osoba_dict["miasto"])

samochod = {
    "marka":"Opel",
    "model":"Insignia",
    "rocznik":2020
}

jsonsam = json.dumps(samochod,indent=4)
print(jsonsam)

with open("samochod.json","w",encoding="utf-8") as f:
    f.write(jsonsam)

with open("samochod.json","r",encoding="utf-8") as f:
    auto_dict = json.load(f)

print(auto_dict)
print(type(auto_dict))
