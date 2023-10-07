from tkinter import *
from tkinter import ttk
import pandas as pd
import time
import csv

def change(n, which):
    global candidates
    global votingRoot
    global pos
    global i
    global cand1
    global cand2
    global studentDetails
    global Details

    Details.iloc[n-2,which]=int(1+Details.iloc[n-2][which])
    Details.to_csv('CandData.csv',index=False)
    
    try:
        pos.config(text=candidates[n][0])
        cand1.config(text=studentDetails.loc[int(candidates[n][1])]['Name'])
        cand2.config(text=studentDetails.loc[int(candidates[n][3])]['Name'])
    except:
        votingRoot.destroy()
    i += 1


def votingData():
    global votingRoot
    global candidates
    global pos
    global i
    i = 1
    global cand1
    global cand2
    global studentDetails
    global Details
    studentDetails=pd.read_csv("StuData.csv")
    studentDetails.set_index("AdNo", inplace=True)

    Details=pd.read_csv("CandData.csv")

    votingRoot = Tk()

    votingBg = PhotoImage(file='votingBg.png')

    canvas = Canvas(votingRoot)
    canvas.create_image(0, 0, image=votingBg, anchor=NW)
    #canvas.create_text(680, 50, text="Add Candidate", fill='black',
                        #font=('Britannic Bold', 50))
    canvas.pack(fill='both', expand=True)

    with open('CandData.csv') as candDetails:
        candidates = list(csv.reader(candDetails))
        pos = Label(votingRoot, text=candidates[i][0], font=(
            'Small Fonts', 20))
        pos.place(relx=0.5, rely=0.4)

        cand1 = Button(
            votingRoot, text=studentDetails.loc[int(candidates[i][1])]['Name'], command=lambda: change(i+1,2))
        cand1.place(relx=0.4, rely=0.8)
        cand2 = Button(
            votingRoot, text=studentDetails.loc[int(candidates[i][3])]['Name'], command=lambda: change(i+1,4))
        cand2.place(relx=0.6, rely=0.8)
    

    
    
    quit = Button(votingRoot, text="Logout", command=votingRoot.destroy)
    quit.place(relx=0.9, rely=0.02)

    votingRoot.attributes('-fullscreen', True)
    votingRoot.configure(bg='#3AAFA9')
    votingRoot.mainloop()


votingData()
