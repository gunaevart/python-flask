import sqlite3


class File:

    def Db():
        connect = sqlite3.connect('test.db')
        connect.row_factory = sqlite3.Row
        cursorObj = connect.cursor()
        result = cursorObj.execute('SELECT * FROM user')
        rows = cursorObj.fetchall()
        return rows
