import tkinter as tk
from PIL import ImageTk, Image
import loginpage as login
#hello this is main frame
def main():
    root = tk.Tk()
    app = Mainframe(root)
    return app


class Mainframe:
    def __init__(self, root):
        self.root = root
        self.root.title('Student And Course Managment ')
        self.frame1 = tk.Frame(self.root, width=1920, height=1080, bg='light blue')
        self.frame1.pack()
        self.img = ImageTk.PhotoImage(Image.open("img.png"))

        self.img1 = ImageTk.PhotoImage(Image.open("img1.png"))

        self.label = tk.Label(self.frame1, image=self.img)
        self.label.place(x=10, y=25)

        self.l1 = tk.Label(self.frame1, image=self.img1)
        self.l1.place(x=400, y=200)
        self.b1 = tk.Button(self.frame1, text="Student", bg='yellow', fg='black', font=("Arial", 17),
                            activeforeground="white",
                            activebackground="red", command=lambda: login.login_app(self))
        self.b1.place(x=500, y=650)
        self.b2 = tk.Button(self.frame1, text="Faculty", bg="yellow", fg="black", font=("Arial", 17),activeforeground="white",activebackground="red",command=lambda: login.login_app(self))
        self.b2.place(x=400, y=650)
        self.b3 = tk.Button(self.frame1, text="X Exit", bg="red", fg="black", font=("Arial", 17),
                            activeforeground="white",
                            activebackground="red", command=self.exit)
        self.b3.place(x=800, y=650)
        self.b4=tk.Button(self.frame1,text="Admin",bg="yellow",fg="black",font=("Arial",17),activeforeground="white",
                          activebackground="red")
        self.b4.place(x=600,y=650)
        self.m = tk.Label(self.frame1, text="D.G Ruparel College of Arts,\n Science and Commerce", bg="white", fg="purple",font=('bold 30 underline'))
        self.m.place(x=400, y=15)

        #self.root.geometry("1000x1000")
        self.root.attributes('-fullscreen', True)
        self.root.mainloop()

    def exit(self):
        self.root.destroy()


if __name__ == "__main__":
    main()