from tkinter import *
from tkinter import ttk     # подключаем пакет ttk
import utils


root = utils.window_setup()
label = Label(text="Привет!")
label.place()

def button_1():
    print(1)
# btn = ttk.Button(text="1", command=button_1())
# btn.place(relx = 0,rely = 0.9, relheight=0.1, relwidth=1/3)



name_label = ttk.Label(root, text="Введите имя")
name_label.pack(anchor=NW)
name_entry = ttk.Entry(root)
name_entry.pack(anchor=NW)


frame_grid = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
for c in range(4): frame_grid.columnconfigure(index=c, weight=1)
for r in range(6): frame_grid.rowconfigure(index=r, weight=1)

for r in range(6):
    for c in range(4):
        # def btn_handler():
        #     print(c, r)
        s = f"({r},{c})"
        btn_handler = lambda: print(c, r)
        btn = ttk.Button(frame_grid, text=f"({r},{c})", command=lambda: print(s))
        btn.grid(row=r, column=c, ipadx=10, ipady=5, padx=0, pady=0, sticky = NSEW)
frame_grid.pack(anchor="s", expand=True)

# def button_2():
#     print(2)
# btn = ttk.Button(text="2", command=button_2())
# btn.pack(anchor=S, expand=True, ipadx=10, ipady=15)
root.mainloop()