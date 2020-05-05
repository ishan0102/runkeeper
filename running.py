# parses running spreadsheet and does basic analysis

# import data analysis modules
import openpyxl
import matplotlib.pyplot as plt

# variable to store spreadsheet location
loc = "/Users/ishanshah/Documents/Programming/Projects/runkeeper/running.xlsx"

# open excel spreadsheet
workbook = openpyxl.load_workbook(loc)
sheet = workbook.active

def getDist():
    sum = 0
    for i in range(2, len(sheet['B']) + 1):
        sum += (sheet.cell(row = i, column = 2)).value
    return sum

def main():
    print("You've run " + str(getDist()) + " total miles.")

main()