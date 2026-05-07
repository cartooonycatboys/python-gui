from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("menu demonstration")

Menubar=Menu(root)

file=Menu(Menubar,tearoff=0)
Menubar.add_cascade(label="File",menu=file)
file.add_command(label="new file",command=None)
file.add_command(label="Open",command=None)
file.add_command(label="Save",command=None)
file.add_separator()
file.add_command(label="Exit",command=root.destroy)
root.config(menu=Menubar)

edit=Menu(Menubar,tearoff=0)
Menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut",command=None)
edit.add_command(label="Copy",command=None)
edit.add_command(label="Paste",command=None)
edit.add_command(label="Select all",command=None)
edit.add_separator()
edit.add_command(label="Find",command=None)
edit.add_command(label="Find all",command=None)

help_ = Menu(Menubar, tearoff=0)
Menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)

root.mainloop()