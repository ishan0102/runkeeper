# parses running spreadsheet and does basic analysis
from data import *
from app import *

if __name__ == "__main__":
    exec(open("app.py").read())
    # print "\nWelcome to runkeeper.\n"
    # print "You've run " + getDist(sheet_main) + " total miles."
    # print "Your average pace is " + getAvgPace(sheet_main) + " minutes per mile.\n"