import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sample App")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky="NSEW")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

button=tk.Button(root,text="Test",command=lambda:print("test"))
button.grid(row=0,column=0)

root.mainloop()