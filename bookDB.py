import sqlite3
import datetime
from tkinter import *
from tkinter import ttk
from random import randint

class Book_Database:
    def __init__(self, book_db):
        self.conn = sqlite3.connect(book_db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book_db (id INTEGER PRIMARY KEY, key INTEGER, user_name text, "
            "chapter_content text, chapter_title text)")
        #number = str(1001)
        #self.cur.execute("UPDATE book_db SET chapter_title=? where id=6", ("Title2",))
        #self.conn.commit()
        #self.cur.execute("DELETE from book_db WHERE id=5")
        #self.conn.commit()
        #self.cur.execute("INSERT INTO book_db VALUES(NULL, ?,?,?,?)",
        #                 (number, "ivan", "Content 1", "Title 1"))
        #self.conn.commit()
        #self.cur.execute("PRAGMA table_info(book_db)")
        #print(self.cur.fetchall())
        #self.cur.execute("SELECT * FROM book_db")
        #print(self.cur.fetchall())
        self.cur.execute("SELECT * FROM book_db")
        print(self.cur.fetchall())
        #key = self.cur.fetchall()
        #print(key)
    def table_columns(self):
        self.cur.execute("PRAGMA table_info(book_db)")
        self.cur.execute("SELECT * FROM book_db")
        g = self.cur.fetchall()
        return g

    def frst_chapter(self,var):
        #self.cur.execute("INSERT INTO book_db VALUES (NULL, ?,?)",
         #                (user_name, chapter_content))
        self.cur.execute("SELECT * FROM book_db WHERE user_name=? OR chapter_title=?",(var,var))
        g = self.cur.fetchall()
        print(g)
        return g

    def show_all_chapters(self):
        self.cur.execute("SELECT * FROM book_db")
        g = self.cur.fetchall()
        return g

    def add_chapter_master(self,key,user_name,new_chapter, write_chapter):
        self.cur.execute("INSERT INTO book_db VALUES(NULL,?,?,?,?)",
                         (key,user_name, new_chapter, write_chapter))
        self.conn.commit()
        self.cur.execute("SELECT * FROM book_db")
        g = self.cur.fetchall()
        print(g)
        return g

    def edit_chapter_db(self, edited_content, user_name, title_name):
        self.cur.execute("UPDATE book_db SET chapter_content=? WHERE user_name=? AND chapter_title=?",
                         (edited_content, user_name, title_name))
        self.conn.commit()
        g = self.cur.fetchall()
        return g


    def tree(self):
        self.cur.execute("SELECT * FROM book_db")
        g = self.cur.fetchall()
        print(g)
        return g



