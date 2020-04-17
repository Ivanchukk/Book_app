import tkinter as tk
from dominio.entidades import *
# from menu.principal import *
from logindb import *
from tkinter import ttk, messagebox, PhotoImage
from book_1 import *

main = tk.Tk()
db = Database('login_db.db')


#### Login UI with tkinter
class MainWindow(Usuario):
    def __init__(self, root):
        # Login window
        root.title('Login')
        root.iconbitmap('image/login.ico')
        root.geometry("300x500")
        root.resizable(0, 0)
        #########centered screen##############
        root.update_idletasks()
        width = root.winfo_width()
        frm_width = root.winfo_rootx() - root.winfo_x()
        win_width = width + 2 * frm_width
        height = root.winfo_height()
        titlebar_height = root.winfo_rooty() - root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = root.winfo_screenwidth() // 2 - win_width // 2
        y = root.winfo_screenheight() // 2 - win_height // 2
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        root.deiconify()

        # Log in label enetry and button UI
        self.username = tk.StringVar()
        label_user = tk.Label(root, text="Username", font=("Arial", 12)).place(x=35, y=210)
        entry_user = tk.Entry(root, width=40, textvariable=self.username).place(x=35, y=240)

        self.password = tk.StringVar()
        label_pass = tk.Label(root, text="Password", font=("Arial", 12)).place(x=35, y=270)
        entry_user = tk.Entry(root, width=40, textvariable=self.password, show="*").place(x=35, y=300)

        button_login = tk.Button(root, text="Login", font=("Arial", 12), command=self.login).place(x=35, y=350)
        button_register = tk.Button(root, text="Register", font=("Arial", 12), command=self.registry).place(x=210,
                                                                                                            y=350)

    # check if user name and pasword correct
    def login(self):
        user_name = self.username.get()
        password = self.password.get()
        # look for user name and password in login data base
        user_name_password_db_get = db.details_check(user_name, password)
        # user name and password confarmation adn message box if incorect login details
        try:
            if user_name_password_db_get[0][2] == user_name and user_name_password_db_get[0][3] == password:
                New_page(user_name)
        except (TypeError, IndexError):
            messagebox.showerror(title="Wrong details", message="Wrong Password or User name")

    # Top level window with registration form
    def registry(self):
        # UI layout
        self.registry_win = tk.Toplevel()
        self.registry_win.title('Registry')
        self.registry_win.iconbitmap('image/register.ico')
        self.registry_win.geometry("300x350")
        self.registry_win.resizable(0, 0)

        title_label = tk.Label(self.registry_win, text="Registry", font=("Arial", 20), fg="black").place(x=90,
                                                                                                         y=0)
        self.email = tk.StringVar()
        email_label = tk.Label(self.registry_win, text="Email:", font=("Arial", 12)).place(x=20, y=50)
        email_entry = tk.Entry(self.registry_win, width=30, textvariable=self.email).place(x=100, y=51)

        self.username = tk.StringVar()
        user_label = tk.Label(self.registry_win, text="Username:", font=("Arial", 12)).place(x=20, y=90)
        user_entry = tk.Entry(self.registry_win, width=30, textvariable=self.username).place(x=100, y=91)

        self.password = tk.StringVar()
        pass_label = tk.Label(self.registry_win, text="Password:", font=("Arial", 12)).place(x=20, y=130)
        pass_entry = tk.Entry(self.registry_win, width=30, textvariable=self.password, show="*").place(x=100, y=131)

        button_new = tk.Button(self.registry_win, text="New", font=("Arial", 12), command=self.new).place(x=20, y=200)

        button_registry_sql = tk.Button(self.registry_win, text="Register", font=("Arial", 12),
                                        command=self.check_if_new).place(x=210,
                                                                         y=200)

    # Checking if the user name or the password in use or not if in use popup showerror messagebox
    def check_if_new(self):
        email = self.email.get()
        user_name = self.username.get()
        password = self.password.get()
        if email == "" or user_name == "" or password == "":
            messagebox.showerror(title="Incomplete data", message="Fill in the data")
        else:
            username_email_in_db = db.check_userName_password(email, user_name)
        if username_email_in_db == []:
            db.register_sql(email, user_name, password)
            self.registry_win.destroy()
        else:
            messagebox.showerror(title="Mail or User Name in use", message="Mail or User Name in use")

    #Adding user name to log in data base
    def reg_client(self):
        email = self.email.get()
        user_name = self.username.get()
        password = self.password.get()
        if email == "" or user_name == "" or password == "":
            messagebox.showerror(title="Incomplete data", message="Fill in the data")
            g = db.check_userName_password(email, user_name)
            db.register_sql(email, user_name, password)
            self.registry_win.destroy()

    def new(self):
        get_entry = self.email.get()
        get_entry_data = db.search_c()


window = MainWindow(main)
main.mainloop()
