from tkinter import *
from tkinter import ttk


def addCandidate():
    import candidate
    candidate.candidate()


def addVoter():
    import voter
    voter.voter()


def getResult():
    import result
    result.result()


def runTeacher():
    teacherRoot = Toplevel()
    candImg = PhotoImage(file='candidate.png')
    voterImg = PhotoImage(file='voter.png')
    resultImg = PhotoImage(file='result.png')
    logImg = PhotoImage(file='logImage.png')

    Button(teacherRoot, image=candImg, bg='#3AAFA9', border=0, pady=0, padx=0,
           cursor='hand2', command=addCandidate, activebackground='#3AAFA9').place(relx=0.5, rely=0.2, anchor=CENTER)
    Button(teacherRoot, image=voterImg, bg='#3AAFA9', border=0, pady=0, padx=0,
           cursor='hand2', command=addVoter, activebackground='#3AAFA9').place(relx=0.5, rely=0.5, anchor=CENTER)
    Button(teacherRoot, image=resultImg, bg='#3AAFA9', border=0, pady=0, padx=0,
           cursor='hand2', command=getResult, activebackground='#3AAFA9').place(relx=0.5, rely=0.8, anchor=CENTER)

    quit = Button(teacherRoot, image=logImg, bg='#3AAFA9', border=0,
                  activebackground='#3AAFA9', command=teacherRoot.destroy, cursor='hand2')
    quit.place(relx=0.95, rely=0.05, anchor=CENTER)

    teacherRoot.attributes('-fullscreen', True)
    teacherRoot.configure(bg='#3AAFA9')
    teacherRoot.mainloop()


