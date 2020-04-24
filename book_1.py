import tkinter as tk
from KeyValidator import *
from tkinter.ttk import Combobox, Treeview, Scrollbar

book_DB = Book_Database('book_db.db')
from tkinter.ttk import Combobox, Treeview, Scrollbar


class New_page:
    def __init__(self, user_name):

        popup = tk.Toplevel(bg='#ccddff')
        popup.geometry(f'{500}x{700}')
        title = tk.Label(popup,
          text="{} welcome to our book".format(user_name.title()), bg='#ccddff', fg="#66b3ff",
                         font=("Courier bold", 28))
        title.place(x=45, y=15)
        self.user_name = user_name
        frst_c_btn = tk.Button(popup, text="read first chapter",bg='#b3d9ff', command=self.go_to_first_chapter)
        frst_c_btn.place(x=30, y=100)

        user_chapter = tk.Button(popup, text="Check your chapters",bg='#b3d9ff', command=self.user_chapter_def)
        user_chapter.place(x=175, y=100)

        all_chepters = tk.Button(popup, text="Check all chapters",bg='#b3d9ff', command=self.all_chepters_def3)
        all_chepters.place(x=350, y=100)

        self.frame_user_capters = tk.Frame(popup, bg='#ccddff')
        self.frame_all_user_capters = tk.Frame(popup)
        self.all_data = book_DB.show_all_chapters()

    def create_new_chap(self):
        try:
            self.read_first_chapter.withdraw()
        except AttributeError:
            self.first_chapter_level.withdraw()
        self.write_chapter = tk.Toplevel(bg='#ccddff')
        self.write_chapter.geometry(f'{1250}x{900}')
        self.write_chapter.title("New Chapter")
        self.chapter_name1 = tk.StringVar()
        self.chapter_name = tk.Entry(self.write_chapter, textvariable=self.chapter_name1, width=50)
        self.chapter_name.place(x=500,y=15)
        # text box
        self.writer_entry = tk.Text(self.write_chapter, height=50, width=150)
        self.writer_entry.place(x=20,y=50)
        # word counter
        self.write_chapter.bind("<space>", self.count_words)
        self.word_counter_label = tk.Label(self.write_chapter,bg='#ccddff', text="word count")
        self.word_counter_label.place(x=20,y=860)
        # Create button in Text window
        btn = tk.Button(self.write_chapter, text="save",bg='#b3d9ff', command=lambda: self.retrieve_input())
        btn.place(x=550,y=860)
        # word counter

    def count_words(self, event):
        repr(event.char)
        character_counter = self.writer_entry.get("1.0", "end-1c")
        count_words_in_box_text_live = len(character_counter.split())
        count_words_in_box_text_live_label = tk.Label(self.write_chapter,bg='#ccddff', text=count_words_in_box_text_live)
        count_words_in_box_text_live_label.place(x=120,y=860)
        # return count_words_in_box_text_live

    def retrieve_input(self):
        inputvalue = self.writer_entry.get("1.0", "end-1c")
        count_words_in_box_text = len(inputvalue.split())
        if count_words_in_box_text > 1 and self.chapter_name1.get() != '':
            try:
                key_1001_data = book_DB.frst_chapter(self.radionvar.get())
            except AttributeError:
                key_1001_data = book_DB.frst_chapter(1001)
            chapter_key = key_1001_data[0][1]
            chapter_user_name = key_1001_data[0][3]
            chapter_number = key_1001_data[0][2]

            if chapter_key == '1001':
                key = self.keyvalMaster()
            elif self.user_name == self.row_of_colled_chapter[0][3]:
                key = self.row_of_colled_chapter[0][1]
            #            elif chapter_user_name == self.user_name:
            #                key = chapter_key+1
            else:
                key = self.keyval_branch(self.row_of_colled_chapter[0][1])
            book_DB.add_chapter(str(key), chapter_number + 1, self.user_name, inputvalue, self.chapter_name1.get())
            self.write_chapter.destroy()
        else:
            tk.messagebox.showinfo(parent=self.write_chapter, title="Word count message",
                                   message="You have to write minimum of 1,500 words or no title")

    def go_to_first_chapter(self):
        self.read_first_chapter = tk.Toplevel(bg='#ccddff')
        self.read_first_chapter.geometry(f'{1250}x{900}')
        self.get_frst_c = book_DB.frst_chapter('1001')
        frst_chhapter_title = tk.Label(self.read_first_chapter,text=self.get_frst_c[0][5],bg='#ccddff',fg="#66b3ff",
                                       font=("bold 24"))
        frst_chhapter_title.place(x=500,y=5)
        first_chapter_text = tk.Text(self.read_first_chapter, height=50, width=150)
        first_chapter_text.place(x=20,y=50)
        first_chapter_text.insert(tk.INSERT, self.get_frst_c[0][4])
        first_chapter_text.config(state="disabled")
        # Create button - Next Chapter - in text window
        create_chapter_btn = tk.Button(self.read_first_chapter,bg='#b3d9ff', text="Write next chapter",
                                       command=self.create_new_chap)
        create_chapter_btn.place(x=1100,y=15)

    def user_chapter_def(self):
        self.frame_all_user_capters.grid_forget()
        self.frame_user_capters.place(x=185, y=150)
        self.radionvar = tk.StringVar()
        x = book_DB.frst_chapter(self.user_name)
        self.row_number = 20

        for p in x:
            a = tk.Radiobutton(self.frame_user_capters, bg = '#ccddff', text=p[5], variable=self.radionvar, value=p[5], tristatevalue=0)
            a.grid(row=self.row_number, column=0)
            self.row_number += 1
        go_to_chapter_btn = tk.Button(self.frame_user_capters,bg='#b3d9ff', text="go to chapter",font='bold',
                                      command=lambda: self.print_radio())
        go_to_chapter_btn.grid(row=self.row_number + 1, column=0)

    def print_radio(self):
        self.row_of_colled_chapter = book_DB.frst_chapter(self.radionvar.get())
        self.first_chapter_level = tk.Toplevel(bg='#ccddff')
        self.first_chapter_level.geometry(f'{1250}x{900}')
        self.first_chapter_level.title(self.row_of_colled_chapter[0][5])
        chosen_title = tk.Label(self.first_chapter_level,bg='#ccddff', text=self.radionvar.get(), font=("Arial", 12))
        chosen_title.place(x=600,y=5)
        self.chosen_chapter = tk.Text(self.first_chapter_level, height=50, width=150)
        self.chosen_chapter.place(x=20,y=50)
        self.chosen_chapter.insert(tk.INSERT, self.row_of_colled_chapter[0][4])
        self.chosen_chapter.config(state="disabled")

        # Check if this the chapter of the loged in user
        if self.user_name == self.row_of_colled_chapter[0][3]:
            edit_chapter_btn = tk.Button(self.first_chapter_level, bg='#b3d9ff', text="Edit", command=self.edit_chapter)
            edit_chapter_btn.place(x=1000,y=15)
        write_next__chapter_btn = tk.Button(self.first_chapter_level,bg='#b3d9ff', text="write next chapter",
                                            command=self.create_new_chap)
        write_next__chapter_btn.place(x=1100,y=15)

    def edit_chapter(self):
        self.chosen_chapter.config(state="normal")
        btn_save = tk.Button(self.first_chapter_level,bg='#b3d9ff', text="save",
                             command=lambda: self.retrieve_input_edit())
        btn_save.place(x=950,y=15)

    def retrieve_input_edit(self):
        edited_chapter = self.chosen_chapter.get("1.0", "end-1c")
        book_DB.edit_chapter_db(edited_chapter, self.user_name, self.radionvar.get())
        self.first_chapter_level.destroy()

  #  def open_next_branch(self, key):
  #      self.row_number += 1
   #     self.column_number = 0
  #      self.rradionvar = tk.StringVar()
  #      key_str = str(key)
   #     key_str_len_minus_1 = key_str[:-1]
   #     key_str_len = len(key_str)
   #     next_branch = book_DB.filter_new_branch(key_str, key_str_len_minus_1, key_str_len)
   #     for p in next_branch:
   #         bb = tk.Radiobutton(self.frame_all_user_capters, text="this is Second first chapter {}".format(p[4]),
   #                             indicatoron=0, variable=self.rradionvar, value=p[1], tristatevalue=0,
  #                              command=lambda: self.open_next_branch(self.rradionvar.get()))
  #          bb.grid(row=self.row_number, column=self.column_number, sticky='W')
  #          self.column_number += 1
   #     self.column_number -= 1

  #  def open_next_branch_2(self):
   #     self.frame_all_user_capters.grid_forget()
   #     self.row_number += 1
   #     self.column_number = 0
   #     key = self.rradionvar.get()
  #      key_str = str(key)
   #     key_str_len_minus_1 = key_str[:-1]
    #    key_str_len = len(key_str)
   #     next_branch = book_DB.filter_new_branch(key_str, key_str_len_minus_1, key_str_len)
  #      for p in next_branch:
  #          bb = tk.Radiobutton(self.frame_all_user_capters, text=p[4], indicatoron=0, variable=self.rradionvar,
   #                             value=p[1], tristatevalue=0, command=self.open_next_branch_2)
   #         bb.grid(row=self.row_number, column=self.column_number, sticky='W')
    #        self.column_number += 1

  #  def all_chepters_def(self):
  #      self.frame_user_capters.grid_forget()
  #      self.frame_all_user_capters.grid(row=3, column=1)
 #       self.radionvar = tk.StringVar()
  #      x = book_DB.show_all_chapters()
  #      # Making separated column for each user
  #      lst_unique = []
 #       for m in x:
  #          if m[3] not in lst_unique:
  #              print(m[3])
  #              lst_unique.append(m[3])
  #      print(lst_unique)
 #       lng = len(lst_unique)
 #       print(lng)
  #      counter = 0
  #      zoro = 0
  #      while counter < lng:
# #           n = 5
         #   for i in x:
        #        if lst_unique[counter] in i:
       #             a = tk.Radiobutton(self.frame_all_user_capters, text="chapter {}".format(i[1]),
      #                                 variable=self.radionvar, value=i[5],
     #                                  tristatevalue=0)
    #                a.grid(row=n, column=counter, sticky='W')
   #                 n += 1
  #          counter += 1
       # zzz = 5
       # for p in x:
      #      bb = tk.Button(self.frame_all_user_capters, text=" this is {}\n {}".format(p[1], p[5]),
     #                      command=self.open_next_branch)
    #        bb.grid(row=zzz, column=11, sticky='W')
   #         a = tk.Label(self.frame_all_user_capters, text=p[1])
  #          a.grid(row=zzz, column=10, sticky='W')
 #           zzz += 1

      #  go_to_chapter_btn = tk.Button(self.frame_all_user_capters, text="go to chapter",
     #                                 command=lambda: self.print_radio())
    #    go_to_chapter_btn.grid(row=n + 1, column=1)

   # def all_chepters_def2(self):
  #      ffff = tk.Toplevel()
 #       x = book_DB.muduul()
#
     #   column = 0
    #    row = 1
   #     for i in x:
  #          if i[2] == row:
 #               bb = Label(ffff, text=i[5])
#                bb.grid(row=i[2], column=column)
      #3          row += 1
     #       else:
    #            column += 1
   #             bb = Label(ffff, text=i[5])
  #              bb.grid(row=i[2], column=column)
 #               row += 1
#                column -= 1

    def all_chepters_def3(self):
        ffff = tk.Toplevel(bg='#ccddff')
        ffff.geometry(f'{1200}x{700}')
        all_keys = book_DB.all_kyes_in_db()
        lst_keys = []
        for i in all_keys:
            if i not in lst_keys:
                lst_keys.append(i[0])
        lst_keys_sort = []
        for i in self.lst_maker(lst_keys):
            z = book_DB.filter_new_branch2(i)
            for ii in z:
                if ii not in lst_keys_sort:
                    lst_keys_sort.append(ii[1])

        clm = 0
        lng = 4
        self.radionvar = tk.StringVar()
        for i in self.lst_maker(lst_keys_sort):
            spesific_user_info = book_DB.frst_chapter(i)
            for ii in spesific_user_info:
                btn_read_chapter = tk.Radiobutton(ffff, text="{}\nWriten by {}".format(ii[5],ii[3]), bg='#b3d9ff', indicatoron=0, variable=self.radionvar, value=ii[1],
                                                  tristatevalue=0, command=lambda: self.print_radio())
                btn_read_chapter.grid(row=ii[2], column=clm)
            clm += 1
            lng += 4

    def lst_maker(self,lst):
        lst_keys_unique = []
        for i in lst:
            if i not in lst_keys_unique and len(i) > 4:
                lst_keys_unique.append(i)
        return lst_keys_unique

    def keyvalMaster(self):
        self.lst = book_DB.all_kyes_in_db()
        self.lst_1 = self.lst[0][0]
        self.lst_2 = []
        # create list of strings
        for i in self.lst:
            self.lst_2.append(i[0])
        global new_key
        # Checking that new key have difference of 100 for all the other keys
        t = True
        x = int(randint(1000, 9900))
        while t:
            if all(abs(int(ii) - x) > 100 for ii in self.lst_2):
                new_key = int("%s%s" % (self.lst_2[0], x))
                t = False
        return new_key

    def keyval_branch(self,key_not_1001):
        self.lst = book_DB.all_kyes_in_db()
        self.lst_1 = self.lst[0][0]
        self.lst_2 = []
        key_not_1001 = str(int(key_not_1001) + 1)
        t = True
        x = int(randint(1000, 9900))
        while t:
            if all(abs(ii - x) > 100 for ii in self.lst_2):
                new_key = int("%s%s" % (key_not_1001, x))
                t = False
        return new_key



