#==============
#    imports
#==============


import tkinter as tk
from tkinter import Menu
from tkinter import ttk


class BowlingStatisticsProgram():
    def __init__(self):
        return

    def test(self, num):
        return num * 2

def _quit():
    win.quit()
    win.destroy()
    exit()

def _new():
    exit()
    
def _about():
    exit()

# Create Intance
win = tk.Tk()

# Add Title
win.title("Python Program - Bowling Stats")

#================
# Start GUI
#===============

menuBar = Menu()
win.config(menu=menuBar)

#==============================================
# Menu Tabs
fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = "New")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

#----------------------- Multiple Tabs------------------------------------------------------------
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = "Tab 1")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = "Tab 2")

tabControl.pack(expand=1, fill="both")

#-----------------------------Tab 1 Content------------------------------------------------------
bowling_stats_frame = ttk.LabelFrame(tab1, text="Bowling Statistics")
bowling_stats_frame.grid(column = 0, row =0, padx=8, pady=4)

ttk.Label(bowling_stats_frame, text="Player:").grid(column=0,row=0,sticky='E')


#------------------Combo Box-------------------------------------------
city = tk.StringVar()
citySelected = ttk.Combobox(bowling_stats_frame, width=12, textvariable=city)
#TODO - Values comes from api hit as well
citySelected['values'] = ('Tucker Miller', 'Lakin Lane', 'Mitch Lewis')
citySelected.grid(column=1, row=0)
citySelected.current(0)

max_width = max([len(x) for x in citySelected['values']])
new_width = max_width
citySelected.config(width=new_width)


ENTRY_WIDTH = max_width + 3

ttk.Label(bowling_stats_frame, text="Last Updated: ").grid(column=0, row = 1, sticky='E')
updated=tk.StringVar()
updatedEntry = ttk.Entry(bowling_stats_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')

ttk.Label(bowling_stats_frame, text="Average Score: ").grid(column=0, row = 2, sticky='E')
average=tk.StringVar()
averageEntry = ttk.Entry(bowling_stats_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
averageEntry.grid(column=1, row=5, sticky='W')

ttk.Label(bowling_stats_frame, text="Wins: ").grid(column=0, row = 5, sticky='E')
wins=tk.StringVar()
winsEntry = ttk.Entry(bowling_stats_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
winsEntry.grid(column=1, row=2, sticky='W')

ttk.Label(bowling_stats_frame, text="High Score: ").grid(column=0, row = 3, sticky='E')
highScore=tk.StringVar()
highScoreEntry = ttk.Entry(bowling_stats_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
highScoreEntry.grid(column=1, row=3, sticky='W')

ttk.Label(bowling_stats_frame, text="Low Score: ").grid(column=0, row = 4, sticky='E')
lowScore=tk.StringVar()
lowScoreEntry = ttk.Entry(bowling_stats_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
lowScoreEntry.grid(column=1, row=4, sticky='W')


#-----------Padding------------------------------------
for child in bowling_stats_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

#------------------URL GRAB------------------------
import urllib.request
    
url_general = 'http://webApi.tuckermillerdev.com/hello/'
request = urllib.request.urlopen(url_general)
string = request.read().decode()


string = string.replace("{","").replace("}","")
new = string.split(":")
updated = new[1]

#-----------------------------Tab 2 Content------------------------------------------------------
bowling_stats_frame = ttk.LabelFrame(tab2, text="End Credits")
bowling_stats_frame.grid(column = 0, row =0, padx=8, pady=4)

ttk.Label(bowling_stats_frame, text="Tucker Miller made this and is still getting the hang of it").grid(column=0,row=0,sticky='E')
#-------------
# Start GUI
# -------------


win.minsize(width=400, height=2)
win.mainloop()