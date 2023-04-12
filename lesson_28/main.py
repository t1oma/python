import tkinter as tk

# def hello(event):
#     print("event=", event)
#     print("Очередной хелло ворлд")

root = tk.Tk() # создаем окно
# root.title("Мой первый ТкИНтКЕР") # заголовок окна
# root.geometry("250x500") # разрешение окна

# photo = tk.PhotoImage(file="tinker.png", height="100") # height - для размера картинки
#
# lab1 = tk.Label(root, text="Опа", image=photo)
# lab1.pack()
#
# btn = tk.Button(root) # master - привязка к окну
# # btn['command'] = hello # действие при нажатие
# btn.bind("<Button-1>", hello) # лкм
# btn.bind("<Double-Button-1>", hello) # 2-йное пкм
# btn.bind("<Button-3>", hello) # пкм
# btn.bind("<Return>", hello)
# btn['text'] = 'Приффки'
# btn['font'] = ('times new roman', 20, "bold") # шрифт
# btn['height'] = 64 # высота
# btn['width'] = 2 # ширина
# btn['foreground'] = 'blue'
# btn['background'] = 'pink' # цвет фона
# btn.pack(anchor="e") # разместить элемент
# anchor=e - привязка на earth (право)

def show_message():
    label['text'] = ent.get() # как очистить поле ввода
    ent.delete(0, 'end')

label = tk.Label(text="приффки")
label.pack()
ent = tk.Entry(root)
ent.pack()
confirm = tk.Button(text="Отправить", command=show_message)
confirm.pack()

root.mainloop()