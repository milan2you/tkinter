from tkinter  import *
#Grid view first
root =Tk()
#creating a lable widget 
myLablel1=Label(root,text="Hello World!")
myLablel2=Label(root,text="Hello World!")
myLablel3=Label(root,text="*********").grid(row=1,column=1)
#shoving it onto the screen
myLablel1.grid(row=0,column=0)
myLablel2.grid(row=1,column=5)

root.mainloop()