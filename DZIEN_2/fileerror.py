import sys

try:
    f = open("waznedane.txt","r",encoding="utf-8")
    s = f.readline()
    i = int(s.strip())
    raise Exception(d=i/0)
except OSError as er:
    print(f'błąd systemowy: {er}')
except ValueError:
    print('nie można przkonwertować danych z typu str do int')
except Exception as exx:
    print(f"klasa błędu: {type(exx)}")
    print(exx.args)
    print(exx)
except:
    print(f'nieoczekiwany błąd: {sys.exc_info()[0]}')
