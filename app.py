import tkinter as tk
from tkmacosx import Button
import time
from data import *

# called when submit button is pressed to store data
def submit():
    date = e1.get()
    distance = e2.get()
    duration = e3.get()
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)

    try:
        status.configure(text = "Entry recorded successfully")
        inputData(date, distance, duration, sheet_main)
    except Exception:
        status.configure(text = "Please format inputs\nas specified :^)")

# called when total distance button is pressed
def grab_dist():
    return None

# called when average pace button is pressed
def grab_avgpace():
    return None

# called when total time button is pressed
def grab_totaltime():
    return None

# called when entry fields are pressed to clear default text
def entry_click1(e):
    e1.delete(0, tk.END)
    e1.configure(fg = "black")
    status.configure(text = "Enter date in MM/DD/YY\nEx. 05/26/20")

def entry_click2(e):
    e2.delete(0, tk.END)
    e2.configure(fg = "black")
    status.configure(text = "Enter distance in miles\nEx. 1.58")

def entry_click3(e):
    e3.delete(0, tk.END)
    e3.configure(fg = "black")
    status.configure(text = "Enter duration in HH:MM:SS\nEx. 24:38")

def app():
    # begin gui
    global root
    root = tk.Tk()

    # root window
    root.title("Runkeeper")
    root.geometry("520x280+1300+300")
    root.configure(bg = "#2c6b6f")

    # greeting labels
    greeting1 = tk.Label(root, text="Add Data")
    greeting1.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 18), pady = 16)
    greeting1.grid(row = 0, column = 1, sticky = tk.N)

    greeting2 = tk.Label(root, text="Enter info below:")
    greeting2.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), pady = 4)
    greeting2.grid(row = 1, column = 1)

    greeting3 = tk.Label(root, text="See Running Stats")
    greeting3.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 18), pady = 16)
    greeting3.grid(row = 0, column = 3, sticky = tk.N)

    greeting2 = tk.Label(root, text="Analysis options:")
    greeting2.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), pady = 4)
    greeting2.grid(row = 1, column = 3)

    # spacer
    blank1 = tk.Label(root, text="space")
    blank1.configure(bg = "#2c6b6f", fg = "#2c6b6f")
    blank1.grid(row=0, column=2)

    # status label
    global status
    status = tk.Label(root, text="Welcome to Runkeeper!")
    status.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), pady = 4)
    status.grid(row = 6, column = 1)

    # item labels
    labels = [tk.Label(root, text = "Date"), tk.Label(root, text = "Distance"), tk.Label(root, text = "Duration")]

    labels[0].grid(row = 2)
    labels[1].grid(row = 3)
    labels[2].grid(row = 4)

    labels[0].configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), padx = 5, pady = 4)
    labels[1].configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), padx = 5, pady = 4)
    labels[2].configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14), padx = 5, pady = 4)

    # entry boxes
    global e1, e2, e3
    e1 = tk.Entry(root)
    e2 = tk.Entry(root)
    e3 = tk.Entry(root)

    e1.insert(0, "10/21/21")
    e2.insert(0, "3.52")
    e3.insert(0, "01:22:17")

    e1.configure(fg = "#808080")
    e2.configure(fg = "#808080")
    e3.configure(fg = "#808080")

    e1.grid(row = 2, column = 1)
    e2.grid(row = 3, column = 1) 
    e3.grid(row = 4, column = 1)

    e1.bind('<FocusIn>', entry_click1)
    e2.bind('<FocusIn>', entry_click2)
    e3.bind('<FocusIn>', entry_click3)

    # submit button
    submitButton = Button(root, text='Submit', command = submit, borderless = 1)
    submitButton.configure(pady = 4, bg = "white", fg = "black", font = ("Open Sans", 14))
    submitButton.grid(row = 5, column = 1, pady = 4)

    # total distance button
    submitButton = Button(root, text='Total Distance', command = grab_dist, borderless = 1)
    submitButton.configure(pady = 4, bg = "white", fg = "black", font = ("Open Sans", 14))
    submitButton.grid(row = 2, column = 3)

    # average pace button
    submitButton = Button(root, text='Average Pace', command = grab_avgpace, borderless = 1)
    submitButton.configure(pady = 4, bg = "white", fg = "black", font = ("Open Sans", 14))
    submitButton.grid(row = 3, column = 3)

    # total time button
    submitButton = Button(root, text='Total Time', command = grab_totaltime, borderless = 1)
    submitButton.configure(pady = 4, bg = "white", fg = "black", font = ("Open Sans", 14))
    submitButton.grid(row = 4, column = 3)

    # data analysis text
    global stats_text
    stats_text = tk.Label(root, text="Press a button to view \nyour running statistics")
    stats_text.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 14))
    stats_text.grid(row = 5, column = 3)

    # keep running until window closed
    root.mainloop() # keep running until window closed

if __name__ == "__main__":
    app()