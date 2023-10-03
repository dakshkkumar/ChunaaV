from tkinter import *
from tkinter import ttk
import pandas as pd
import csv

def runStudent(id):
    studentRoot = Toplevel()

    Label(studentRoot,text=id,border=0,pady=0,bg='#3AAFA9',fg='#FFF2CC',font=('Britannic Bold',50)).place(relx=0.5,rely=0.08,anchor=CENTER)


    with open('StuData.csv') as studentDetails:
        students=csv.reader(studentDetails)
        for data in students:
            if data[0]==str(id):
                Label(studentRoot, text='Hi '+data[2]+',', border=0,pady=0,bg='#3AAFA9',fg='#FFF2CC',font=('Britannic Bold',50)).place(relx=0.5,rely=0.5)




    quit = Button(studentRoot, text="Logout",
                    command=studentRoot.destroy)
    quit.place(relx=0.9, rely=0.02)

    studentRoot.attributes('-fullscreen', True)
    studentRoot.configure(bg='#3AAFA9')
    studentRoot.mainloop()