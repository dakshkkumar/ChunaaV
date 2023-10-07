from tkinter import *
from tkinter import ttk
import pandas as pd
import time
import csv


def votingData(i, previousWindow):
    votingRoot = Tk()
    # global current
    with open('CandData.csv') as candDetails:
        candidates = list(csv.reader(candDetails))
        try:
            Label(votingRoot, text=candidates[i][0], font=(
                'Small Fonts', 20)).place(relx=0.5, rely=0.5)
            Button(votingRoot, text='next', command=lambda: votingData(i+1, votingRoot)).place(relx=0.8,rely=0.8)
        except:
            votingRoot.destroy()



    quit = Button(votingRoot, text="Logout", command=votingRoot.destroy)
    quit.place(relx=0.9, rely=0.02)

    # time.sleep(1)
    

    votingRoot.attributes('-fullscreen', True)
    votingRoot.configure(bg='#3AAFA9')
    votingRoot.mainloop()
    if previousWindow != None:
        previousWindow.destroy()


votingData(0, None)