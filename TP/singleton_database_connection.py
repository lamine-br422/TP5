import sqlite3

class DatabaseSingleton:
    instance = None

    def __new__(cls, dbname):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.conn = sqlite3.connect(dbname)
        return cls.instance

    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()
