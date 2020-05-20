# IMPORTS
# -----------------------------------------
import tkinter as tk
import random



# THE WINDOW OBJECT
# -----------------------------------------
win = tk.Tk()
win.title("Grid Layout with Tkinter")

# Position and size of the window X x Y + W + H
# win.geometry(f"400x420+760+330")

# Prevents window resizing (if you want)
# win.resizable(False, False)



# CREATE ELEMENTS
# -----------------------------------------
display = tk.Entry(win)

btn0 = tk.Button(win, text="0")
btn1 = tk.Button(win, text="1")
btn2 = tk.Button(win, text="2")
btn3 = tk.Button(win, text="3")
btn4 = tk.Button(win, text="4")
btn5 = tk.Button(win, text="5")
btn6 = tk.Button(win, text="6")
btn7 = tk.Button(win, text="7")
btn8 = tk.Button(win, text="8")
btn9 = tk.Button(win, text="9")



# PUT ELEMENTS ON GRID
# -----------------------------------------
display.grid(row=0, column=0, columnspan=3)

btn0.grid(row=4, column=1)
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)



# MANDATORY MAIN LOOP
# -----------------------------------------
win.mainloop()