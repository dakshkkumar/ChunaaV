from tkinter import *
from tkinter import ttk
import csv
import pandas as pd


def result():
    resultRoot = Tk()

    studentDetails = pd.read_csv("StuData.csv")
    studentDetails.set_index("AdNo", inplace=True)

    allWinners = Frame(resultRoot)
    allWinners.pack()
    Label(resultRoot, text='All Winners!', font=('Britannic Bold', 35),bg='#3AAFA9',fg='gold').place(
        relx=0.5, rely=0.07, anchor=CENTER)
    
    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview.Heading',rowheight=40,font=('Impact',30),background='green')
    s.configure('Treeview',font=('Segoe UI Semibold',13),rowheight=25)
    allEntries = ttk.Treeview(allWinners,height=20)
    allEntries['columns'] = ('Position', 'Ruling', 'Opposition')
    allEntries.column("#0", width=0,  stretch=NO)
    allEntries.column("Position", anchor=CENTER, width=400)
    allEntries.column("Ruling", anchor=CENTER, width=400)
    allEntries.column("Opposition", anchor=CENTER, width=400)

    allEntries.heading("#0", text="", anchor=CENTER)
    allEntries.heading("Position", text="Position", anchor=CENTER)
    allEntries.heading("Ruling", text="Ruling", anchor=CENTER)
    allEntries.heading("Opposition", text="Opposition", anchor=CENTER)
    allWinners.place(x=100, y=100)
    y = 1
    with open('CandData.csv') as candDetails:
        candidates = list(csv.reader(candDetails))
        for item in candidates[1:]:
            if int(item[2]) > int(item[4]):
                r = 1
                o = 3
            else:
                r = 3
                o = 1
            allEntries.insert(parent='', index='end', iid=y, text='',
                              values=(item[0], studentDetails.loc[int(item[r])]['Name']+' ('+str(item[r])+')', studentDetails.loc[int(item[o])]['Name']+' ('+str(item[o])+')'))
            y += 1
            allEntries.pack()

    Button(resultRoot, text='Back', command=resultRoot.destroy).place(
        relx=0.9, rely=0.02)
    
    Button(resultRoot,text='Save as pdf', command=None, background='#0000FF', foreground='white', activebackground='#82CAFF',activeforeground='white',font=('Arial',16),border=0,cursor='hand2').place(relx=0.45,rely=0.9)
    resultRoot.attributes('-fullscreen', True)
    resultRoot.configure(bg='#3AAFA9')
    resultRoot.mainloop()


result()
