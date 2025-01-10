import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Hello!",f"Hello, {user_input}!")
    else:
        messagebox.showwarning("Input Needed","Please enter your name!")

root =tk.Tk()
root.title("Basic GUI App")
root.geometry("300x200")

label = tk.Label(root, text="Enter your name:", font=("Arial",12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial",12))
entry.pack(pady=10)

button = tk.Button(root, text="Greet Me", command=on_button_click, font=("Arial, 12"))
button.pack(pady=10)

root.mainloop()