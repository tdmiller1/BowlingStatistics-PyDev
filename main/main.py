#==============
#    imports
#==============


import tkinter as tk
from tkinter import Menu
from tkinter import Button
from tkinter import ttk

from webAPI.webAPI import webAPI

class BowlingStatisticsProgram():
    def __init__(self):
        return

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
win.title("Bowling Stats - Python")

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

#-----------------Tab 1 Content-----------------------------------------------------------------
bowling_stats_frame = ttk.LabelFrame(tab1, text="Bowling Statistics")
bowling_stats_frame.grid(column = 0, row =0, padx=8, pady=4)

ttk.Label(bowling_stats_frame, text="Player:").grid(column=0,row=0,sticky='E')

#------------------Combo Box--------------------------------------------------------------------
city = tk.StringVar()
playerSelected = ttk.Combobox(bowling_stats_frame, width=12, textvariable=city)
#TODO - Values comes from api hit as well
playerSelected['values'] = ('Tucker Miller', 'Lakin Lane', 'Mitch Lewis')
playerSelected.grid(column=1, row=0)

max_width = max([len(x) for x in playerSelected['values']])
new_width = max_width
playerSelected.config(width=new_width)

ENTRY_WIDTH = max_width + 3

# Average Score Entry
ttk.Label(bowling_stats_frame, text="Average Score: ").grid(column=0, row = 2, sticky='E')
average=tk.StringVar()
averageEntry = ttk.Entry(bowling_stats_frame, width=ENTRY_WIDTH, textvariable=average, state='readonly')
averageEntry.grid(column=1, row=2, sticky='W')

# Highscore/Max Score Entry
ttk.Label(bowling_stats_frame, text="High Score: ").grid(column=0, row = 3, sticky='E')
highScore=tk.StringVar()
highScoreEntry = ttk.Entry(bowling_stats_frame, width=ENTRY_WIDTH, textvariable=highScore, state='readonly')
highScoreEntry.grid(column=1, row=3, sticky='W')

for child in bowling_stats_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

#------------------URL GRAB------------------------
webAPI = webAPI()
data = webAPI.getPlayers()

players = []
# Set Combobox
for i in (data):
    players.append(i["playerName"])
    currentPlayer = data[0]
    average.set(currentPlayer["average"])
    highScore.set(currentPlayer["max"])

playerSelected['values'] = players
playerSelected.current(0)

# Button Click set data
def update_Entry():
    for i in data:
        if playerSelected.get() == i["playerName"]:
            currentPlayer = i
            average.set(i["average"])
            highScore.set(i["max"])

refreshButton = Button(bowling_stats_frame, text = "Refresh", command = update_Entry)
refreshButton.grid(column=4, row=0)

#-----------------------------Tab 2 Content------------------------------------------------------
bowling_stats_frame = ttk.LabelFrame(tab2, text="End Credits")
bowling_stats_frame.grid(column = 0, row =0, padx=8, pady=4)

ttk.Label(bowling_stats_frame, text="Tucker Miller made this and is still getting the hang of it").grid(column=0,row=0,sticky='E')

#-------------
# Start GUI
# -------------
win.minsize(width=300, height=2)
win.mainloop()