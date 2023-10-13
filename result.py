from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import csv
import pandas as pd
from fpdf import FPDF
import os


def makePDF():
    global data
    pdf = FPDF(format='letter', unit='in')

    # Add new page. Without this you cannot create the document.
    pdf.add_page()

    # Remember to always put one of these at least once.
    pdf.set_font('Times', '', 10.0)

    pdf.image('pdfBg.jpg',x=0,y=0,w=9,h=12,type='',link='')

    # Effective page width, or just epw
    epw = pdf.w - 2*pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw/3
    th = pdf.font_size

    pdf.set_font('Times','B',14.0) 
    # pdf.cell(epw, 0.0, 'School Council \n (powered by ChunaaV)', align='C')
    # pdf.set_font('Times','',10.0) 
    pdf.ln(2.5)
    

    for row in data:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 2*th, str(datum), border=1)
    
        pdf.ln(2*th)
    filepath=filedialog.asksaveasfilename(defaultextension='.pdf')
    pdf.output(filepath)
    os.system(filepath)

def result():
    global data
    resultRoot = Toplevel()

    studentDetails = pd.read_csv("StuData.csv")
    studentDetails.set_index("AdNo", inplace=True)

    allWinners = Frame(resultRoot)
    allWinners.pack()
    Label(resultRoot, text='School Council!', font=('Britannic Bold', 40), bg='#3AAFA9', fg='gold').place(
        relx=0.5, rely=0.07, anchor=CENTER)

    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview.Heading', rowheight=40,
                font=('Impact', 30), background='green')
    s.configure('Treeview', font=('Segoe UI Semibold', 13), rowheight=25)
    allEntries = ttk.Treeview(allWinners, height=20)
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

    # pdf = FPDF(format='letter', unit='in')

    # # Add new page. Without this you cannot create the document.
    # pdf.add_page()

    # # Remember to always put one of these at least once.
    # pdf.set_font('Times', '', 10.0)

    # # Effective page width, or just epw
    # epw = pdf.w - 2*pdf.l_margin

    # # Set column width to 1/4 of effective page width to distribute content
    # # evenly across table and page
    # col_width = epw/3

    data = [['Position', 'Ruling', 'Opposition']]
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
            current=[item[0], studentDetails.loc[int(item[r])]['Name']+' ('+str(
                item[r])+')', studentDetails.loc[int(item[o])]['Name']+' ('+str(item[o])+')']
            data.append(current)
            allEntries.insert(parent='', index='end', iid=y, text='',
                              values=(item[0], studentDetails.loc[int(item[r])]['Name']+' ('+str(item[r])+')', studentDetails.loc[int(item[o])]['Name']+' ('+str(item[o])+')'))
            y += 1
            allEntries.pack()

    backImg=PhotoImage(file='backImage.png')
    Button(resultRoot, image=backImg, command=resultRoot.destroy,border=0,pady=0,padx=0,activebackground=None).place(
        relx=0.95, rely=0.05,anchor=CENTER)

    Button(resultRoot, text='Save as pdf', command=makePDF, background='#0000FF', foreground='white', activebackground='#82CAFF',
           activeforeground='white', font=('Arial', 16), border=0, cursor='hand2').place(relx=0.45, rely=0.9)
    resultRoot.attributes('-fullscreen', True)
    resultRoot.configure(bg='#3AAFA9')
    resultRoot.mainloop()