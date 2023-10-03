from tkinter import *
from tkinter import ttk
import teacher
import student
import pandas as pd
root = Tk()


def tempUserText(e):
    if user.get() == 'Username':
        user.delete(0, 'end')


def tempPassText(e):
    passw.delete(0, 'end')


def Login():
    global passw
    global user
    studentDetails=pd.read_csv("StuData.csv")
    studentDetails.set_index("AdNo", inplace=True)

    if user.get() == 'admin' and passw.get() == '12345':
        teacher.runTeacher()
    elif user.get().isnumeric() and int(user.get()) in range(1000,10000) and studentDetails.loc[int(user.get())]['Password']==passw.get():
        student.runStudent(int(user.get()))
    else:
        Label(root,text='*Uh oh! Invalid username or password!*',fg='red',font=(20),bg='#3AAFA9').place(relx=0.73,rely=0.70,anchor=CENTER)
        


Label(root,text="ChunaaV",border=0,pady=0,bg='#3AAFA9',fg='#FFF2CC',font=('Britannic Bold',50)).place(relx=0.5,rely=0.08,anchor=CENTER)
Frame(root, width=330, height=3, bg='black').place(
    relx=0.5, rely=0.13, anchor=CENTER)


img = PhotoImage(file='login.png')
Label(root, image=img, bg='#3AAFA9').place(relx=0.06, rely=0.18)
Button(root, text='exit', command=root.destroy).place(relx=0.9, rely=0.05)

Label(root, text='Sign In', fg='white', bg='#3AAFA9', font=(
    'Microsoft YaHei UI Light', 23, 'bold')).place(relx=0.72, rely=0.31,anchor=CENTER)
user = Entry(root, fg='black', width=25, border=0, bg='#3AAFA9',
             font=('Microsoft YaHei UI Light', 11))
user.place(relx=0.7, rely=0.5, anchor=CENTER)
user.insert(0, 'Username')
user.bind('<FocusIn>', tempUserText)
Frame(root, width=295, height=2, bg='black').place(
    relx=0.73, rely=0.52, anchor=CENTER)


passw = Entry(root, fg='black', width=25, border=0, bg='#3AAFA9',
              font=('Microsoft YaHei UI Light', 11))
passw.place(relx=0.7, rely=0.6, anchor=CENTER)
passw.insert(0, 'Password')
passw.bind('<FocusIn>', tempPassText)
Frame(root, width=295, height=2, bg='black').place(
    relx=0.73, rely=0.62, anchor=CENTER)

Button(root, width=30, pady=7, text='Log in', bg='white', fg='#57a1f8', border=0, cursor='hand2', font=(
    'Microsoft YaHei UI Light', 11, 'bold'), command=Login).place(relx=0.73, rely=0.77, anchor=CENTER)

root.attributes('-fullscreen', True)
root.configure(bg='#3AAFA9')
root.mainloop()
