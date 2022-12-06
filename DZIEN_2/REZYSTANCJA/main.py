from oldresistor import OldResistor

r0 = OldResistor(2.2E3)
print(f"_________________{r0.__class__.__name__}____________________")
print(r0.get_ohms())
r0.set_ohms(1.1E2)
print(r0.get_ohms())
