# DOCUMENTATION
# ==================================================================
# https://docs.python.org/3/library/tk.html
# https://docs.python.org/3.8/library/datetime.html



# THE APP
# ==================================================================
# region
# IMPORTS
# ------------------------------------------
import tkinter as tk
from datetime import datetime



# INIT & SHORTCUTS
# ------------------------------------------
# region
# Tk() is the main class from tkinter
gui = tk.Tk()

# Screen width and height
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

# Window width and height
win_width = 500
win_height = 260
win_title_height = 55

# Center the window on screen
win_center_x = int( (screen_width / 2) - (win_width / 2) )
win_center_y = int( (screen_height / 2) - (win_height / 2) - win_title_height)
# ------------------------------------------
# endregion



# WINDOW AND ROW/COLUMN CONFIG
# ------------------------------------------
# region
# Windows size and position as a string. Exemple: "500x200+positionX+positionY"
gui.geometry(f"{win_width}x{win_height}+{win_center_x}+{win_center_y}")

# If you want to block the size of the window
# gui.resizable(False,False)


# Rows/Columns behavior
# Window content → center the content; 
# the "weight" arg permit the row/column to grow if there is space around
gui.rowconfigure(0, weight = 0)
gui.rowconfigure(1, weight = 1)
gui.columnconfigure(0, weight = 1)
# ------------------------------------------
# endregion



# CREATE AND CONFIG CONTENT
# Create 2 widgets "Label" 
# to hold the title and the clock string
# ------------------------------------------
# region
title = tk.Label()
clock = tk.Label()


# Title config
title["text"]   = "Your time is currently :"
title["font"]   = ("Open Sans", 14)
# title["bg"]     = "#f5f5f5"

# Label config
clock["text"]   = "ERROR"
clock["font"]   = ("Open Sans", 32)
clock["bg"]     = "#fff"

# Config variant
# label.config(
#     text = "ERROR",
#     bg = "#f5f5f5",
#     font = ("Open Sans", 18),
# )
# ------------------------------------------
# endregion



# POSITION LABELS TO THE GRID
# ------------------------------------------
# region
# Grid, rows and columns
title.grid(row = 0, column = 0, pady = 20, ipadx = 10, ipady = 2)
clock.grid(row = 1, column = 0, pady = 0, ipadx = 20, ipady = 10)
# ------------------------------------------
# endregion



# FUNCTION TO GET/UPDATE TIME
# ------------------------------------------
# region
def update_time():
    
    # Datetime has to be called here (if stored into a variable, will not update)
    clock["text"] = datetime.now().strftime("%H:%M:%S")

    # Recursive call this function every 1 sec
    gui.after(1000, update_time)

# Call the function
update_time()
# ------------------------------------------
# endregion



# MAINLOOP
# Listen to window events → this is mandatory
# ------------------------------------------
gui.mainloop()



# COMPILE THIS APP TO EXECUTABLE :
# ------------------------------------------
# region
"""
1.  Install pyinstaller
    pip install pyinstaller

2.  cd into your app.py folder

3.  Run pyinstaller with these arguments
    pyinstaller --onefile --noconsole app.py
"""
# ------------------------------------------
# endregion
# ==================================================================
# endregion