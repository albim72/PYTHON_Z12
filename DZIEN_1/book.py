sklep = ["masło","mleko","twaróg","jaja","szczypiorek"]
enumsklep = enumerate(sklep)
print(type(enumsklep))
print(list(enumsklep))

drugienum = enumerate(sklep,105)
print(list(drugienum))

print("________________________________________________________")

nb = [1,2,3,4,5]
opis_pl = ['jeden','dwa','trzy','cztery','pięć']
opis_eng = ['one','two','three','four','five']

wn = zip(nb,opis_pl,opis_eng)
print(type(wn))
wn_list = list(wn)
print(wn_list)
