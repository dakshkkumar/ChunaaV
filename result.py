from tkinter import *
from tkinter import ttk


def result():
    resultRoot = Tk()
    Label(resultRoot, text='Result').place(relx=0.5, rely=0.5)

    Button(resultRoot, text='Back', command=resultRoot.destroy).place(
        relx=0.9, rely=0.02)
    resultRoot.attributes('-fullscreen', True)
    resultRoot.configure(bg='#3AAFA9')
    resultRoot.mainloop()
