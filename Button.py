from tkinter import *

root=Tk()

def clicked():
    myLable=Label(root,text="Hello you Clicked Button ").grid(row=2,column=3)
#state
myButton=Button(root,text="Newone",state=DISABLED).grid(row=0,column=0)
#padx
myButton=Button(root,text="Newone",padx=20,command=clicked).grid(row=0,column=1)
#pady
myButton=Button(root,text="Newone",pady=20).grid(row=0,column=2)



root.mainloop()