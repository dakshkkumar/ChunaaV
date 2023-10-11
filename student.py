from tkinter import *
from tkinter import ttk
import pandas as pd
import csv
import votingPage


def runStudent(id):
    global studentRoot
    studentRoot = Toplevel()

    with open('StuData.csv') as studentDetails:
        students = csv.reader(studentDetails)
        for data in students:
            if data[0] == str(id):
                Label(studentRoot, text='Welcome,\n'+data[2]+',', border=0, pady=0, bg='#3AAFA9', fg='#FFF2CC', font=(
                    'Britannic Bold', 40), justify='left').place(relx=0.03, rely=0.03)
                break

    Label(studentRoot, text='''This is the school voting portal powered by ChunaaV! Please read the following instructions carefully before casting your vote to ensure
a smooth and fair voting process:''', font=('Small Fonts', 15), justify='left', border=0, pady=0, bg='#3AAFA9', fg='black').place(relx=0.03, rely=0.2)

    Label(studentRoot, text='''
1. You will see two buttons, each displaying the name of a candidate, competing for the mentioned position.

2. Carefully review the candidates and their position to make an informed choice.

3. Click on the button of the candidate you wish to vote for.

4. After clicking, your vote will automatically be submitted, and you will not be able to change it.

5. Ensure you cast your vote accurately, as only one vote is allowed per person, per position.
          
6. Click on the 'GO!' button, to start ;)''', font=('Small Fonts', 15), justify='left', border=0, pady=0, bg='#3AAFA9', fg='black').place(relx=0.07, rely=0.27)

    Label(studentRoot, text='''Thank You for participating in our school's democratic process!''', font=(
        'Small Fonts', 20), justify='left', border=0, pady=0, bg='#3AAFA9', fg='green').place(relx=0.03, rely=0.69)

    quit = Button(studentRoot, text="Logout",
                  command=studentRoot.destroy)
    quit.place(relx=0.9, rely=0.02)

    with open('StuData.csv') as studentDetails:
        students = csv.reader(studentDetails)
        for data in students:
            if data[0] == str(id):
                if data[3] == 'True':
                    Button(studentRoot, text='GO!', command=None, state=DISABLED, font=(
                        'Small Fonts', 30), pady=0).place(relx=0.45, rely=0.8)
                    Label(studentRoot, text='''**Looks like you've
ALREADY voted.**''', font=('Small Fonts', 15), bg='#3AAFA9', fg='red', justify='left').place(relx=0.55, rely=0.81)
                else:
                    Button(studentRoot, text='GO!', command=lambda: votingPage.votingData(
                        id,studentRoot), font=('Small Fonts', 30), pady=0).place(relx=0.45, rely=0.8)
                    Label(studentRoot, text='''<--Click here
to vote''', font=('Small Fonts', 15), bg='#3AAFA9', fg='green', justify='left').place(relx=0.55, rely=0.81)
                break
    studentRoot.attributes('-fullscreen', True)
    studentRoot.configure(bg='#3AAFA9')
    studentRoot.mainloop()


