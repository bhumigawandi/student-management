
import tkinter as tk
from tkinter import messagebox
import smtplib
import random

class OTPSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def generate_otp(self):
        return str(random.randint(100000, 999999))

    def send_otp(self, email, otp):
        try:
            # Create an SMTP connection
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()

            # Log in to your email account
            server.login(self.sender_email, self.sender_password)

            # Compose the email
            subject = 'Your OTP'
            body = f'Your OTP is: {otp}'
            message = f'Subject: {subject}\n\n{body}'

            # Send the email
            server.sendmail(self.sender_email, email, message)

            # Close the SMTP connection
            server.quit()

            messagebox.showinfo('Success', 'OTP sent successfully!')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to send OTP: {str(e)}')

class OTPApp:
    def __init__(self, root):
        self.root = root
        self.root.title('OTP Sender')

        self.otp_sender = OTPSender('smtp.gmail.com', 587, 'ruparelmanagement@gmail.com', 'uewv oitf hbpn diyb')

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text='Enter your email:', font=("Arial", 17),fg="maroon",bg="light blue")
        self.label.pack(pady=10)

        self.email_entry = tk.Entry(self.root,bd=5, font=("Arial", 10))
        self.email_entry.pack(pady=10)

        self.send_button = tk.Button(self.root, text='Send OTP', command=self.send_otp_button_click,fg="maroon",bg="yellow",activebackground="green")
        self.send_button.pack(pady=10)

        self.otp_label = tk.Label(self.root, text='Enter OTP:', font=("Arial", 17),fg="maroon",bg="light blue")
        self.otp_label.pack(pady=10)

        self.otp_entry = tk.Entry(self.root, show='*',bd=5,fg="maroon", font=("Arial", 10))
        self.otp_entry.pack(pady=10)

        self.verify_button = tk.Button(self.root, text='Verify OTP', command=self.verify_otp_button_click,fg="maroon",bg="yellow",activebackground="green")
        self.verify_button.pack(pady=10)

    def send_otp_button_click(self):
        email = self.email_entry.get()
        if email:
            self.generated_otp = self.otp_sender.generate_otp()
            self.otp_sender.send_otp(email, self.generated_otp)
            self.label.config(text='Enter your email (OTP sent)')
        else:
            messagebox.showwarning('Warning', 'Please enter your email address.')

    def verify_otp_button_click(self):
        entered_otp = self.otp_entry.get()
        if entered_otp == self.generated_otp:
            messagebox.showinfo('Success', 'OTP Verified!')
        else:
            messagebox.showerror('Error', 'Invalid OTP. Please try again.')

if __name__ == "__main__":
    root = tk.Tk()
    app = OTPApp(root)
    root.mainloop()

