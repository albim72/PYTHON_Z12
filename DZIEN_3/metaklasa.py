class MojaMeta(type):
    def __new__(cls, clsname,supercls,attribsdict):
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy: {supercls}")
        print(f"atrybuty: {attribsdict}")
        return type.__new__(cls, clsname,supercls,attribsdict)


class Base:
    pass

bs = Base()

class Pierwsza(Base,metaclass=MojaMeta):
    pass

class H:
    pass

class Druga(Pierwsza,H):
    pass
