import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',
                             port=3306, database='dbtestowa')

cursorObject = db.cursor()

print("wyświetlania imienia i nazwiska studenta z tabeli student: ")

query = "SELECT imie, nazwisko FROM student"
cursorObject.execute(query)

result = cursorObject.fetchall()

for x in result:
    print(x)

print("wyświetlania imienia i nazwiska studenta z tabeli student z indeksami powyżej numeru 100000: ")

nquery = "SELECT * FROM student WHERE nralb > 100000;"
cursorObject.execute(nquery)

nresult = cursorObject.fetchall()

for x in nresult:
    print(x)


db.close()

