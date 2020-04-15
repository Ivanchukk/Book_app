import sqlite3
import datetime

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS login_db (id INTEGER PRIMARY KEY, email text, user_name text, "
            "password text)")
        self.conn.commit()



    def register_sql(self, email, user_name, password):
        self.cur.execute("INSERT INTO login_db VALUES (NULL, ?,?,?)",
                         (email,user_name,password))

        self.conn.commit()

    def check_userName_password(self,mail,user_name):
        self.cur.execute("SELECT * FROM login_db WHERE email=? OR user_name=?",(mail,user_name,))
        g = self.cur.fetchall()
        return g

    def search_c(self):
        self.cur.execute("SELECT * FROM login_db")
        g = self.cur.fetchall()
        print(g)

    def details_check(self,user_name,password):
        try:
            self.cur.execute("SELECT * FROM login_db WHERE user_name=? and password=?",(user_name,password))
            g = self.cur.fetchall()
            return g
        except (IndexError, TypeError):
            g = False
            return g




