import tkinter as tk
from tk import *
import os

# run GUI app #2c6b6f
def runGUI():
    print "\n\nrunning...\n"
    root = tk.Tk()

    root.title("Runkeeper")
    root.geometry("400x400+200+300")
    root.configure(bg = "#2c6b6f")

    greeting = tk.Label(root, text="Welcome to Runkeeper!")
    greeting.configure(bg = "#2c6b6f", fg = "white", font = ("Open Sans", 20), pady=40)
    greeting.pack()


    # button = tk.Button(root, text = "hi")
    # button.pack(side = tk.TOP, pady = 20)


    root.mainloop() # keep running until window closed
    print "\n...end of run\n\n"

runGUI()