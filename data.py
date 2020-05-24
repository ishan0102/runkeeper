# this module contains I/O functions for the excel spreadsheet
# and various graphing features

# import excel reading and graph making modules
import openpyxl
from openpyxl.styles import Alignment
import matplotlib.pyplot as plt
from running import *

# open excel spreadsheet 
workbook = openpyxl.load_workbook("running.xlsx")
sheet_main = workbook["main"]
sheet_test = workbook["test"]

def inputData(date, distance, duration, sheet):
    currentRow = findEmpty(sheet_test)
    cell1 = sheet.cell(row = currentRow, column = 1)
    cell2 = sheet.cell(row = currentRow, column = 2)
    cell3 = sheet.cell(row = currentRow, column = 3)
    cell4 = sheet.cell(row = currentRow, column = 4)

    cell1.value = date
    cell2.value = distance
    cell3.value = duration
    cell4.value = calcPace(distance, duration)

    cell1.alignment = Alignment(horizontal='right')
    cell2.alignment = Alignment(horizontal='right')
    cell3.alignment = Alignment(horizontal='right')
    cell4.alignment = Alignment(horizontal='right')

    # save workbook
    workbook.save("running.xlsx")

def findEmpty(sheet):
    i = 1
    while (sheet.cell(row = i, column = 1).value != None):
        i += 1
    return i