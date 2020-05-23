import tkinter as tk
from tkinter import *
from tkmacosx import Button
import os

# called when submit button is pressed to store data
def submit():
    print("Date: %s\nDistance: %s\nDuration: %s" % (e1.get(), e2.get(), e3.get()))
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)

# called when entry fields are pressed to clear default text
def entry_click1(e):
    e1.delete(0, tk.END)
    e1.configure(fg = "black")

def entry_click2(e):
    e2.delete(0, tk.END)
    e2.configure(fg = "black")

def entry_click3(e):
    e3.delete(0, tk.END)
    e3.configure(fg = "black")    

# begin gui
print "\n\nrunning...\n"
root = tk.Tk()

# root window
root.title("Runkeeper")
root.geometry("300x240+1200+300")
root.configure(bg = "#2c6b6f")

# greetings
greeting1 = tk.Label(root, text="Welcome to Runkeeper!")
greeting1.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 18), pady=16)
greeting1.grid(row=0, column=1, sticky=tk.N)

greeting2 = tk.Label(root, text="Enter info below:")
greeting2.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), pady=4)
greeting2.grid(row=1, column=1)

# labels
l1 = tk.Label(root, text="Date")
l2 = tk.Label(root, text="Distance")
l3 = tk.Label(root, text="Duration")

l1.grid(row=2)
l2.grid(row=3)
l3.grid(row=4)

l1.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), padx=5, pady=4)
l2.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), padx=5, pady=4)
l3.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), padx=5, pady=4)

# entry boxes
global e1, e2, e3
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)

e1.insert(0, "MM/DD/YYYY")
e2.insert(0, "Number of miles")
e3.insert(0, "Number of minutes")

e1.configure(fg = "gray")
e2.configure(fg = "gray")
e3.configure(fg = "gray")

e1.grid(row=2, column=1)
e2.grid(row=3, column=1) 
e3.grid(row=4, column=1)

e1.bind('<FocusIn>', entry_click1)
e2.bind('<FocusIn>', entry_click2)
e3.bind('<FocusIn>', entry_click3)

# submit button
submit = Button(root, text='Submit', command=submit, borderless=1)
submit.configure(pady=4, bg = "white", fg = "black", font = ("Open Sans", 14))
submit.grid(row=5, column=1, pady=4)

# end gui
root.mainloop() # keep running until window closed
print "\n...end of run\n\n"