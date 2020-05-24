import tkinter as tk
from tkmacosx import Button
from data import *

# called when submit button is pressed to store data
def submit():
    # global date, distance, duration
    date = e1.get()
    distance = e2.get()
    duration = e3.get()
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    inputData(date, distance, duration, sheet_test)
    print "Entry recorded\n"

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

def app():
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
    labels = [tk.Label(root, text="Date"), tk.Label(root, text="Distance"), tk.Label(root, text="Duration")]
    # l1 = tk.Label(root, text="Date")
    # l2 = tk.Label(root, text="Distance")
    # l3 = tk.Label(root, text="Duration")

    labels[0].grid(row=2)
    labels[1].grid(row=3)
    labels[2].grid(row=4)

    labels[0].configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), padx=5, pady=4)
    labels[1].configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), padx=5, pady=4)
    labels[2].configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), padx=5, pady=4)

    # entry boxes
    global e1, e2, e3
    e1 = tk.Entry(root)
    e2 = tk.Entry(root)
    e3 = tk.Entry(root)

    e1.insert(0, "MM/DD/YYYY")
    e2.insert(0, "Number of miles")
    e3.insert(0, "MM:SS")

    e1.configure(fg = "#808080")
    e2.configure(fg = "#808080")
    e3.configure(fg = "#808080")

    e1.grid(row=2, column=1)
    e2.grid(row=3, column=1) 
    e3.grid(row=4, column=1)

    e1.bind('<FocusIn>', entry_click1)
    e2.bind('<FocusIn>', entry_click2)
    e3.bind('<FocusIn>', entry_click3)

    # submit button
    submitButton = Button(root, text='Submit', command=submit, borderless=1)
    submitButton.configure(pady=4, bg = "white", fg = "black", font = ("Open Sans", 14))
    submitButton.grid(row=5, column=1, pady=4)

    # keep running until window closed
    root.mainloop() # keep running until window closed
    print "\n...end of run\n\n"

if __name__ == "__main__":
    app()