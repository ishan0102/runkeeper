# this module contains I/O functions for the excel spreadsheet
# and various graphing features

import openpyxl
import matplotlib.pyplot as plt

# open excel spreadsheet
workbook = openpyxl.load_workbook("running.xlsx")
sheet = workbook["main"]