from xml.etree.ElementTree import Element,SubElement
import xml.etree.ElementTree as ET
from prettyfy import pretty


top = Element("autokomis")

sam1 = SubElement(top,'samochod')

id = SubElement(sam1,'id')
id.text = 'sam1'

marka = SubElement(sam1,'marka')
marka.text = 'Subaru'

model = SubElement(sam1,'model')
model.text = 'Impreza'

rok = SubElement(sam1,'rocznik')
rok.text = '1999'

poj = SubElement(sam1,'pojemnosc')
poj.text = '2.0'

cena = SubElement(sam1,'cena')
cena.text = '56000'

wyp_dod = SubElement(sam1,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czarna perła'
klima = SubElement(wyp_dod,'klimatyzacja')
klima.text = 'czarna perła'

# drugi egzemplarz

sam2 = SubElement(top,'samochod')

id = SubElement(sam2,'id')
id.text = 'sam2'

marka = SubElement(sam2,'marka')
marka.text = 'Subaru'

model = SubElement(sam2,'model')
model.text = 'Outback'

rok = SubElement(sam2,'rocznik')
rok.text = '2019'

poj = SubElement(sam2,'pojemnosc')
poj.text = '2.4'

cena = SubElement(sam2,'cena')
cena.text = '124000'

wyp_dod = SubElement(sam2,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czerwony metallic'
dodpod = SubElement(wyp_dod,'dodatkowe_poduszki')
dodpod.text = '4'
