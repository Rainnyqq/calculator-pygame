from tkinter import *
from tkinter import ttk     # подключаем пакет ttk
import utils


root = utils.window_setup()
label = Label(text="Привет!")
label.pack()



def click_button():
    print(1)
btn = ttk.Button(text="Click Me", command=click_button)
btn.pack()






root.mainloop()