import tkinter as tk

win = tk.Tk()

# region Understanding frames
# frame_1 = tk.Frame()
# frame_2 = tk.Frame()

# lbl = tk.Label(master=frame_1, text="Title")
# lbl.pack()
# btn = tk.Button(master=frame_2, text="Change text")
# btn.pack()

# frame_1.pack()
# frame_2.pack()
# endregion

# region Testing fill and entry manip
# ent = tk.Entry(width=40, bg="black", fg="white")
# ent.pack(fill=tk.X)

# ent.insert(0, "What's your name?")
# endregion

# region Testing frames
win.rowconfigure(0, weight=1, minsize=50)
win.columnconfigure([0, 1], weight=1, minsize=100)

frame_lbls = tk.Frame(master=win)
frame_btns = tk.Frame(master=win)

lbl_1 = tk.Label(master=frame_lbls, text="Title 1")
lbl_2 = tk.Label(master=frame_lbls, text="Title 2")

btn1 = tk.Button(master=frame_btns, text="Change text")
btn2 = tk.Button(master=frame_btns, text="Change text")

frame_lbls.grid(row=0, column=0, padx=5, pady=5)
frame_btns.grid(row=0, column=1, padx=5, pady=5)

lbl_1.pack(padx=5, pady=5)
lbl_2.pack(padx=5, pady=5)

btn1.pack(padx=5, pady=5)
btn2.pack(padx=5, pady=5)
# endregion

# region Testing grid
# win.rowconfigure(0, minsize=50)
# win.columnconfigure([0, 1, 2, 3], minsize=50)

# label1 = tk.Label(text="1", bg="black", fg="white")
# label2 = tk.Label(text="2", bg="black", fg="white")
# label3 = tk.Label(text="3", bg="black", fg="white")
# label4 = tk.Label(text="4", bg="black", fg="white")

# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1, sticky="ew")
# label3.grid(row=0, column=2, sticky="ns")
# label4.grid(row=0, column=3, sticky="nsew")
# endregion

# region Making a form
# win.rowconfigure()
# win.columnconfigure()

# Labels
# frame_body = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# frame_body.pack()

# lbl_name = tk.Label(master=frame_body, text="Name:")
# ent_name = tk.Entry(master=frame_body, width=40)
# lbl_name.grid(row=0, column=0, sticky="e")
# ent_name.grid(row=0, column=1)

# lbl_surname = tk.Label(master=frame_body, text="Surname:")
# ent_surname = tk.Entry(master=frame_body, width=40)
# lbl_surname.grid(row=1, column=0, sticky="e")
# ent_surname.grid(row=1, column=1)

# lbl_age = tk.Label(master=frame_body, text="Age:")
# ent_age = tk.Entry(master=frame_body, width=40)
# lbl_age.grid(row=2, column=0, sticky="e")
# ent_age.grid(row=2, column=1)

# def changeTxt():
#   lbl_age["text"] = ent_age.get()

# # Buttons
# frame_buttons = tk.Frame()
# frame_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# btn_submit = tk.Button(master=frame_buttons, text="Submit", command=changeTxt)
# btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# btn_clear = tk.Button(master=frame_buttons, text="Clear")
# btn_clear.pack(side=tk.RIGHT, padx=1, ipadx=1)
# endregion

# ...

win.mainloop()