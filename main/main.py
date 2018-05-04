# ==============
#    imports
# ==============


import tkinter as tk
from tkinter import ttk
from tkinter import *

from webAPI.webAPI import WebApi


class BowlingStatisticsProgram:
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


# Create Instance
win = tk.Tk()

# Add Title
win.title("Bowling Stats - Python")

# ================
# Start GUI
# ===============

menuBar = Menu()
win.config(menu=menuBar)

# ==============================================
# Menu Tabs
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# ----------------------- Multiple Tabs------------------------------------------------------------
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Player Data")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Game Data")

tabControl.pack(expand=1, fill="both")

# -----------------Tab 1 Content-----------------------------------------------------------------
bowling_stats_frame = ttk.LabelFrame(tab1, text="Bowling Statistics")
bowling_stats_frame.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(bowling_stats_frame, text="Player:").grid(column=0, row=0, sticky='E')

# ------------------Combo Box--------------------------------------------------------------------
city = tk.StringVar()
playerSelected = ttk.Combobox(bowling_stats_frame, width=12, textvariable=city)
playerSelected['values'] = ('Tucker Miller', 'Lakin Lane', 'Mitch Lewis')
playerSelected.grid(column=1, row=0)

max_width = max([len(x) for x in playerSelected['values']])
new_width = max_width
playerSelected.config(width=new_width)

ENTRY_WIDTH = max_width + 3

# Average Score Entry
ttk.Label(bowling_stats_frame, text="Average Score: ").grid(column=0, row=2, sticky='E')
average = tk.StringVar()
averageEntry = ttk.Entry(bowling_stats_frame, width=ENTRY_WIDTH, textvariable=average, state='readonly')
averageEntry.grid(column=1, row=2, sticky='W')

# High score/Max Score Entry
ttk.Label(bowling_stats_frame, text="High Score: ").grid(column=0, row=3, sticky='E')
highScore = tk.StringVar()
highScoreEntry = ttk.Entry(bowling_stats_frame, width=ENTRY_WIDTH, textvariable=highScore, state='readonly')
highScoreEntry.grid(column=1, row=3, sticky='W')

for child in bowling_stats_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

# ------------------URL GRAB------------------------
WebApi = WebApi()
data = WebApi.get_players()

games = WebApi.get_player_games(1)

players = []
# Set Combobox
for i in data:
    players.append(i["playerName"])
    currentPlayer = data[0]
    average.set(currentPlayer["average"])
    highScore.set(currentPlayer["max"])

playerSelected['values'] = players
playerSelected.current(0)


# Button Click set data
def update_entry():
    for p in data:
        if playerSelected.get() == p["playerName"]:
            average.set(p["average"])
            highScore.set(p["max"])
            newgames = WebApi.get_player_games(p['id'])
            refresh_game_data(newgames)


refreshButton = Button(bowling_stats_frame, text="Refresh", command=update_entry)
refreshButton.grid(column=4, row=0)

# -----------------------------Tab 2 Content------------------------------------------------------
scrollbar = ttk.Scrollbar(tab2)
scrollbar.pack(side=RIGHT, fill=BOTH)
myList = Listbox(tab2, yscrollcommand=scrollbar.set)
myList.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=myList.yview)


def refresh_game_data(newgames):
    counter = 0
    for j in games:
        myList.delete(counter, END)
        counter = counter + 1
    for k in newgames:
        myList.insert(END, "Game: " + str(k['id'] + '  Score: ' + str(k['score'])))


refresh_game_data(games)
# -------------
# Start GUI
# -------------


win.minsize(width=200, height=2)
win.mainloop()
