import tkinter as tk
from tkinter import filedialog, Text
import os

def runGUI():
    root = tk.Tk()
    canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
    canvas.pack()
    root.mainloop()