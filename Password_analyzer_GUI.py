import tkinter as tk
from tkinter import ttk, messagebox

def check_password(password):
    length = len(password)

    if length < 6:
        return "Password must be at least 6 characters long!"

    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    special = any(not c.isalnum() for c in password)
    digits = any(c.isdigit() for c in password)

    if upper and lower and special and digits:
        if length >= 10:
            return "The strength of password is strong."
        else:
            return "The strength of password is medium."
    else:
        
        missing_elements = []
        if not upper:
            missing_elements.append("one uppercase character")
        if not lower:
            missing_elements.append("one lowercase character")
        if not special:
            missing_elements.append("one special character")
        if not digits:
            missing_elements.append("one digit")
        return "Password must contain at least " + ", ".join(missing_elements) + "."

def on_check_password():
    password = entry.get()
    result = check_password(password)
    messagebox.showinfo("Password Check Result", result)


root = tk.Tk()
root.title("Password Analyzer")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg='lightblue')


entry_label = ttk.Label(root, text="Please enter password:")
entry_label.pack(pady=20)

entry = ttk.Entry(root, show='*', width=30)
entry.pack(pady=10)

# Add button to check password
check_button = ttk.Button(root, text="Check Password", command=on_check_password)
check_button.pack(pady=20)

root.mainloop()
