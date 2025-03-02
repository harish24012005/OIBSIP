import tkinter as tk
from tkinter import messagebox
import os

FILE_PATH = "users.txt"  

def register_user():
    username = reg_username_entry.get()
    password = reg_password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Fields cannot be empty!")
        return

    
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            for line in file:
                stored_username, _ = line.strip().split(":")
                if stored_username == username:
                    messagebox.showerror("Error", "Username already exists!")
                    return

    with open(FILE_PATH, "a") as file:
        file.write(f"{username}:{password}\n")

    messagebox.showinfo("Success", "Registration successful!")
    register_window.destroy()
    login_window.deiconify()  

def login_user():
    username = login_username_entry.get()
    password = login_password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Fields cannot be empty!")
        return

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if stored_username == username and stored_password == password:
                    messagebox.showinfo("Success", "Login Successful!")
                    login_window.destroy()
                    open_secured_page()
                    return

    messagebox.showerror("Error", "Invalid Username or Password!")

def open_secured_page():
    secured_window = tk.Tk()
    secured_window.title("Secured Page")
    secured_window.geometry("300x150")

    tk.Label(secured_window, text="Welcome to the secured page!", font=("Arial", 12)).pack(pady=20)

    tk.Button(secured_window, text="Logout", command=secured_window.destroy).pack()
    secured_window.mainloop()

def open_register_window():
    global register_window, reg_username_entry, reg_password_entry

    login_window.withdraw()  

    register_window = tk.Tk()
    register_window.title("Register")
    register_window.geometry("300x200")

    tk.Label(register_window, text="Username:").pack()
    reg_username_entry = tk.Entry(register_window)
    reg_username_entry.pack()

    tk.Label(register_window, text="Password:").pack()
    reg_password_entry = tk.Entry(register_window, show="*")
    reg_password_entry.pack()

    tk.Button(register_window, text="Register", command=register_user).pack(pady=10)
    tk.Button(register_window, text="Back to Login", command=lambda: (register_window.destroy(), login_window.deiconify())).pack()

    register_window.mainloop()

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Username:").pack()
login_username_entry = tk.Entry(login_window)
login_username_entry.pack()

tk.Label(login_window, text="Password:").pack()
login_password_entry = tk.Entry(login_window, show="*")
login_password_entry.pack()

tk.Button(login_window, text="Login", command=login_user).pack(pady=5)
tk.Button(login_window, text="Register", command=open_register_window).pack()

login_window.mainloop()
