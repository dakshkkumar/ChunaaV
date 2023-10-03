from tkinter import *
from tkinter import ttk
import csv

newCandidates = []

def genPass(AdNo, name):
    fullname=name.split(' ')
    revAd = AdNo[::-1]
    passw = fullname[0]+revAd
    return passw

def addAnother():
    global newCandidates
    if (AdNo.get() != '' and int(AdNo.get()) in range(1000, 10000)) and all(map(lambda x: x.isalpha(), name.get().split())):
        current = []
        current.append(AdNo.get())
        current.append(genPass(AdNo.get(), name.get()))
        current.append(name.get())
        current.append('FALSE')
        newCandidates.append(current)
        current = []
        AdNo.delete(0, 'end')
        name.delete(0, 'end')
    else:
        error=canvas.create_text(
            680, 400, text='*Invalid Entry*', fill='red', font=('Helvetica', 15))
        AdNo.delete(0, 'end')
        name.delete(0, 'end')

def done():
    global newCandidates
    candidateFile = open('stuData.csv', 'a', newline='')

    if (AdNo.get() != '' and int(AdNo.get()) in range(1000, 10000)) and all(map(lambda x: x.isalpha(), name.get().split())):
        current = []
        current.append(AdNo.get())
        current.append(genPass(AdNo.get(), name.get()))
        current.append(name.get())
        current.append('FALSE')
        newCandidates.append(current)
        AdNo.delete(0, 'end')
        name.delete(0, 'end')
        current = []

    doneRoot = Tk()
    doneRoot.geometry('500x350')
    allDetails=Frame(doneRoot)
    allDetails.pack()
    Label(doneRoot,text='All new voters',font=('Futura',25)).place(relx=0.5,rely=0.07,anchor=CENTER)
    Button(doneRoot,text='Okay!',command=lambda:(doneRoot.destroy(),candRoot.destroy())).place(relx=0.5,rely=0.9,anchor=CENTER)
    allEntries=ttk.Treeview(allDetails)
    allEntries['columns']=('stuId','Passw','Name')
    allEntries.column("#0", width=0,  stretch=NO)
    allEntries.column("stuId",anchor=CENTER, width=80)
    allEntries.column("Passw",anchor=CENTER,width=150)
    allEntries.column("Name",anchor=CENTER,width=250)

    allEntries.heading("#0",text="",anchor=CENTER)
    allEntries.heading("stuId",text="Id",anchor=CENTER)
    allEntries.heading("Passw",text="Password",anchor=CENTER)
    allEntries.heading("Name",text="Name",anchor=CENTER)
    allDetails.place(x=10,y=50)
    y = 1
    writer = csv.writer(candidateFile)
    for item in newCandidates:
        writer.writerow(item)
        allEntries.insert(parent='',index='end',iid=y,text='',
                        values=(item[0],item[1],item[2]))
        y+=1
        allEntries.pack()


def candidate():
    candRoot = Toplevel()
    voterBg = PhotoImage(file='candBg.png')

    canvas = Canvas(candRoot)
    canvas.create_image(0, 0, image=voterBg, anchor=NW)
    canvas.create_text(680, 50, text="Add Candidate", fill='black',
                        font=('Britannic Bold', 50))
    canvas.pack(fill='both', expand=True)

    canvas.create_text(400, 200, text='Admission Number:',
                        fill='blue', font=('Helvetica', 20))
    AdNo = Entry(candRoot, fg='black', width=30, border=0,
                    font=('Microsoft YaHei UI Light', 11))
    AdNo.place(relx=0.5, rely=0.265, anchor=CENTER)

    canvas.create_text(480, 330, text='Name:',
                        fill='blue', font=('Helvetica', 20))
    name = Entry(candRoot, fg='black', width=30, border=0,
                    font=('Microsoft YaHei UI Light', 11))
    name.place(relx=0.5, rely=0.435, anchor=CENTER)

    Button(candRoot, text='Add another',
            command=addAnother,width=15,height=1,font=('Impact',20),pady=0,bg='#EA3323',fg='white').place(relx=0.8, rely=0.25,anchor=CENTER)

    Button(candRoot, text='Done', command=done,width=15,height=1,font=('Impact',20),pady=0,fg='#EA3323',bg='white').place(relx=0.8, rely=0.45,anchor=CENTER)

    Button(candRoot, text='Back', command=candRoot.destroy).place(
        relx=0.9, rely=0.02)
    candRoot.attributes('-fullscreen', True)
    candRoot.configure(bg='#3AAFA9')
    candRoot.mainloop()

