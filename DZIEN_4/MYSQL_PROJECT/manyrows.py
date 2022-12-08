import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',
                             port=3306, database='dbtestowa')

cursorObject = db.cursor()

insert_student = "INSERT INTO student(imie,nazwisko,nralb) VALUES(%s,%s,%s)"
val = [
    ('Janina',"Nowak",675465),
    ('Janusz',"Nowik",5656),
    ('Olaf',"Kolek",786767),
    ('Anna',"Kowal",89888),
    ('Henio',"Kos",454554),
    ('Nadia',"Maj",656356),
    ('Marek',"Ryć",4567657),
]

cursorObject.executemany(insert_student,val)
db.commit()

print(f'dodano rekordów: {cursorObject.rowcount}')
db.close()
