from tkinter import *
from tkinter import ttk

root = Tk()

tree = ttk.Treeview(root)

tree["columns"] = ("one", "two")
tree.column("one", width=150)
tree.column("two", width=100)
tree.heading("one", text="column A")
tree.heading("two", text="column B")


### insert format -> insert(parent, index, iid=None, **kw)
### reference: https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview
tree.insert("", 0, text="Line 1", values=("1A", "1b"))
tree.insert("", "end", text="sub dir 2", values=("2A", "2B"))
x = [(1, 1001, 'Admin', 'Content 1', 'Title 1'), (2, 10012225, 'ivan', 'Content Ivan content 2 2 2 ', 'Ivan Title 2'), (3, 100122258521, 'ivan', 'COntent Ivan content 3 3 3', 'Title 3 Ivan '), (4, 10019288, 'user2', 'Content user2 chapter 2 2 2 2 ', 'user 2 Title chapter 2'), (5, 100192899632, 'user2', 'Content user2 chapter 3 3 3 3 ', 'User 2 Title 3'), (6, 10012015, 'user3', 'Content Chapter 2 user 3 Content  ', 'Title Chapter 2 user 3'), (7, 100120161781, 'user3', 'Content 3 User 3 Chapter 3', 'Title 3 User 3 Chapter 3'), (8, 1001222585221529, 'user2', 'CONTENT OF CHAPTER 4 IT CONTINUE CHAPTER # OF IVAN ', 'user2 TITLE 4 continue 3-ivan')]
d2 = tree.insert("", "end", "dir2", text="Dir 2")
tree.insert("", END, values='1')
for i in x:
    tree.insert(d2, "end", text=i[2], values=(i[4], "2B"))
    tree.move(d2, i[2], "end" )
    #tree.insert(id2, "end", text="sub dir 2-2", values=("2A-2", "2B-2"))
    print(i[2],i[1],i[4])
### insert sub-item, method 1
#id2 = tree.insert("", "end", "dir2", text="Dir 2")
#tree.insert(id2, "end", text="sub dir 2-1", values=(x, "2B"))
#tree.insert(id2, "end", text="sub dir 2-2", values=("2A-2", "2B-2"))

### insert sub-item, method 2
#tree.insert("", "end", "dir3", text="Dir 3")
#tree.insert("dir3", "end", text=" sub dir 3", values=("3A", "3B"))

tree.pack()
root.mainloop()