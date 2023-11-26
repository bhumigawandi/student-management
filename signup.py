import tkinter as tk
class Singup:
    def __init__(self,root):
        root = root
        self.f = tk.Frame(root, width=1500, height=1000, bg="light blue")
        self.f.propagate(0)
        self.f.pack()

        self.leftframe = tk.LabelFrame(self.f, bd=10, bg="pink")
        self.leftframe.place(x=100, y=10, width=1000, height=500)
        self.l = tk.Label(self.leftframe, text="Login", font=("Arial", 30, 'bold'), fg="red", bg="pink")
        self.l1 = tk.Label(self.leftframe, text="Username :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
        self.l2 = tk.Label(self.f, text="Password :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
        self.l3 = tk.Label(self.f, text="Username :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
        self.l4 = tk.Label(self.f, text="Password :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
        self.l5 = tk.Label(self.f, text="Email Id :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
        self.l6 = tk.Label(self.f, text="Sign Up", font=("Arial", 30, 'bold'), fg="red", bg="pink")
        self.l6.place(x=700, y=35)

        self.e1 = tk.Entry(self.f, width=15, font=(10), bd=5, fg='pink')
        self.e2 = tk.Entry(self.f, width=15, font=(10), bd=5)
        self.e3 = tk.Entry(self.f, width=15, font=(10), bd=5)
        self.e4 = tk.Entry(self.f, width=15, font=(10), bd=5, show='*')
        self.e5 = tk.Entry(self.f, width=15, font=(10), bd=5)
        self.l.place(x=150, y=15)

        self.l1.place(x=20, y=120)
        self.e1.place(x=300, y=140)

        self.l2.place(x=130, y=200)
        self.e2.place(x=300, y=200)

        self.l3.place(x=600, y=120)
        self.e3.place(x=780, y=125)

        self.l4.place(x=600, y=250)
        self.e4.place(x=750, y=255)

        self.l5.place(x=600, y=180)
        self.e5.place(x=750, y=185)

        self.b = tk.Button(self.f, text="Login", bg="yellow", font=("Arial", 10, 'bold'))
        self.b.place(x=300, y=300)

        self.b2 =tk.Button(self.f, text="forget password", font=("Arial", 10, 'bold'), fg="blue", bg="light blue")
        self.b2.place(x=400, y=250)

        self.b3 = tk.Button(self.f, text="X Exit", bg="red", font=("Arial", 10, 'bold'))
        self.b3.place(x=545, y=450)

        self.b4 = tk.Button(self.f, text="Sign up", bg="red", font=("Arial", 10, 'bold'))
        self.b4.place(x=700, y=350)

        self.canvas_width = 5
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.f, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.propagate()
        self.canvas.place(x=550, y=10)

if __name__ == "__main__":
    root = tk.Tk()
    login_page = Singup(root)
    root.mainloop()