from tkinter import *

root=Tk()
root.geometry("300x300")

Btn=Button(root,text="STOP",bd="5",background="red").place(x=150,y=0)


Btn2=Button(root,text="WAIT",bd="5",background="yellow").place(x=150,y=150)


Btn3=Button(root,text="GO  ",bd="5",background="green").place(x=150,y=270)


root.mainloop()