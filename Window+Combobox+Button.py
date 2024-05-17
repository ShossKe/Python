import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root=tk.Tk()

root.title("Window")

n=["1","2","3","4","5"]    
c=ttk.Combobox(
    root,
    state="normal",
    values=n,
    width=3
)
c.current(0)
c.pack(expand=True)

def co1():
    i=str(c.get())
    messagebox.showinfo("Info",i+".")
b=ttk.Button(
    root,
    text="Button",
    command=co1
)
b.pack(expand=True)
root.mainloop()