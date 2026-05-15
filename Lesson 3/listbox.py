from tkinter import *

root=Tk()
root.title("my favorite food")

list=Listbox(root,height=10,width=15,bg="grey",activestyle="dotbox",font="Helvetica",fg="yellow")
label=Label(root,text="Food Items")
list.insert(1,"Nachos")
list.insert(2,"pizza")
list.insert(3,"steak")
list.insert(4,"mac and cheese")
list.insert(5,"rice")
label.pack()
list.pack()
root.mainloop()