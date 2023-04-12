import tkinter as tk

root = tk.Tk()

def show_message():
    x = ent.get()
    y = ent2.get(1.0, "end")
    ent.delete(0, 'end')
    ent2.delete(0.0, 'end')
    print(x)
    print(y)


label = tk.Label(text="Введи номер карты")
label.pack()
ent = tk.Entry(root)
ent.pack()
label2 = tk.Label(text="Адрес почты")
label2.pack()
ent2 = tk.Text(root)
ent2.pack()
confirm = tk.Button(text="Отправить", command=show_message)
confirm.pack()


root.mainloop()