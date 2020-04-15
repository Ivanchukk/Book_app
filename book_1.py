import tkinter as tk
from dominio.entidades import *
#from menu.principal import *
from logindb import *
from tkinter import ttk, messagebox, PhotoImage
from bookDB import *
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

        self.frame = tk.Frame(popup)
        self.frame.grid(row=3, column=1)



    def creat_new_chap(self):
        write_chapter = tk.Toplevel()
        # Chapter name
        self.chapter_name1 = tk.StringVar()
        self.chapter_name = tk.Entry(write_chapter, textvariable=self.chapter_name1)
        self.chapter_name.grid(row=1,column=1)
        #text box
        self.writer_entry = tk.Text(write_chapter, height=10,width=50)
        self.writer_entry.grid(row=3,column=1)

        btn = tk.Button(write_chapter,text="save", command=lambda: self.retrieve_input())
        btn.grid(row=4,column=1)

    def retrieve_input(self):
        inputValue = self.writer_entry.get("1.0", "end-1c")
        x = book_DB.add_chapter_master(self.user_name, inputValue ,self.chapter_name1.get())

        print(self.chapter_name1.get())

    def go_to_first_chapter(self):
        #book_DB.frst_chapter("ivan", "hjdsjkahdaskjhdkjasdhklasjdkalshdwjkhqwhjkvcxklbhsfidou uiaw asjk sajfhas fasdlkjf hasl wepior qoi askj dhlui weiup hksjadfn l;a fhweu gfas lh fwui fg sadjlf asif uas fglj hqw; j hkjlasf haf halsjdkfh alsjk hqwuil jf")

        get_frst_c = book_DB.frst_chapter(0)
        frst_c = tk.Label(self.frame, text = get_frst_c)
        frst_c.grid(row=2,column=1)

        create_chapter_btn = tk.Button(self.frame,text="create next chapter", command = self.creat_new_chap)
        create_chapter_btn.grid(row=3,column=1)


        #print(get_frst_c)



    def user_chapter_def(self):

        self.radionvar = tk.StringVar()
        x = book_DB.frst_chapter(self.user_name)
        #frst_c = tk.Label(self.frame, text=x)
        #frst_c.grid(row=4, column=1)
        #print(x)
        self.n=5

        for p in x:
            a = tk.Radiobutton(self.frame, text=p[3], variable=self.radionvar, value=p[3],tristatevalue=0)
            a.grid(row=self.n, column=1)
            self.n += 1

        go_to_chapter_btn = tk.Button(self.frame, text="go to chapter", command=lambda: self.print_radio())
        go_to_chapter_btn.grid(row=self.n+1,column=1)



    def print_radio(self):
        x = book_DB.frst_chapter(self.radionvar.get())
        first_chapter_level = tk.Toplevel()

        self.chosen_chapter = tk.Text(first_chapter_level, height=10, width=50)
        self.chosen_chapter.grid(row=3, column=1)


        self.chosen_chapter.insert(tk.INSERT,x)
        self.chosen_chapter.config(state="disabled")

        mylabel = tk.Label(self.frame, text=self.radionvar.get())
        mylabel.grid(row=self.n + 2, column=1)






    def all_chepters_def(self):
        return














