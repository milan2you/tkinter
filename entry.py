from tkinter import *

root=Tk()
entone=""
ent=Entry(root,width=50,textvariable=entone )
ent.grid(row=0,column=0)


def afterClick():
    hello="hello"+ ent.get()
    myLable=Label(root,text=hello)
    myLable.grid(row=3,column=0)

myButton =Button(root,text="Click Me",command=afterClick).grid(row=1,column=0)



root.mainloop()