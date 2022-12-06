from typing import Protocol,runtime_checkable

@runtime_checkable
class Zwierz(Protocol):
    def odglos(self) -> None:
        ...

    def liczba_nog(self) -> int:
        ...


class Dog:
    def odglos(self) -> None:
        print("Odgłos psa - szczekanie")

    def liczba_nog(self) -> int:
        return 4


def pies_szczeka(zw) -> None:
    zw.odglos()

pies = Dog()
print(isinstance(pies,Zwierz))
pies_szczeka(pies)
