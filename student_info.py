from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import ImageTk, Image

import tkinter as tk
import mysql.connector

from tkinter import messagebox


# Create a SQLite database and connect to it
conn =mysql.connector.connect(host="localhost", username="root", password="root123",database="studentmanagement")
c = conn.cursor()

def save():
    c.execute('')


def std_info():
    root = tk.Tk()
    app1 = info(root)
    return app1


class info:
    def __init__(self,root):
        self.root = root
        def get_fun():
            self.var = ""
            self.id = self.e1.get()
            self.reg_no = self.e2.get()
            self.gender = self.e3.get()
            self.email = self.e4.get()
            self.add = self.e5.get()
            self.std_name = self.e6.get()
            self.role_no = self.e7.get()
            self.birth_date = self.e8.get()
            self.phone_no = self.e9.get()
            self.batch_mentor = self.e10.get()
            self.department = self.e11.get()
            self.year = self.e12.get()
            self.course = self.e13.get()
            self.subject = self.e14.get()
            self.DIGITS=self.id.isdigit()
            self.DIGITS1=self.reg_no.isdigit()

            self.SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
            self.LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            self.UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R',
                                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            self.combine=self.LOCASE_CHARACTERS+self.UPCASE_CHARACTERS

            self.l = []


            for self.i in self.email:
                self.l.append(self.i)

            self.a = ['@', 'g', 'm', 'a', 'i', 'l', '.', 'c', 'o', 'm']
            self.b = self.l[-10:]  # email



            if self.id == self.var or self.reg_no == self.var or self.gender==self.var or self.email==self.var or self.add == self.var or self.std_name==self.var or self.role_no==self.var or self.birth_date==self.var or self.phone_no==self.var or self.batch_mentor==self.var or self.department==self.var or self.year==self.var or self.course==self.var or self.subject==self.var:
                messagebox.askokcancel("Input","Invalid Input")

            elif self.a != self.b:
                messagebox.askokcancel('email', 'invaild email id')

            elif not self.id.isdigit():
                messagebox.askokcancel('ID ',"Invalid ID")
            elif not self.reg_no.isdigit():
                messagebox.askokcancel("Reg No","Invalid REG NO")
            elif not self.phone_no.isdigit() :
                messagebox.askokcancel("PHONE NO","Invalid Phone No")
            elif not self.std_name.isalpha():
                messagebox.askokcancel(" NAME"," Please Enter Valid Name ")
            else:
                messagebox.askokcancel("Signin","Saved Successfully")














        self.leftframe = tk.LabelFrame(self.root, bd=8, bg="white", text="Student Information",font=("Arial", 17))
        self.leftframe.place(x=25, y=10, width=1200, height=1500)

        self.stdfrm = tk.LabelFrame(self.root, bd=10, bg="white", text="Student Detail",font=("Arial", 17),background='light blue')
        self.stdfrm.place(x=50, y=80, width=630, height=280)

        self.crsfrm = tk.LabelFrame(self.root, bd=10, bg="white", text="Course Information",font=("Arial", 17),background='light blue')
        self.crsfrm.place(x=50, y=400, width=630, height=180)

        self.l1 = tk.Label(self.stdfrm, text="Student ID:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l2 = tk.Label(self.stdfrm, text="Reg No:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l3 = tk.Label(self.stdfrm, text="Gender: ", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l4 = tk.Label(self.stdfrm, text="Email:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l5 = tk.Label(self.stdfrm, text=" Address:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l6 = tk.Label(self.stdfrm, text="Student Name:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l7 = tk.Label(self.stdfrm, text="Role No:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l8 = tk.Label(self.stdfrm, text="Date of Birth ", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l9 = tk.Label(self.stdfrm, text="Phone No:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l10 = tk.Label(self.stdfrm, text="Batch Mentor:", fg="black", bg="pink",font=("Arial", 10,'bold'))

        self.e1 = tk.Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e2 = tk.Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e3 = ttk.Combobox(self.stdfrm, width=10, font=(5), values=['Male', 'Female'],state="readonly")
        self.e4 = tk.Entry(self.stdfrm, width=10, font=(10), bd=2)
        self.e5 = tk.Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e6 = tk.Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e7 = tk.Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e8 = DateEntry(self.stdfrm, width=10, font=(5),state="readonly")
        self.e9 = tk.Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e10 =ttk.Combobox(self.stdfrm, width=10, font=(5), values=['IT-Mandar Bhave ', 'CS-Priti Kharbe'],state="readonly")



        self.l1.place(x=15, y=15)
        self.e1.place(x=88, y=15)

        self.l2.place(x=15, y=55)
        self.e2.place(x=75, y=55)

        self.l3.place(x=15, y=100)
        self.e3.place(x=74, y=100)

        self.l4.place(x=15, y=145)
        self.e4.place(x=75, y=145)

        self.l5.place(x=15, y=195)
        self.e5.place(x=75, y=195)

        self.l6.place(x=360, y=15)
        self.e6.place(x=450, y=15)

        self.l7.place(x=360, y=55)
        self.e7.place(x=450, y=55)

        self.l8.place(x=360, y=100)
        self.e8.place(x=450, y=100)

        self.l9.place(x=360, y=150)
        self.e9.place(x=450, y=150)

        self.l10.place(x=360, y=200)
        self.e10.place(x=450, y=200)

        self.l11 = tk.Label(self.crsfrm, text="Department :", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l12 = tk.Label(self.crsfrm, text="Year :", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l13 = tk.Label(self.crsfrm, text="Subject : ", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l14 = tk.Label(self.crsfrm, text="Course :", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l15 = tk.Label(self.crsfrm, text=" Semester :", fg="black", bg="pink",font=("Arial", 10,'bold'))

        self.e11 = ttk.Combobox(self.crsfrm, width=10, font=(5), values=['IT', 'CS'],state="readonly")
        self.e12 = ttk.Combobox(self.crsfrm, width=10, font=(5), values=['2022-23', '2023-24'],state="readonly")
        self.e13 = tk.Entry(self.crsfrm, width=10, font=(5), bd=2)
        self.e14 = ttk.Combobox(self.crsfrm, width=10, font=(5), values=['C', 'C++','Python','Java'],state="readonly")
        self.e15 = ttk.Combobox(self.crsfrm, width=10, font=(5), values=['1', '2','3','4','5','6'],state="readonly")

        self.l11.place(x=2, y=10)
        self.e11.place(x=95, y=10)

        self.l12.place(x=5, y=50)
        self.e12.place(x=50, y=50)

        self.l13.place(x=200, y=98)
        self.e13.place(x=270, y=95)

        self.l14.place(x=350, y=10)
        self.e14.place(x=415, y=10)

        self.l15.place(x=350, y=50)
        self.e15.place(x=435, y=50)

        self.img = ImageTk.PhotoImage(Image.open("studentimg1.jpg"))

        self.label = tk.Label(self.leftframe, image=self.img)
        self.label.pack()

        self.image = Image.open("studentimg1.jpg")
        self.image1 = self.image.resize((150, 50))
        self.updateimage = ImageTk.PhotoImage(self.image1)

        self.sav = Image.open("save2.jpg")
        self.sav = self.sav.resize((150, 71))
        self.savimg = ImageTk.PhotoImage(self.sav)

        self.savbtn = tk.Button(self.leftframe, bg="white", bd=0, image=self.savimg, cursor="hand2",command=get_fun)
        self.savbtn.place(x=900, y=180, width=150, height=100)

        self.update = Image.open("update.png")
        self.update = self.update.resize((150, 50))
        self.updateimg = ImageTk.PhotoImage(self.update)

        self.updatebtn = tk.Button(self.leftframe, bg="white", bd=0, image=self.updateimg, cursor="hand2")
        self.updatebtn.place(x=900, y=290, width=140, height=45)

        self.delete = Image.open("delete2.jpg")
        self.delete = self.delete.resize((150, 50))
        self.deleteimg = ImageTk.PhotoImage(self.delete)

        self.deletebtn = tk.Button(self.leftframe, bg="white", bd=0, image=self.deleteimg, cursor="hand2")
        self.deletebtn.place(x=900, y=470, width=140, height=45)

        self.reset = Image.open("reset2.jpg")
        self.reset = self.reset.resize((150, 50))
        self.resetimg = ImageTk.PhotoImage(self.reset)

        self.rsetbtn = tk.Button(self.leftframe, bg="white", bd=0, image=self.resetimg, cursor="hand2")
        self.rsetbtn.place(x=900, y=380, width=140, height=45)
        self.leftframe.mainloop()



