import tkinter as tk
from tkinter import messagebox as msgbox
import random as rand

# Window
# region ----------------------------
win = tk.Tk()
# win.geometry("500x400+800+300")
win.rowconfigure([0, 1], weight=1)
win.columnconfigure([0, 1], weight=1)
# endregion -------------------------



# Globals
# region ----------------------------
pad = 20
default_length = 22

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specials = "!#$%&?@"
inc_number = tk.IntVar()
inc_upper = tk.IntVar()
inc_lower = tk.IntVar()
inc_special = tk.IntVar()


# endregion

# region DISPLACE ME LATER


# Functions
# region ----------------------------
def rand_num():
  return str(rand.randrange(0, 9))

def rand_upp():
  return rand.choice(uppers)

def rand_low():
  return rand.choice(lowers)

def rand_spe():
  return rand.choice(specials)


def main_gen():
  # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  gen_list = []

  if inc_number.get():
      gen_list.insert(len(gen_list), rand_num)
  if inc_upper.get():
      gen_list.insert(len(gen_list), rand_low)
  if inc_lower.get():
      gen_list.insert(len(gen_list), rand_upp)
  if inc_special.get():
      gen_list.insert(len(gen_list), rand_spe)

  if not gen_list:
    msgbox.showerror("Error", "Choose at least one parameter!")
    return
  
  out = []

  while(len(out) < int(length_value.get())):
    out.insert(len(out), rand.choice(gen_list)())

    str_out = ""
    for ele in out:
      str_out += ele
  
  output_field.insert(tk.END, f"{str_out}\n")
  # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def length_incr():
  out = int(length_value.get())
  out += 1
  length_value.delete(0, tk.END)
  length_value.insert(0, out)

def length_decr():
  if int(length_value.get()) > 1:
    out = int(length_value.get())
    out -= 1
    length_value.delete(0, tk.END)
    length_value.insert(0, out)

def reset():
  output_field.delete(1.0, tk.END)
  length_value.delete(0, tk.END)
  length_value.insert(0, default_length)
  
  check_numbers.select()
  check_upper.select()
  check_lower.select()
  check_special.deselect()
# endregion



# Title
# region ----------------------------
title = tk.Label(text="Password Generator", padx=pad, pady=pad, font=("Open Sans", 18))
title.pack()
# endregion



# Body
# region ----------------------------------------------------------------
body = tk.Frame()
body.pack()


# Left frame
# region ----------------------------------------------
left = tk.Frame(master=body, relief=tk.SUNKEN, borderwidth=1)
left.grid(row=0, column=0, padx=pad, pady=pad)

# Check buttons
checks = tk.Frame(master=left)
check_numbers = tk.Checkbutton(master=checks, text="Include numbers? (0-9)", variable=inc_number)
check_upper = tk.Checkbutton(master=checks, text="Include uppercase letters? (A-Z)", variable=inc_lower)
check_lower = tk.Checkbutton(master=checks, text="Include lowercase letters? (a-z)", variable=inc_upper)
check_special = tk.Checkbutton(master=checks, text="Include special characters? ($#!)", variable=inc_special)

check_numbers.select()
check_upper.select()
check_lower.select()
check_special.deselect()

checks.grid()
check_numbers.grid(sticky="w")
check_upper.grid(sticky="w")
check_lower.grid(sticky="w")
check_special.grid(sticky="w")
# endregion -------------------------------------------



# Right frame
# region ----------------------------------------------
right = tk.Frame(master=body, relief=tk.SUNKEN, borderwidth=1)
right.grid(row=0, column=1, padx=pad, pady=pad)


# Setting password length
length = tk.Frame(master=right, padx=pad)
length_label = tk.Label(master=length, text="Length")
length_scrollbar = tk.Frame(master=length)


# Custom scrollbar
plus = tk.Button(master=length_scrollbar, text="-", command=length_decr, width=3)
length_value = tk.Entry(master=length_scrollbar)
minus = tk.Button(master=length_scrollbar, text="+", command=length_incr, width=3)

plus.grid(row=0, column=0)
length_value.grid(row=0, column=1, padx=pad)
length_value.insert(0, default_length)
minus.grid(row=0, column=2)


length.grid(row=0, column=0, pady=pad)
length_label.grid(row=0, column=0, sticky="e", ipadx=10)
length_scrollbar.grid(row=0, column=1)


# Generator button and miscs
buttons = tk.Frame(master=right)
buttons_generate = tk.Button(master=buttons, text="Generate", command=main_gen)
buttons_reset = tk.Button(master=buttons, text="Reset", command=reset)
buttons_about = tk.Button(master=buttons, text="About")

buttons.grid(row=1, column=0)
buttons_generate.grid(row=0, column=0)
buttons_reset.grid(row=0, column=1)
buttons_about.grid(row=0, column=2)

# End of right frame
# endregion -------------------------------------------



# End of body
# endregion -------------------------------------------------------------



# Output generation
# region ----------------------------------------------
output_field = tk.Text()
# output_field.tag_config("sel",
#   justify="center"
# )
output_field.pack(padx=pad, pady=pad)
# endregion -------------------------------------------


win.mainloop()