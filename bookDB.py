import sqlite3
import datetime

class Book_Database:
    def __init__(self, book_db):
        self.conn = sqlite3.connect(book_db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book_db (id INTEGER PRIMARY KEY, user_name text, "
            "chapter1 text, chapter_title)")
        #self.cur.execute("UPDATE book_db SET chapter_name =? WHERE id = 2",("ChapterTwo",))
        #self.conn.commit()
        self.cur.execute("SELECT * FROM book_db")
        g = self.cur.fetchall()
        print(g)
        self.cur.execute("SELECT * FROM book_db WHERE user_name=?", ("ivan",))
        g = self.cur.fetchall()
        self.cur.execute("PRAGMA table_info(book_db)")


        #self.cur.execute("ALTER TABLE book_db RENAME TO book_db_orig")
        #self.cur.execute("CREATE TABLE team(user_name TEXT, chapter_content TEXT, chapter_title TEXT)")
        #self.cur.execute("ALTER TABLE book_db RENAME TO book_db_orig;")




    def frst_chapter(self,var):
        #self.cur.execute("INSERT INTO book_db VALUES (NULL, ?,?)",
         #                (user_name, chapter1))
        print(var)
        self.cur.execute("SELECT * FROM book_db WHERE user_name=? OR chapter_title=?",(var,var))
        g = self.cur.fetchall()
        print(g)
        return g

    def add_chapter_master(self,user_name,new_chapter, write_chapter):
        self.cur.execute("INSERT INTO book_db VALUES(NULL, ?,?,?)",
                         (user_name, new_chapter, write_chapter))
        self.conn.commit()
        self.cur.execute("SELECT * FROM book_db")
        g = self.cur.fetchall()
        print(user_name,new_chapter, write_chapter)
        return g