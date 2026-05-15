from tkinter import *
from tkinter.ttk import *

root=Tk()
root.geometry("300x150")

w=Label(root,text="chocos and icecreames",font="50")
w.pack()

frame=Frame(root)
frame.pack()

b1_button=Button(frame,text="choco")
b1_button.pack(side=LEFT)

b2_button=Button(frame,text="dark choco")
b2_button.pack(side=LEFT)

b3_button=Button(frame,text="white choco")
b3_button.pack(side=LEFT)

frame2=Frame(root)

b4_button=Button(frame2,text="choco")
b4_button.pack(side=LEFT)

b5_button=Button(frame2,text="dark choco")
b5_button.pack(side=LEFT)

b6_button=Button(frame2,text="white choco")
b6_button.pack(side=LEFT)
frame.pack(side=BOTTOM)
root.mainloop()