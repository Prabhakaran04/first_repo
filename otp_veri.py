import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_otp():
    # Generate a random 6-digit OTP
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(6))
    return otp

def verify_otp():
    user_otp = otp_entry.get()
    generated_otp = otp_label.cget("text")
    
    if user_otp == generated_otp:
        messagebox.showinfo("Success", "OTP verified successfully!")
    else:
        messagebox.showerror("Error", "Invalid OTP. Please try again.")

root = tk.Tk()
root.title("OTP Verification")
otp_label = tk.Label(root, text="", font=("Arial", 24))
otp_label.pack(pady=10)
def generate_and_display_otp():
    otp = generate_otp()
    otp_label.config(text=otp)

# Create the main application window
# root = tk.Tk()
# root.title("OTP Verification")

# Generate and display the initial OTP
generate_and_display_otp()

# OTP label
# otp_label = tk.Label(root, text="", font=("Arial", 24))
# otp_label.pack(pady=10)

# OTP entry field
otp_entry = tk.Entry(root, font=("Arial", 24))
otp_entry.pack(pady=10)

# Verify OTP button
verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=10)

# Generate new OTP button
generate_button = tk.Button(root, text="Generate New OTP", command=generate_and_display_otp)
generate_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()



