import tkinter as tk
from tkinter import ttk

coef = 0.05

root = tk.Tk()
root.geometry("250x200")
root.eval('tk::PlaceWindow . center')

spinbox = ttk.Spinbox(from_=0, to=1, increment=0.01)
spinbox.set(coef)
spinbox.pack()

def finish():
    global coef
    coef = float(spinbox.get())
    root.destroy()

okay = tk.Button(text='OK', command=finish)
okay.pack()
 
root.mainloop()
print(coef)
