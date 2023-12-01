import tkinter as tk
from tkinter import messagebox
import mainframe as m
import emailtest as Email
import student_detail as Detail
import student_info as Info


def login_app(root_parent):
    root = tk.Tk()
    main_obj = root_parent
    root_parent.exit()
    login_obj = Login(root, main_obj)
    return login_obj


class Login:
    def __init__(self, root, main_obj):

        self.flag = None

        def check_fun():
            self.flag = 0
            self.l = []
            self.e = self.e2.get()
            for self.i in self.e:
                self.l.append(self.i)
            self.a = ['@', 'g', 'm', 'a', 'i', 'l', '.', 'c', 'o', 'm']
            self.b = self.l[-10:]  # email

            self.l = ""
            self.p = self.e3.get()  # username

            self.p1 = self.e1.get()
            if self.p == self.l or self.p1 == self.l or self.a == self.l:
                messagebox.askokcancel("Input", "Invalid Input")
            elif self.a != self.b:
                messagebox.askokcancel('email', 'invaild email id')
            else:
                self.flag = 1
                messagebox.askokcancel('Input', 'login successfully')

        def combo():
            check_fun()
            if self.flag == 1:
                Info.std_info()



        self.root = root
        self.parent = main_obj
        root.title("Login")
        self.f = tk.Frame(root, width=1500, height=1500, bg="light blue")
        self.f.propagate(0)
        self.f.pack()
        self.leftframe = tk.LabelFrame(self.f, bd=10, bg="pink")
        self.leftframe.place(x=200, y=10, width=800, height=500)
        self.l = tk.Label(self.leftframe, text="Login", font=("Arial", 30, 'bold'), fg="red", bg="pink")
        self.l1 = tk.Label(self.leftframe, text="Username", font=("Arial", 20, 'bold'), bg="pink", fg='maroon')
        self.l2 = tk.Label(self.leftframe, text="Email Id", font=("Arial", 20, 'bold'), bg="pink", fg='maroon')

        self.l3 = tk.Label(self.leftframe, text="Password", font=("Arial", 20, 'bold'), bg="pink", fg='maroon')

        self.e1 = tk.Entry(self.leftframe, width=20, font=("Arial", 10, 'bold'), bd=5)
        self.e2 = tk.Entry(self.leftframe, width=20, font=("Arial", 10, 'bold'), bd=5)
        self.e3 = tk.Entry(self.leftframe, width=20, font=("Arial", 10, 'bold'), bd=5)
        self.l.place(x=300, y=30)
        self.l1.place(x=20, y=100)
        self.e1.place(x=200, y=100)
        self.l2.place(x=20, y=150)
        self.e2.place(x=200, y=150)
        self.l3.place(x=20, y=200)
        self.e3.place(x=200, y=200)
        self.b = tk.Button(self.f, text="Login", bg='red', border=5, command=combo)
        self.b.place(x=300, y=300)

        self.b2 = tk.Button(self.f, text="forget password", font=("Arial", 10, 'bold'), fg="blue", bg="pink", border=5,
                            activebackground='red', command=lambda: Email.email(self))

        self.b3 = tk.Button(self.f, text="X BACK", bg="red", fg="black", font=("Arial", 17),
                            activeforeground="white",
                            activebackground="red", command=self.exit)
        self.b3.place(x=400,y=400)
        self.b2.place(x=460, y=260)
        self.root.attributes('-fullscreen', True)
        self.root.mainloop()

    def exit(self):
        self.root.destroy()
        m.main()
