import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to connect to the database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",  # your database host
        user="root",  # your database username
        password="Oneeyedeagle@21",  # your database password
        database="mydatabase"  # your database name
    )

# Function to check login credentials
def check_login(username, password):
    db = connect_to_db()
    cursor = db.cursor()

    query = "SELECT password FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    db.close()

    if result is None:
        return False

    stored_password = result[0]
    return stored_password == password

# Function to create a new user
def create_user(username, password):
    db = connect_to_db()
    cursor = db.cursor()

    # Check if username already exists
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    if cursor.fetchone():
        db.close()
        return False

    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    db.commit()
    db.close()
    return True

# Function to handle login button click
def login():
    username = entry_username.get()
    password = entry_password.get()

    if check_login(username, password):
        messagebox.showinfo("Login", "Login successful!")
        root.destroy()
        open_store_management_system()
    else:
        messagebox.showerror("Error", "Invalid Credentials")



def open_store_management_system():
    import store

# Function to handle register button click
def register():
    username = entry_username.get()
    password = entry_password.get()

    if create_user(username, password):
        messagebox.showinfo("Register", "Registration successful!")
    else:
        messagebox.showerror("Register", "Username already exists! Please choose a different username.")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create and place the username label and entry
label_username = tk.Label(root, text="Username")
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password")
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, padx=10, pady=10)

# Create and place the register button
register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=2, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()
