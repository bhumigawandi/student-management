import tkinter as tk
from tkinter import messagebox
class login:
    def __init__(self,root):
        self.root = root
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
        self.b = tk.Button(self.f, text="Login", bg='red', border=5)
        self.b.place(x=300, y=300)

        self.b2 = tk.Button(self.f, text="forget password", font=("Arial", 10, 'bold'), fg="blue", bg="pink", border=5,
                    activebackground='red')
        self.b2.place(x=460, y=260)
    # def login(self):
        # username = self.username_entry.get()
        # password = self.password_entry.get()
        #
        # # Add your authentication logic here
        # # For simplicity, let's use a basic check
        # if username == "admin" and password == "password":
        #     messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        # else:
        #     messagebox.showerror("Login Failed", "Invalid username or password")



if __name__ == "__main__":
    root = tk.Tk()
    login_page = login(root)
    root.mainloop()