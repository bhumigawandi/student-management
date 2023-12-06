from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox



class Detail:
    def __init__(self,root):
        # def on_exit():
        #     result = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
        #
        #     if result:
        #         root.protocol("WM_DELETE_WINDOW", on_exit)
        #
        #         self.root.destroy()
        def on_exit():
            result = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
            if result:
                self.root.destroy()

            # Create the main Tkinter window
            root = tk.Tk()
            root.title("Exit Message Box Example")

            # Bind the on_exit function to the close button of the window
            root.protocol("WM_DELETE_WINDOW", on_exit)

            # Create some widgets or components for your application
            label = tk.Label(root, text="Hello, Tkinter!")
            label.pack(pady=10)



        self.root=root
        self.MainFrame= LabelFrame(self.root, bd=5, bg="white",  text="Student Information",)

        self.MainFrame.place(x=25, y=10, width=1200, height=1500)
        self.img = ImageTk.PhotoImage(Image.open("studentimg1.jpg"))




        self.label = Label(self.MainFrame, image = self.img)
        self.label.pack()

        self.viewframe= LabelFrame(self.MainFrame, bd=5, bg="white",  text="Student Information",)
        self.viewframe.place(x=25, y=200, width=800, height=70)

        self.m = Label(self.MainFrame, text="STUDENT & COURSE\n MANAGEMENT SYSTEM", bg="white", fg="purple",
                          font=('bold 30 underline'))
        self.m.place(x=450, y=5)

        self.Infoframe= LabelFrame(self.MainFrame, bg="white")
        self.Infoframe.place(x=25, y=300, width=800, height=300)

        self.S1=Scrollbar(self.Infoframe,orient=HORIZONTAL,width=20)
        self.S1.pack(side=BOTTOM,fill=X)

        self.S2=Scrollbar(self.Infoframe,orient=VERTICAL,width=20)
        self.S2.pack(side=RIGHT,fill=Y)

        self.L1=Label(self.viewframe,text="Search By :" ,bg="black",fg="white",font=(20))
        self.L1.place(x=5,y=10)

        self.E1=ttk.Combobox(self.viewframe, width=10, font=(5))
        self.E1.place(x=150,y=10)

        self.E2 = Entry(self.viewframe, width=10, font=(5), bd=2)
        self.E2.place(x=300,y=10)

        self.B1=Button(self.viewframe,text="Search",bg="yellow",fg="black",font=(40),width=10,activebackground='white',activeforeground='black')
        self.B1.place(x=500)

        self.B2=Button(self.viewframe,text="Show All",bg="yellow",fg="black",font=(40),width=10)
        self.B2.place(x=650)



