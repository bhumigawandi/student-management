from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import ImageTk, Image
class info:
    def __init__(self,root):
        self.root = root

        self.leftframe = LabelFrame(self.root, bd=8, bg="white", text="Student Information",font=("Arial", 17))
        self.leftframe.place(x=25, y=10, width=1200, height=1500)

        self.stdfrm = LabelFrame(self.root, bd=10, bg="white", text="Student Detail",font=("Arial", 17),background='light blue')
        self.stdfrm.place(x=50, y=80, width=630, height=280)

        self.crsfrm = LabelFrame(self.root, bd=10, bg="white", text="Course Information",font=("Arial", 17),background='light blue')
        self.crsfrm.place(x=50, y=400, width=630, height=180)

        self.l1 = Label(self.stdfrm, text="Student ID:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l2 = Label(self.stdfrm, text="Reg No:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l3 = Label(self.stdfrm, text="Gender: ", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l4 = Label(self.stdfrm, text="Email:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l5 = Label(self.stdfrm, text=" Address:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l6 = Label(self.stdfrm, text="Student Name:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l7 = Label(self.stdfrm, text="Role No:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l8 = Label(self.stdfrm, text="Date of Birth ", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l9 = Label(self.stdfrm, text="Phone No:", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l10 = Label(self.stdfrm, text="Batch Mentor:", fg="black", bg="pink",font=("Arial", 10,'bold'))

        self.e1 = Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e2 = Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e3 = ttk.Combobox(self.stdfrm, width=10, font=(5), values=['Male', 'Female'])
        self.e4 = Entry(self.stdfrm, width=10, font=(10), bd=2)
        self.e5 = Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e6 = Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e7 = Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e8 = DateEntry(self.stdfrm, width=10, font=(5))
        self.e9 = Entry(self.stdfrm, width=10, font=(5), bd=2)
        self.e10 = Entry(self.stdfrm, width=10, font=(5), bd=2)

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

        self.l11 = Label(self.crsfrm, text="Department :", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l12 = Label(self.crsfrm, text="Year :", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l13 = Label(self.crsfrm, text="Subject : ", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l14 = Label(self.crsfrm, text="Course :", fg="black", bg="pink",font=("Arial", 10,'bold'))
        self.l15 = Label(self.crsfrm, text=" Semester :", fg="black", bg="pink",font=("Arial", 10,'bold'))

        self.e11 = ttk.Combobox(self.crsfrm, width=10, font=(5), values=['IT', 'CS'])
        self.e12 = ttk.Combobox(self.crsfrm, width=10, font=(5), values=['2022-23', '2023-24'])
        self.e13 = Entry(self.crsfrm, width=10, font=(5), bd=2)
        self.e14 = ttk.Combobox(self.crsfrm, width=10, font=(5), values=['C', 'C++','Python','Java'])
        self.e15 = ttk.Combobox(self.crsfrm, width=10, font=(5), values=['1', '2','3','4','5','6'])

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

        img = ImageTk.PhotoImage(Image.open("studentimg1.jpg"))

        self.label = Label(self.leftframe, image=img)
        self.label.pack()

        self.image = Image.open("studentimg1.jpg")
        self.image1 = self.image.resize((150, 50))
        self.updateimage = ImageTk.PhotoImage(self.image1)

        self.sav = Image.open("save2.jpg")
        self.sav = sav.resize((150, 71))
        self.savimg = ImageTk.PhotoImage(self.sav)

        self.savbtn = Button(self.leftframe, bg="white", bd=0, image=self.savimg, cursor="hand2")
        self.savbtn.place(x=900, y=180, width=150, height=100)

        self.update = Image.open("update1.jpg")
        self.update = self.update.resize((150, 50))
        self.updateimg = ImageTk.PhotoImage(self.update)

        self.updatebtn = Button(self.leftframe, bg="white", bd=0, image=self.updateimg, cursor="hand2")
        self.updatebtn.place(x=900, y=290, width=140, height=45)

        self.delete = Image.open("delete2.jpg")
        self.delete = self.delete.resize((150, 50))
        self.deleteimg = ImageTk.PhotoImage(self.delete)

        self.deletebtn = Button(self.leftframe, bg="white", bd=0, image=self.deleteimg, cursor="hand2")
        self.deletebtn.place(x=900, y=470, width=140, height=45)

        self.reset = Image.open("reset2.jpg")
        self.reset = self.reset.resize((150, 50))
        self.resetimg = ImageTk.PhotoImage(self.reset)

        self.rsetbtn = Button(self.leftframe, bg="white", bd=0, image=self.resetimg, cursor="hand2")
        self.rsetbtn.place(x=900, y=380, width=140, height=45)


