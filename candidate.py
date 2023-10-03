from tkinter import *
from tkinter import ttk
import pandas as pd
import csv

newCandidates = []
position=None
cand1=None
cand2=None
candRoot=None
canvas=None


def addAnother():
    global newCandidates
    global position
    global cand1
    global cand2
    global canvas

    stuDetails=pd.read_csv('StuData.csv')
    print(cand1.get())
    if (int(cand1.get()) in stuDetails['AdNo'].tolist() and int(cand2.get()) in stuDetails['AdNo'].tolist()):
        current = []
        current.append(position.get())
        current.append(cand1.get())
        current.append(0)
        current.append(cand2.get())
        current.append(0)
        newCandidates.append(current)
        current = []
        position.delete(0, 'end')
    else:
        error=canvas.create_text(
            680, 400, text='*Invalid Entry*', fill='red', font=('Helvetica', 15))
        position.delete(0, 'end')
    cand1.delete(0, 'end')
    cand2.delete(0, 'end')

def done():
    global newCandidates
    global candRoot

    candidateFile = open('CandData.csv', 'a', newline='')
    stuDetails=pd.read_csv('StuData.csv')

    if (int(cand1.get()) in stuDetails['AdNo'].tolist() and int(cand2.get()) in stuDetails['AdNo'].tolist()):
        current = []
        current.append(position.get())
        current.append(cand1.get())
        current.append(0)
        current.append(cand2.get())
        current.append(0)
        newCandidates.append(current)
        current = []

    doneRoot = Tk()
    doneRoot.geometry('500x350')
    allDetails=Frame(doneRoot)
    allDetails.pack()
    Label(doneRoot,text='All new candidates',font=('Futura',25)).place(relx=0.5,rely=0.07,anchor=CENTER)
    Button(doneRoot,text='Okay!',command=lambda:(doneRoot.destroy(),candRoot.destroy())).place(relx=0.5,rely=0.9,anchor=CENTER)
    allEntries=ttk.Treeview(allDetails)
    allEntries['columns']=('Position','Candidate 1','Candidate 2')
    allEntries.column("#0", width=0,  stretch=NO)
    allEntries.column("Position",anchor=CENTER, width=80)
    allEntries.column("Candidate 1",anchor=CENTER,width=150)
    allEntries.column("Candidate 2",anchor=CENTER,width=250)

    allEntries.heading("#0",text="",anchor=CENTER)
    allEntries.heading("Position",text="Position",anchor=CENTER)
    allEntries.heading("Candidate 1",text="Candidate 1",anchor=CENTER)
    allEntries.heading("Candidate 2",text="Candidate 2",anchor=CENTER)
    allDetails.place(x=10,y=50)
    y = 1
    writer = csv.writer(candidateFile)
    for item in newCandidates:
        writer.writerow(item)
        allEntries.insert(parent='',index='end',iid=y,text='',
                        values=(item[0],item[1],item[3]))
        y+=1
        allEntries.pack()


####### Driver Function #######
def candidate():
    global position
    global cand1
    global cand2
    global canvas

    candRoot = Toplevel()
    voterBg = PhotoImage(file='candBg.png')

    canvas = Canvas(candRoot)
    canvas.create_image(0, 0, image=voterBg, anchor=NW)
    canvas.create_text(680, 50, text="Add Candidate", fill='black',
                        font=('Britannic Bold', 50))
    canvas.pack(fill='both', expand=True)

    canvas.create_text(480, 150, text='POSITION:',
                        fill='blue', font=('Helvetica', 20))
    position = Entry(candRoot, fg='white', bg='grey', width=30, border=0,
                    font=('Microsoft YaHei UI Light', 25))
    position.place(relx=0.5, rely=0.265, anchor=CENTER)


    canvas.create_text(550, 330, text='Candidate 1 (Admission No.):',
                        fill='blue', font=('Helvetica', 15))
    cand1 = Entry(candRoot, fg='black',bg='light grey', width=30, border=0,
                    font=('Microsoft YaHei UI Light', 18))
    cand1.place(relx=0.5, rely=0.48, anchor=CENTER)

    canvas.create_text(550, 430, text='Candidate 2 (Admission No.):',
                        fill='blue', font=('Helvetica', 15))
    cand2 = Entry(candRoot, fg='black',bg='light grey', width=30, border=0,
                    font=('Microsoft YaHei UI Light', 18))
    cand2.place(relx=0.5, rely=0.61, anchor=CENTER)
    

    Button(candRoot, text='Add another',
            command=addAnother,width=15,height=1,font=('Impact',20),pady=0,bg='#EA3323',fg='white').place(relx=0.4, rely=0.8,anchor=CENTER)

    Button(candRoot, text='Done', command=done,width=15,height=1,font=('Impact',20),pady=0,fg='#EA3323',bg='white').place(relx=0.6, rely=0.8,anchor=CENTER)

    Button(candRoot, text='Back', command=candRoot.destroy).place(
        relx=0.9, rely=0.02)
    candRoot.attributes('-fullscreen', True)
    candRoot.configure(bg='#3AAFA9')
    candRoot.mainloop()