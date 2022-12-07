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
