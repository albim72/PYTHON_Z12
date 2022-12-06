try:
    x=1
    print(x)
except NameError:
    print("x nie jest zdefiniowane")
except TypeError:
    print("niewłaściwa wartość")
except Exception as ex:
    print(ex)
except:
    print("nieoczekiwany błąd")
else:
    print('x istnieje!')
finally:
    y =9
    print(y)

print("ciąg dalszy....")
