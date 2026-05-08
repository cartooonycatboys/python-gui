from tkinter import *
from tkinter.ttk import *
import time

root=Tk()
Progress=Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate')
Progress.pack(pady=10)
def bar():
    Progress["value"]=20
    root.update_idletasks()
    time.sleep(1)

    Progress["value"]=40
    root.update_idletasks()
    time.sleep(1)

    Progress["value"]=50
    root.update_idletasks()
    time.sleep(1)

    Progress["value"]=60
    root.update_idletasks()
    time.sleep(1)

    Progress["value"]=80
    root.update_idletasks()
    time.sleep(1)

    Progress["value"]=100


Button(root,text="Start",command=bar).pack(padx=10,pady=10)

root.mainloop()