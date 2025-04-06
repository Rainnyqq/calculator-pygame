from tkinter import *


width_mon, height_mon = 1920, 1080
window_size :list[int] = [350, 500]
window_pos_x = width_mon // 2 - window_size[0] // 2
window_pos_y = height_mon // 2 - window_size[1] // 2

root = Tk()     # создаем корневой объект - окно
root.title("Калькулятор")     # устанавливаем заголовок окна
root.geometry (f"{window_size[0]}x{window_size[1]}+{window_pos_x}+{window_pos_y}")    # устанавливаем размеры окна
 
label = Label(text="Привет!") # создаем текстовую метку
label.pack()    # размещаем метку в окне
 
root.mainloop()
