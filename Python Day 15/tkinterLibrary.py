import tkinter as tk

def check():
    username = entry.get()
    l = len(username)

    if l < 10:
        result.config(text="Less than 10 characters", fg="red")
    elif l == 10:
        result.config(text="Exactly 10 characters", fg="green")
    else:
        result.config(text="More than 10 characters", fg="blue")

root = tk.Tk()
root.title("Username Checker")

tk.Label(root, text="Enter username:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=check).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()
