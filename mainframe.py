import tkinter as tk
from PIL import ImageTk, Image

class Mainframe:
    def __init__(self,root):
        root = root
        root.title('student and course managment ')
        self.frame1=tk.Frame(root,width=1920,height=1080,bg='light blue')
        self.frame1.pack()
        self.img = ImageTk.PhotoImage(Image.open("img.png"))

        self.img1 = ImageTk.PhotoImage(Image.open("img1.png"))

        self.label = tk.Label(self.frame1, image=self.img)
        self.label.place(x=10, y=25)
        self.l1 = tk.Label(self.frame1, image=self.img1)
        self.l1.place(x=300, y=150)
        self.b1 = tk.Button(self.frame1, text="Student", bg='yellow', fg='black', font=("Arial", 17), activeforeground="white",
                    activebackground="red")
        self.b1.place(x=950, y=300)
        self.b2 = tk.Button(self.frame1, text="Faculty", bg="yellow", fg="black", font=("Arial", 17), activeforeground="white",
                    activebackground="red")
        self.b2.place(x=950, y=350)
        self.b3 = tk.Button(self.frame1, text="X Exit", bg="red", fg="black", font=("Arial", 17), activeforeground="white",
                    activebackground="red")
        self.b3.place(x=800, y=650)
        self.m = tk.Label(self.frame1, text="STUDENT & COURSE\n MANAGEMENT SYSTEM", bg="white", fg="purple", font=('bold 30 underline'))
        self.m.place(x=450, y=15)

        root.geometry("1000x1000")


if __name__ == "__main__":
    root = tk.Tk()
    login_page = Mainframe(root)
    root.mainloop()