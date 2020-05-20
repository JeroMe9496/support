# IMPORTS
# -----------------------------------------
import tkinter as tk
import random



# THE WINDOW OBJECT
# -----------------------------------------
win = tk.Tk()

# Position and size of the window X x Y + W + H
# win.geometry(f"400x420+760+330")

# Prevents window resizing (if you want)
# win.resizable(False, False)



# FUNCTIONS (the logic of our app)
# -----------------------------------------
# region
def rand():
    result["text"] = random.randrange(10, 100)

def setTexts():
    result["text"] = random.randrange(100, 1000)

def incr():
  value = float(result["text"])
  result["text"] = f"{value + 1}"

def decr():
  value = float(result["text"])
  result["text"] = f"{value - 1}"

def mult():
  value = float(result["text"])
  result["text"] = f"{value * 10}"

def div():
  value = float(result["text"])
  result["text"] = f"{value / 10}"
# endregion



# RESULT (Label)
# -----------------------------------------
# region
result = tk.Label(text="0", padx=20, bg="#fff")
result["font"] = ("Open Sans", 18)
result.pack(pady=40, side=tk.TOP)
# endregion



# BUTTONS (Frame & Buttons)
# -----------------------------------------
# region
# Create a frame to hold the buttons together (frame it's like a div)
frame_btns = tk.Frame()
frame_btns.pack(padx=40, pady=(0, 40), side=tk.BOTTOM)

# Create buttons and associate them with the frame
btn1 = tk.Button(text="-1", command=decr, master=frame_btns)
btn2 = tk.Button(text="/10", command=div, master=frame_btns)
btn3 = tk.Button(text="Randomize", command=rand, master=frame_btns)
btn4 = tk.Button(text="*10", command=mult, master=frame_btns)
btn5 = tk.Button(text="+1", command=incr, master=frame_btns)

# Place the buttons on the grid
btn1.grid(row = 1, column = 0, padx=10)
btn2.grid(row = 1, column = 1, padx=10)
btn3.grid(row = 1, column = 2, padx=10)
btn4.grid(row = 1, column = 3, padx=10)
btn5.grid(row = 1, column = 4, padx=10)
# endregion



# MANDATORY MAIN LOOP
win.mainloop()