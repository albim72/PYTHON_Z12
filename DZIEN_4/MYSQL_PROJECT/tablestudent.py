import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',
                             port=3306, database='dbtestowa')

cursorObject = db.cursor()

nowatab = "CREATE TABLE student(imie VARCHAR(50), nazwisko VARCHAR(50), nralb int);"

cursorObject.execute(nowatab)
print("tabela student została utworzona w bazie dbtestowa...")

insert_student = "INSERT INTO student(imie,nazwisko,nralb) VALUES(%s,%s,%s)"
val = ("Jan","Kot",54545)

cursorObject.execute(insert_student,val)
db.commit()

print(f'dodano rekordów: {cursorObject.rowcount}')
db.close()

