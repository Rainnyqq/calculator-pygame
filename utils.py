from tkinter import *
from tkinter import ttk     # подключаем пакет ttk


def window_setup():
    width_mon, height_mon = 1920, 1080
    window_size :list[int] = [350, 500]
    window_pos_x = width_mon // 2 - window_size[0] // 2
    window_pos_y = height_mon // 2 - window_size[1] // 2
    root = Tk()
    root.title("Калькулятор")
    root.geometry (f"{window_size[0]}x{window_size[1]}+{window_pos_x}+{window_pos_y}")
    root.resizable(True, True)
    return root
