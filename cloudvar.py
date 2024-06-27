import scratchattach as scratch3
import hashlib
import sys
import tkinter as tk
from tkinter import messagebox

def SHA1(msg: str) -> str:
    return hashlib.sha1(msg.encode()).hexdigest()

global username, password, session, id, conn, logs, keys, flood_entry, variable_entry, value_entry

def on_command():
    flood = flood_entry.get()
    variables = variable_entry.get()
    value = value_entry.get()

    var_list = variables.split("-")

    if flood == 'yes':
        while True:
            for name in var_list:
                conn.set_var(name, value)
    else:
        for name in var_list:
            conn.set_var(name, value)

def on_submit():
    global username, password, session, id, conn, logs, keys, flood_entry, variable_entry, value_entry

    username = username_entry.get()
    password = password_entry.get()
    id = id_entry.get()

    # Basic validation
    if not username or not password or not id:
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    
    session = scratch3.login(username, password) # so that you are logged in
    conn = session.connect_cloud(id)
    logs = scratch3.get_cloud(id)
    keys = list(logs.keys())

    username_entry.destroy()
    password_entry.destroy()
    id_entry.destroy()
    username_label.destroy()
    password_label.destroy()
    id_label.destroy()
    submit_button.destroy()

    tk.Label(root, text=f"Variables in Use: {keys}\nPut in variables to change (sep:-): ").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    variable_entry = tk.Entry(root)
    variable_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Value:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    value_entry = tk.Entry(root)
    value_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Flood?:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    flood_entry = tk.Entry(root)
    flood_entry.grid(row=2, column=1, padx=10, pady=10)

    command_button = tk.Button(root, text="Submit", command=on_command)
    command_button.grid(row=3, column=0, columnspan=2, pady=10)
    # Display input values
    # messagebox.showinfo("Input Received", f"Username: {username}\nPassword: {SHA1(password)}")

# Create the main window
root = tk.Tk()
root.title("Scratch Cloud Injection")
root.geometry("500x200")

# Create and place the labels and entry widgets
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry = tk.Entry(root)
password_entry.grid(row=1, column=1, padx=10, pady=10)

id_label = tk.Label(root, text="Project ID:")
id_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
id_entry = tk.Entry(root)
id_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
