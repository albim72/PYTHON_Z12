from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance

r0 = OldResistor(2.2E3)
print(f"_________________{r0.__class__.__name__}____________________")
print(r0.get_ohms())
r0.set_ohms(1.1E2)
print(r0.get_ohms())

r1 = Resistor(2.1E2)
print(f"_________________{r1.__class__.__name__}____________________")
print(f'oporność początkowa: {r1.ohms} om')
r1.ohms = 7.8E2

print(f"układ elektryczny:\noporność: {r1.ohms} om\nnapięcie prądu: {r1.voltage} V\n"
      f"natężenie prądu: {r1.current} A")

r2 = VoltageResistance(1.09E3)
print(f"_________________{r2.__class__.__name__}____________________")
print(f'natężenie początkowe prądu: {r2.current} A')
r2.voltage = 45
print(f'natężenie prądu: {r2.current} A')
print(f'napięcie prądu: {r2.voltage} V')
