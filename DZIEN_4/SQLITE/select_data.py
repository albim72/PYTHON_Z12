import sqlite3
from sqlite3 import Error
from conn import create_connection


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_task_by_priority(conn,priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority = ?",(priority,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

def select():
    database = r"c:\sqlite\db\mojanowabaza.db"
    conn = create_connection(database)
    with conn:
        print("1. Zadanie z filtrowaniem po priorytecie:")
        select_task_by_priority(conn,1)

        print("2. Wyświetlenie wszystkich zadań:")
        select_all_tasks(conn)
