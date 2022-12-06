from typing import Protocol

class Zwierz(Protocol):
    def odglos(self) -> None:
        ...

    def liczba_nog(self) -> int:
        ...


class Dog:
    def odglos(self) -> None:
        print("Odgłos psa - szczekanie")

    # def liczba_nog(self) -> int:
    #     return 4


def pies_szczeka(zw:Zwierz) -> None:
    zw.odglos()

pies = Dog()
pies_szczeka(pies)
