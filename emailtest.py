import smtplib
import tkinter as tk
import random
from email.mime.text import MIMEText
from tkinter import Tk, Label, Entry, Button


def email(root_parent1):
    root = tk.Tk
    main_Obj = root_parent1

    email_obj = OTPSender(root, main_Obj)
    return email_obj


class OTPSender:
    def __init__(self, root, main_Obj):
        self.otp_code = None
        self.root = root

        self.root = Tk()
        self.parent = main_Obj
        self.root.title("OTP Sender")

        self.label = tk.Label(self.root, text="Enter your email:")
        self.label.pack()

        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.send_button = tk.Button(self.root, text="Send OTP", command=self.send_otp)
        self.send_button.pack()

        self.otp_entry = tk.Entry(self.root, show="*")  # Hide entered characters
        self.otp_entry.pack()

        self.verify_button = tk.Button(self.root, text="Verify OTP", command=self.verify_otp, state='disabled')
        self.verify_button.pack()

        self.verification_label = tk.Label(self.root, text="")
        self.verification_label.pack()
        self.root.mainloop()

    def generate_otp(self):
        return str(random.randint(100000, 999999))

    def send_otp(self):
        user_email = self.email_entry.get()
        self.otp_code = self.generate_otp()

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Update with your SMTP server's port
        sender_email = 'ruparelmanagement@gmail.com'  # Replace with your email address
        sender_password = 'uewv oitf hbpn diyb'  # Replace with your email password

        recipient_email = user_email

        subject = 'Your OTP Code'
        body = f'Your OTP code is: {self.otp_code}'
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = recipient_email

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, [recipient_email], message.as_string())
                print(f"OTP sent successfully to {recipient_email}.")
                self.verify_button['state'] = 'normal'  # Enable the Verify button
        except smtplib.SMTPAuthenticationError as auth_error:
            print(f"SMTP Authentication Error: {auth_error}")
        except Exception as e:
            print(f"Error sending OTP: {e}")

    def verify_otp(self):
        entered_otp = self.otp_entry.get()
        if entered_otp == self.otp_code:
            self.verification_label.config(text="OTP verification successful!", fg="green")
        else:
            self.verification_label.config(text="Invalid OTP. Please try again.", fg="red")
