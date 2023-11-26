import tkinter as tk
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
from random import randint

class signUpApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Sign Up with Gmail OTP Verification")

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)
        self.email_label.grid(row=0, column=0, sticky="e")
        self.email_entry.grid(row=0, column=1, columnspan=2, sticky="we")

        self.send_otp_button = tk.Button(root, text="Send OTP", command=self.send_otp)
        self.send_otp_button.grid(row=1, column=0, columnspan=3, pady=10)

        self.otp_label = tk.Label(root, text="OTP:")
        self.otp_entry = tk.Entry(root)
        self.otp_label.grid(row=2, column=0, sticky="e")
        self.otp_entry.grid(row=2, column=1, columnspan=2, sticky="we")

        self.verify_otp_button = tk.Button(root, text="Verify OTP", command=self.verify_otp)
        self.verify_otp_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.otp_code = None

    def generate_otp(self):
        # Generate a random 6-digit OTP
        return str(randint(100000, 999999))

    def send_otp(self):
        email = self.email_entry.get()
        if email:
            # Generate OTP
            self.otp_code = self.generate_otp()

            # Send OTP via email (replace this with actual email sending code)
            try:
                msg = EmailMessage()
                msg.set_content(f"Your OTP is: {self.otp_code}")
                msg["Subject"] = "OTP Verification"
                msg["From"] = ""  # Replace with your Gmail address
                msg["To"] = email

                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login("emailid", "password")  # Replace with your Gmail credentials
                    server.send_message(msg)

                messagebox.showinfo("Success", "OTP sent successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error sending OTP: {e}")
        else:
            messagebox.showerror("Error", "Please enter your email address.")

    def verify_otp(self):
        entered_otp = self.otp_entry.get()
        if entered_otp == self.otp_code:
            messagebox.showinfo("Success", "OTP verification successful.")
        else:
            messagebox.showerror("Error", "Invalid OTP.")


if __name__ == "__main__":
    root = tk.Tk()
    app = signUpApp(root)
    root.mainloop()
