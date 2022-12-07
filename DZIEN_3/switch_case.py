#istrukcja match-case

dzien = 84

match dzien:
    case 1:
        print("poniedziałek")
    case 2:
        print("wtorek")
    case 3:
        print("środa")
    case 4:
        print("czwartek")
    case 5:
        print("piątek")
    case 6:
        print("sobota")
    case 7 | 8:
        print("niedziela")
    case _:
        print("nieznany dzień")

class Switch(object):
    value = None
    def __new__(cls, value):
        cls.value = value
        return True

def case(*args):
    return any((arg==Switch.value for arg in args))

n = int(input("podaj cyfrę (0-9): "))

s1 = Switch(n)
s2 = Switch(90)

print(s1==s2)

while Switch(n):
    if case(0):
        print("n jest równe 0")
        break
    if case(1,4,9):
        print("n jest kwadratem innej liczby")
        break
    if case(2):
        print("n jest liczbą parzystą")
    if case(2,3,5,7):
        print("n jest liczbą pierwszą")
        break
    if case(6,8):
        print("n jest krotnością liczby 2")
        break
    print("pisz tylko cyfry!")
    break
