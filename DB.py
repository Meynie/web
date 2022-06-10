import sqlite3


def create_db():
    conn = sqlite3.connect('dbname.sqlite')
    c = conn.cursor()

    # create table
    c.execute('''CREATE TABLE IF NOT EXISTS mainmenu(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL)''')

    # commit the changes to db
    conn.commit()
    # close connection
    conn.close()


class DBHelper:

    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения из БД")
        return []
