from tkinter import *
from tkinter import font
from tkinter import ttk
root=Tk()
list=list(font.families())
v=Scrollbar(root,orient='vertical')
poy=0.01
pox=0.01
count=0
for x in list:
    y=ttk.Label(root,text=x,font=(x,12))
    y.place(relx=pox,rely=poy)
    poy+=0.05
    count+=1
    if count==20:
        pox+=0.2
        count=0
        poy=0.01
root.mainloop()