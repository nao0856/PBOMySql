import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='kampus_db'
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        if not query.strip().lower().startswith("select"):
            self.conn.commit()
        return self.cursor

    def close(self):
        self.cursor.close()
        self.conn.close()