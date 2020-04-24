import sqlite3
#import datetime
#from tkinter import *
#from tkinter import ttk
#from random import randint


class Book_Database:
    def __init__(self, book_db):
        self.conn = sqlite3.connect(book_db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book_db (id INTEGER PRIMARY KEY, key text, chapter_number INTEGER,"
            "user_name text, "
            "chapter_content text, chapter_title text)")
        #number = '1001656482411327'
        #self.cur.execute("UPDATE book_db SET key=? where id=6", (number,))
        #self.conn.commit()
        #self.cur.execute("DELETE from book_db WHERE id=4")
        #self.conn.commit()
        #number = 1001
        #self.cur.execute("INSERT INTO book_db VALUES(NULL,?,?,?,?,?)",
        #                 (number, 1,  "ivan", "Content 1", "Title 1"))
        #self.conn.commit()
        # self.cur.execute("PRAGMA table_info(book_db)")
        # print(self.cur.fetchall())
        #m= '10014922'
        #m_part_string = m[:-1]
        #print(m_part_string)
        #mm =len(m)
        #self.cur.execute("SELECT *, LENGTH(key) FROM book_db WHERE key LIKE ? AND LENGTH(key)==? OR"
        #                 "(key LIKE ? AND LENGTH(key)==?)",
         #                (m+'%', mm+4,m_part_string+'%',mm))
        #print(self.cur.fetchall())
        #self.cur.execute("SELECT *, LENGTH(key) FROM book_db WHERE LENGTH(key)==?",(mm+4,))
        #print(self.cur.fetchall())
        #self.cur.execute("SELECT * FROM book_db")
        #print(self.cur.fetchall())
        # key = self.cur.fetchall()
        # print(key)
        self.cur.execute("SELECT * FROM book_db ")
        print(self.cur.fetchall())

    def muduul(self):
        self.cur.execute("SELECT * FROM book_db order by chapter_number")
        return self.cur.fetchall()


    def all_kyes_in_db(self):
        self.cur.execute("SELECT key FROM book_db")
        all_keys = self.cur.fetchall()
        return all_keys

    def table_columns(self):
        self.cur.execute("PRAGMA table_info(book_db)")
        self.cur.execute("SELECT * FROM book_db")
        g = self.cur.fetchall()
        return g

    def frst_chapter(self, var):
        self.cur.execute("SELECT * FROM book_db WHERE key=? or user_name=? OR chapter_title=? ORDER BY key ASC",
                         (var, var, var))
        g = self.cur.fetchall()
        return g

    def show_all_chapters(self):
        self.cur.execute("SELECT * FROM book_db")
        g = self.cur.fetchall()
        return g

    def add_chapter(self, key, chapter_number, user_name, new_chapter, write_chapter):
        self.cur.execute("INSERT INTO book_db VALUES(NULL,?,?,?,?,?)",
                         (key, chapter_number, user_name, new_chapter, write_chapter))
        self.conn.commit()
        self.cur.execute("SELECT * FROM book_db")
        g = self.cur.fetchall()
        return g

    def edit_chapter_db(self, edited_content, user_name, title_name):
        self.cur.execute("UPDATE book_db SET chapter_content=? WHERE user_name=? AND chapter_title=?",
                         (edited_content, user_name, title_name))
        self.conn.commit()
        g = self.cur.fetchall()
        return g

  #  def tree(self):
  #      self.cur.execute("SELECT * FROM book_db")
  #      g = self.cur.fetchall()
  #      print(g)
  #      return g

   # def filter_new_branch(self,key_str, key_str_len_minus_1, key_str_len):
  #      self.cur.execute("SELECT *, LENGTH(key) FROM book_db WHERE key LIKE ? AND LENGTH(key)==? OR"
   #                      "(key LIKE ? AND LENGTH(key)==?)",
  #                       (key_str + '%', key_str_len + 4, key_str_len_minus_1 + '%', key_str_len))
#
   #     print(self.cur.fetchall())
#
   #     self.cur.execute("SELECT *, LENGTH(key) FROM book_db WHERE key LIKE ? AND LENGTH(key)==?",
   #                      (key_str + '%', key_str_len + 4))
   #     g = self.cur.fetchall()
   #     return g

    def filter_new_branch2(self,key_str):
        #self.cur.execute("SELECT *, LENGTH(key) FROM book_db WHERE key LIKE ? AND LENGTH(key)==? OR"
        #                 "(LENGTH(key)==?)",
        #                 (key_str + '%', key_str_len + 4, key_str_len))
        #print('#####')
        #print(self.cur.fetchall())

        self.cur.execute("SELECT *, LENGTH(key) FROM book_db WHERE key LIKE ?",
                         (key_str + '%',))
        g = self.cur.fetchall()
        return g

