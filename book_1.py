import tkinter as tk
from dominio.entidades import *
#from menu.principal import *
from logindb import *
from tkinter import ttk, messagebox, PhotoImage
from bookDB import *
from KeyValidator import *
book_DB = Book_Database('book_db.db')


class New_page:
    def __init__(self,user_name):
        popup = tk.Toplevel()
        #popup.grab_set()
        width = popup.winfo_screenwidth()
        height = popup.winfo_screenheight()
        popup.geometry(f'{width}x{height}')
        title = tk.Label(popup, text = "{} welcome to our book".format(user_name.title()), fg = "blue", font=("Courier", 44))
        title.grid(row=0,column=6)
        self.user_name = user_name
        frst_c_btn = tk.Button(popup, text="read first chapter", command=self.go_to_first_chapter)
        frst_c_btn.grid(row=1,column=1)

        user_chapter = tk.Button(popup, text="Check your chapters", command=self.user_chapter_def)
        user_chapter.grid(row=1, column=2)

        all_chepters = tk.Button(popup, text="Check all chapters", command=self.all_chepters_def)
        all_chepters.grid(row=1, column=3)



        #frst_c = tk.Text(popup, text="adasda {}".format(self.get_frst_c))
        #frst_c.grid(row=2, column=1)

        self.frame_user_capters = tk.Frame(popup)
        self.frame_all_user_capters = tk.Frame(popup)




    def creat_new_chap(self):
        write_chapter = tk.Toplevel()
        # Chapter name

        #if key == 1001:
        self.chapter_name1 = tk.StringVar()
        self.chapter_name = tk.Entry(write_chapter, textvariable=self.chapter_name1)
        self.chapter_name.grid(row=1,column=1)
        #text box
        self.writer_entry = tk.Text(write_chapter, height=10,width=50)
        self.writer_entry.grid(row=3,column=1)




        btn = tk.Button(write_chapter,text="save", command=lambda: self.retrieve_input())
        btn.grid(row=4,column=1)

    def retrieve_input(self):
        inputvalue = self.writer_entry.get("1.0", "end-1c")
        key_1001_data = book_DB.frst_chapter(self.radionvar.get())
        chapter_key = key_1001_data[0][1]
        chapter_user_name = key_1001_data[0][2]
        #check_user = self.get_frst_c[0][2]
        #check_user = self.row_of_colled_chapter[0][2]
        #key_not_1001 = self.row_of_colled_chapter[0][1]
        if chapter_key == 1001:
            key = keyvalMaster()
        elif chapter_user_name == self.user_name:
            key = chapter_key+1
        else:
            key = keyvalBranch(chapter_key)
        print(key)
        book_DB.add_chapter_master(key,self.user_name, inputvalue, self.chapter_name1.get())

        print(self.chapter_name1.get())

    def go_to_first_chapter(self):
        read_first_chapter = tk.Toplevel()
        first_chapter_text = tk.Text(read_first_chapter, height=50, width=150)
        first_chapter_text.grid(row=3, column=1, rowspan=35)
        self.get_frst_c = book_DB.frst_chapter("Title 1")
        first_chapter_text.insert(tk.INSERT, self.get_frst_c[0][3])
        first_chapter_text.config(state="disabled")

        create_chapter_btn = tk.Button(read_first_chapter,text="create next chapter",
                                       command = self.creat_new_chap)
        create_chapter_btn.grid(row=0,column=3)

    def user_chapter_def(self):
        self.frame_all_user_capters.grid_forget()
        self.frame_user_capters.grid(row=3, column=1)
        self.radionvar = tk.StringVar()
        x = book_DB.frst_chapter(self.user_name)
        self.row_number=5


        for p in x:
            a = tk.Radiobutton(self.frame_user_capters, text=p[4], variable=self.radionvar, value=p[4],tristatevalue=0)
            a.grid(row=self.row_number, column=1)
            self.row_number += 1
        go_to_chapter_btn = tk.Button(self.frame_user_capters, text="go to chapter", command=lambda: self.print_radio())
        go_to_chapter_btn.grid(row=self.row_number+1,column=1)

    def print_radio(self):
        self.row_of_colled_chapter = book_DB.frst_chapter(self.radionvar.get())
        self.first_chapter_level = tk.Toplevel()
        chosen_title = tk.Label(self.first_chapter_level,text=self.radionvar.get(), font=("Arial", 12))
        chosen_title.grid(row=1, column=1)
        self.chosen_chapter = tk.Text(self.first_chapter_level, height=50, width=150)
        self.chosen_chapter.grid(row=3, column=1,rowspan=35)
        self.chosen_chapter.insert(tk.INSERT,self.row_of_colled_chapter[0][3])
        self.chosen_chapter.config(state="disabled")

        #Check if this the chapter of the loged in user
        if self.user_name == self.row_of_colled_chapter[0][2]:
            edit_chapter_btn = tk.Button(self.first_chapter_level, text="Edit", command=self.edit_chapter)
            edit_chapter_btn.grid(row=1,column=3)
        write_next__chapter_btn = tk.Button(self.first_chapter_level, text="write next chapter",
                                                command=self.creat_new_chap)
        write_next__chapter_btn.grid(row=2, column=3)



        #self.write_next_chapter_btn = tk.Button(self.first_chapter_level, text="Write next Chapter",
        #                                        command=self.write_next_chapter)
        #self.write_next_chapter_btn.grid(row=0, column=3)

#        mylabel = tk.Label(self.frame_user_capters, text=self.radionvar.get())
#        mylabel.grid(row=self.n + 2, column=1)

    def write_next_chapter(self):
        self.first_chapter_level.destroy()
        self.write_next_chapter_ = tk.Toplevel()
        self.chapter_name1 = tk.StringVar
        self.chapter_name = tk.Entry(self.write_next_chapter_, textvariable=self.chapter_name1)
        self.chapter_name.grid(row=1, column=1)
        self.chosen_chapter_next_chapter = tk.Text(self.write_next_chapter_, height=50, width=150)
        self.chosen_chapter_next_chapter.grid(row=3, column=1, rowspan=35)
        create_chapter_btn = tk.Button(self.write_next_chapter_, text="Save New Chapter",
                                       command=self.retrieve_input_save)
        create_chapter_btn.grid(row=1, column=3)

    def retrieve_input_save(self):
        inputvalue = self.chapter_name.get("1.0", "end-1c")
        key_1001 = self.get_frst_c[0][1]
        key_not_1001 = self.row_of_colled_chapter[0][1]
        if key_1001 == 1001:
            key = keyvalMaster()
        #        else:
        #            keyvalBranch(key_not_1001)
        print(key)
        book_DB.add_chapter_master(key, self.user_name, inputvalue, self.chapter_name1.get())

        print(self.chapter_name1.get())

    def edit_chapter(self):
        self.chosen_chapter.config(state="normal")
        btn_save = tk.Button(self.first_chapter_level, text="save", command=lambda: self.retrieve_input_edit())
        btn_save.grid(row=4, column=1)

    def retrieve_input_edit(self):
        edited_chapter = self.chosen_chapter.get("1.0", "end-1c")
        book_DB.edit_chapter_db(edited_chapter,self.user_name,  self.radionvar.get())
        self.first_chapter_level.destroy()

    def all_chepters_def(self):
        self.frame_user_capters.grid_forget()
        self.frame_all_user_capters.grid(row=3, column=1)
        self.radionvar = tk.StringVar()
        x = book_DB.show_all_chapters()
        print(x)
        n = 5
        for p in x:
            print(p[3])
            a = tk.Radiobutton(self.frame_all_user_capters, text=p[4], variable=self.radionvar, value=p[4],tristatevalue=0)
            a.grid(row=n, column=1,sticky='W')
            n += 1

        go_to_chapter_btn = tk.Button(self.frame_all_user_capters, text="go to chapter", command=lambda: self.print_radio())
        go_to_chapter_btn.grid(row=n+1,column=1)














