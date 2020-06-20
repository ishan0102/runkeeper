# Runkeeper
I've been working on this simple GUI app to track my running and do basic data analysis on it. The app currently lets you enter the date, distance, and duration of a run and it will automatically place that data along with your pace in an Excel spreadsheet. You can also make requests to get your total distance and average pace. Overall this was created to help me learn new tools and create something functional.

### Modules
- ***tkinter***: framework for the graphical user interface
- ***openpyxl***: used to read and write to Excel file
- ***numpy***: does mathematical calculations

### Future
- graphing data using *matplotlib*
- adding support for walking and cycling
- download data directly from the Runkeeper API instead of using a GUI

### GUI
Here is an image of the graphical user interface of Runkeeper:
![Runkeeper GUI](/gui.jpg)