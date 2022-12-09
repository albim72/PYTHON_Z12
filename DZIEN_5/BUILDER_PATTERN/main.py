from builder import Builder
from diector import Director
from concrete_builder1 import ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("Podstawowy produkt:")
director.build_minimal_variable_product()
builder.product.list_parts()

print("\n")
