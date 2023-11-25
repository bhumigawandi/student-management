from tkinter import *
from PIL import ImageTk, Image
import smtplib
import random
from email.mime.text import MIMEText
#lnln

def forget():
    
    root = Tk()
    root.title("Forget Password")
    frame = Frame(root, width=350, height=150)
    frame.pack()
    L = Label(frame, text="Email Id", width=30, font=(50), fg="red")
    E = Entry(frame, width=30, bg="white")
    L.place(x=10, y=30)
    E.place(x=85, y=70)
    B = Button(frame, text="Submit", bg="light green", fg="blue")
    B.place(x=150, y=100)
    root.mainloop()
def email():
    def generate_otp():
        return str(random.randint(100000, 999999))

    def send_otp():
        global otp_code
        user_email = email_entry.get()
        otp_code = generate_otp()

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Update with your SMTP server's port
        sender_email = 'ruparelmanagement@gmail.com'  # Replace with your email address
        sender_password = 'uewv oitf hbpn diyb'  # Replace with your email password

        recipient_email = user_email

        subject = 'Your OTP Code'
        body = f'Your OTP code is: {otp_code}'
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = recipient_email

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, [recipient_email], message.as_string())
                verify_button['state'] = 'normal'
                print(f"OTP sent successfully to {recipient_email}.")
        except Exception as e:
            print(f"Error sending OTP: {e}")

    def verify_otp():
        entered_otp = otp_entry.get()
        if entered_otp == otp_code:
            verification_label.config(text="OTP verification successful!", fg="green")
        else:
            verification_label.config(text="Invalid OTP. Please try again.", fg="red")

    # Tkinter GUI
    root = Tk()
    root.title("OTP Sender")

    label = Label(root, text="Enter your email:")
    label.pack()

    email_entry = Entry(root)
    email_entry.pack()

    send_button = Button(root, text="Send OTP", command=send_otp)
    send_button.pack()
    otp_entry = Entry(root, show="*")  
    otp_entry.pack()

    verify_button = Button(root, text="Verify OTP", command=verify_otp, state='disabled')
    verify_button.pack()
    verification_label = Label(root, text="")
    verification_label.pack()

    root.mainloop()



def signup():
    root = Tk()
    f = Frame(root, width=1500, height=1000, bg="light blue")
    f.propagate(0)
    f.pack()

    leftframe = LabelFrame(f, bd=10, bg="pink")
    leftframe.place(x=100, y=10, width=1000, height=500)
    l = Label(leftframe, text="Login", font=("Arial", 30, 'bold'), fg="red", bg="pink")
    l1 = Label(leftframe, text="Username :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
    l2 = Label(f, text="Password :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
    l3 = Label(f, text="Username :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
    l4 = Label(f, text="Password :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
    l5 = Label(f, text="Email Id :", font=("Arial", 20, 'bold'), fg='maroon', bg="pink")
    l6 = Label(f, text="Sign Up", font=("Arial", 30, 'bold'), fg="red", bg="pink")
    l6.place(x=700, y=35)

    e1 = Entry(f, width=15, font=(10), bd=5, fg='pink')
    e2 = Entry(f, width=15, font=(10), bd=5)
    e3 = Entry(f, width=15, font=(10), bd=5)
    e4 = Entry(f, width=15, font=(10), bd=5, show='*')
    e5 = Entry(f, width=15, font=(10), bd=5)
    l.place(x=150, y=15)

    l1.place(x=20, y=120)
    e1.place(x=300, y=140)

    l2.place(x=130, y=200)
    e2.place(x=300, y=200)

    l3.place(x=600, y=120)
    e3.place(x=780, y=125)

    l4.place(x=600, y=250)
    e4.place(x=750, y=255)

    l5.place(x=600, y=180)
    e5.place(x=750, y=185)

    b = Button(f, text="Login", bg="yellow", font=("Arial", 10, 'bold'),command=email)
    b.place(x=300, y=300)

    b2 = Button(f, text="forget password", font=("Arial", 10, 'bold'), fg="blue", bg="light blue", command=forget)
    b2.place(x=400, y=250)

    b3 = Button(f, text="X Exit", bg="red", font=("Arial", 10, 'bold'))
    b3.place(x=545, y=450)

    b4 = Button(f, text="Sign up", bg="red", font=("Arial", 10, 'bold'))
    b4.place(x=700, y=350)

    canvas_width = 5
    canvas_height = 400
    canvas = Canvas(f, width=canvas_width, height=canvas_height, bg="black")
    canvas.propagate()
    canvas.place(x=550, y=10)
    root.mainloop()

def destroy_frame():
    frame1.destroy()
    root.destroy()
def combo1():
    destroy_frame()
    login()
def combo2():
    destroy_frame()
    signup()


def login():

    root = Tk()
    root.title("Login")

    f = Frame(root, width=1500, height=1500, bg="light blue")
    f.propagate(0)
    f.pack()
    leftframe = LabelFrame(f, bd=10, bg="pink")
    leftframe.place(x=200, y=10, width=800, height=500)
    l = Label(leftframe, text="Login", font=("Arial", 30, 'bold'), fg="red", bg="pink")
    l1 = Label(leftframe, text="Username", font=("Arial", 20, 'bold'), bg="pink", fg='maroon')
    l2 = Label(leftframe, text="Email Id", font=("Arial", 20, 'bold'), bg="pink", fg='maroon')

    l3 = Label(leftframe, text="Password", font=("Arial", 20, 'bold'), bg="pink", fg='maroon')

    e1 = Entry(leftframe, width=20, font=("Arial", 10, 'bold'), bd=5)
    e2 = Entry(leftframe, width=20, font=("Arial", 10, 'bold'), bd=5)
    e3 = Entry(leftframe, width=20, font=("Arial", 10, 'bold'), bd=5)
    l.place(x=300, y=30)
    l1.place(x=20, y=100)
    e1.place(x=200, y=100)
    l2.place(x=20, y=150)
    e2.place(x=200, y=150)
    l3.place(x=20, y=200)
    e3.place(x=200, y=200)
    b = Button(f, text="Login", bg='red', border=5,command=email)
    b.place(x=300, y=300)

    b2 = Button(f, text="forget password", font=("Arial", 10, 'bold'), fg="blue", bg="pink", border=5,
                activebackground='red', command=forget)
    b2.place(x=460, y=260)

    root.mainloop()

    root.mainloop()


root = Tk()
root.title('student and course managment ')
frame1=Frame(root,width=1920,height=1080,bg='light blue')
frame1.pack()
img = ImageTk.PhotoImage(Image.open("img.png"))

img1 = ImageTk.PhotoImage(Image.open("img1.png"))

label = Label(frame1, image=img)
label.place(x=10, y=25)
l1 = Label(frame1, image=img1)
l1.place(x=300, y=150)
b1 = Button(frame1, text="Student", bg='yellow', fg='black', font=("Arial", 17), activeforeground="white",
            activebackground="red", command=combo1)
b1.place(x=950, y=300)
b2 = Button(frame1, text="Faculty", bg="yellow", fg="black", font=("Arial", 17), activeforeground="white",
            activebackground="red", command=combo2)
b2.place(x=950, y=350)
b3 = Button(frame1, text="X Exit", bg="red", fg="black", font=("Arial", 17), activeforeground="white",
            activebackground="red")
b3.place(x=800, y=650)
m = Label(frame1, text="STUDENT & COURSE\n MANAGEMENT SYSTEM", bg="white", fg="purple", font=('bold 30 underline'))
m.place(x=450, y=15)

root.geometry("1000x1000")
root.mainloop()