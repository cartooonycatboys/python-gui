from tkinter import *

root=Tk()
root.geometry("300x300")
root.config(background="pink")

username=Label(root,text="username").place(x=40,y=60)
password=Label(root,text="password").place(x=40,y=90)


Btn=Button(root,text="submit",bd="5",background="cyan",command=root.destroy).place(x=40,y=120)

uinput=Entry(root,width=30).place(x=110,y=60)
pinput=Entry(root,width=30).place(x=110,y=90)
root.mainloop()

