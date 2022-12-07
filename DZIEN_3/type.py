def test_method(self):
    print("to jest metoda klasy Test!")

class Base:
    def mojaf(self):
        print("to jest metoda dziedziczona")

#tworzenie klasy test
Test = type('Test',(Base,),dict(x='atul', mojametoda = test_method))

print(f"typ kalsy Test: {type(Test)}")

test_obj = Test()

print(f"typ obiektu: {type(test_obj)}")

test_obj.mojametoda()
test_obj.mojaf()
print(test_obj.x)
