from tkinter import *
from tkinter import ttk
import pandas as pd
import time
import csv
import student




def thank(chosen):
    global votingRoot
    votingRoot.destroy()
    chosenRoot = Toplevel()
    chosenBg = PhotoImage(file='casted.png')
    thankBg=PhotoImage(file='thankImage.png')

    canvas = Canvas(chosenRoot)
    image=canvas.create_image(0, 0, image=chosenBg, anchor=NW)
    textBox=canvas.create_text(640, 310, text=chosen, fill='black',
                        font=('Lucida Handwriting', 25),angle='37')
        
    chosenRoot.after(1000,canvas.delete,image)
    chosenRoot.after(1000,lambda:(canvas.create_image(0, 0, image=thankBg, anchor=NW)))
    chosenRoot.after(1000,lambda: canvas.itemconfig(textBox,text='Thank you',font=('Britannic Bold',30),angle=0))
    canvas.pack(fill='both', expand=True)
    chosenRoot.attributes('-fullscreen', True)
    chosenRoot.configure(bg='#3AAFA9')
    chosenRoot.after(3500, chosenRoot.destroy)
    chosenRoot.mainloop()



def casted(chosen):
    global i
    global votingRoot
    i += 1
    chosenRoot = Toplevel()
    chosenBg = PhotoImage(file='casted.png')

    canvas = Canvas(chosenRoot)
    canvas.create_image(0, 0, image=chosenBg, anchor=NW)
    canvas.create_text(640, 310, text=chosen, fill='black',
                       font=('Lucida Handwriting', 25),angle='37')
    canvas.pack(fill='both', expand=True)
    chosenRoot.attributes('-fullscreen', True)
    chosenRoot.configure(bg='#3AAFA9')
    chosenRoot.after(1000, chosenRoot.destroy)
    chosenRoot.mainloop()


def change(n, which):
    global candidates
    global votingRoot
    global pos
    global i
    global cand1
    global cand2
    global studentDetails
    global Details
    global numbering
    global canvas

    # casted(studentDetails.loc[int(candidates[i][which-1])]['Name'])
    Details.iloc[n-2, which] = int(1+Details.iloc[n-2][which])
    Details.to_csv('CandData.csv', index=False)

    try:
        pos.config(text=candidates[n][0])
        cand1.config(text=studentDetails.loc[int(candidates[n][1])]['Name'])
        cand2.config(text=studentDetails.loc[int(candidates[n][3])]['Name'])
        numbering.config(text=str(n)+'/'+str(len(candidates)-1))
        # canvas.itemconfig(pos, text=candidates[n][0])
        casted(studentDetails.loc[int(candidates[i][which-1])]['Name'])
    except:
        thank(studentDetails.loc[int(candidates[i][which-1])]['Name'])


def votingData(id,root):
    global votingRoot
    global candidates
    global pos
    global i
    i = 1
    global canvas
    global cand1
    global numbering
    global cand2
    global studentDetails
    global Details
    
    root.destroy()

    studentDetails = pd.read_csv("StuData.csv",index_col='AdNo')

    studentDetails.at[id,'HasVoted']=True
    studentDetails.to_csv('StuData.csv')

    Details = pd.read_csv("CandData.csv")

    votingRoot = Toplevel()

    votingBg = PhotoImage(file='votingBg.png')



    canvas = Canvas(votingRoot)
    canvas.create_image(0, 0, image=votingBg, anchor=NW)

    canvas.pack(fill='both', expand=True)

    with open('CandData.csv') as candDetails:
        candidates = list(csv.reader(candDetails))

        # pos=canvas.create_text(720, 580, text=candidates[i][0], fill='black',
        #     font=('Britannic Bold', 50))
        pos = Label(votingRoot, text=candidates[i][0], font=(
            'Britannic Bold', 50),bg='#fcd232',fg='#36599a')
        pos.place(relx=0.53, rely=0.8,anchor=CENTER)

        numbering=Label(votingRoot, text=str(i)+'/'+str(len(candidates)-1),font=('Britannic Bold',35),fg='#fcd232',bg='#36599a')
        numbering.place(relx=0.05,rely=0.05)

        cand1 = Button(
            votingRoot, text=studentDetails.loc[int(candidates[i][1])]['Name'], command=lambda: change(i+1, 2),bg='#fcd232',border=0, font=('Impact',20),cursor='hand2',activebackground='#fcd232')
        cand1.place(relx=0.425, rely=0.115, anchor=CENTER)
        cand2 = Button(
            votingRoot, text=studentDetails.loc[int(candidates[i][3])]['Name'], command=lambda: change(i+1, 4),bg='#fcd232',border=0, font=('Impact',20),cursor='hand2',activebackground='#fcd232')
        cand2.place(relx=0.6, rely=0.17, anchor=CENTER)

    quit = Button(votingRoot, text="Logout", command=votingRoot.destroy)
    quit.place(relx=0.9, rely=0.02)

    votingRoot.attributes('-fullscreen', True)
    votingRoot.configure(bg='#3AAFA9')
    votingRoot.mainloop()
