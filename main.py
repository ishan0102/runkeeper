# parses running spreadsheet and does basic analysis
from running import *

def main():
    execfile("app.py")
    print "\nWelcome to runkeeper.\n"
    print "You've run " + getDist() + " total miles."
    print "Your average pace is " + getAvgPace() + " minutes per mile.\n"

main()