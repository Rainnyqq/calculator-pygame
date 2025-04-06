from tkinter import *
from tkinter import ttk     # подключаем пакет ttk
import utils


root = utils.window_setup()
label = Label(text="Привет!")
label.pack()



def button_1():
    print(1)
btn = ttk.Button(text="1", command=button_1())
btn.place(relx = 0,rely = 0.9, relheight=0.1, relwidth=1/3)

# def button_2():
#     print(2)
# btn = ttk.Button(text="2", command=button_2())
# btn.pack(anchor=S, expand=True, ipadx=10, ipady=15)






root.mainloop()