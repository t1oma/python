import random
from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("500x500")

# Задача 1
# Label(win, text="Логин:").grid(column=0, row=0)
# Label(win, text="Пароль:").grid(column=0, row=1)
# Entry(win, width=20).grid(column=1, row=0,pady=10)
# Entry(win, width=20).grid(column=1, row=1, pady=10)
# Button(win, text="Авторизация").grid(column=1, row=2, sticky=E)


# Задача 2
# from random import randint
# def move(e):
#     btn.place(x=random.randint(0, 300), y=random.randint(0, 300))
#
# btn = Button(win, text="Поймай меня", bg="yellow")
# btn.place(x=10, y=10)
# btn.bind("<Enter>", move)


# Задача 3
# from random import randint
# def switch():
#     rb_val.set(randint(1, 5))
#     win.after(1000, switch)
#
# fr = Frame(win)
# fr.pack(anchor=NW)
#
# rb_val = IntVar()
# rb1 = Radiobutton(fr, variable=rb_val, value=1)
# rb1.pack(side=LEFT)
# rb2 = Radiobutton(fr, variable=rb_val, value=1)
# rb2.pack(side=LEFT)
# rb3 = Radiobutton(fr, variable=rb_val, value=3)
# rb3.pack(side=LEFT)
# rb4 = Radiobutton(fr, variable=rb_val, value=4)
# rb4.pack(side=LEFT)
# rb5 = Radiobutton(fr, variable=rb_val, value=5)
# rb5.pack(side=LEFT)
#
# switch()


# Задача 4
# def func1(bind_e):
#     index1 = lstbox1.curselection()[0]
#     phrase[0] = lst1[index1]
#     ent['state'] = 'normal'
#     ent.delete(0, END) # ОЧИСТКА
#     ent.insert(0, f"{phrase[0]  + '' + phrase[1]}")
#     ent['state'] = 'readonly'
#
# def func2(bind_e):
#     index2 = lstbox2.curselection()[0]
#     phrase[1] = lst2[index2]
#     ent['state'] = 'normal'
#     ent.delete(0, END)  # ОЧИСТКА
#     ent.insert(0, f"{phrase[0] + ' ' + phrase[1]}")
#     ent['state'] = 'readonly'
#
# phrase = ["", ""]
# lst1 = ["обоятельный", "нервный", "здравый", "опасный", "саблезубый", "заниженный", "адекватный"]
# lst2 = ["пакет", "доклад", "гость", "заезд", "поршень", "унитаз", "объект"]
# lst1tk = StringVar(value=lst1)
# lst2tk = StringVar(value=lst2)
#
# lstbox1 = Listbox(win, listvariable=lst1tk, exportselection=False)
# lstbox1.grid(column=0, row=0, padx=10, pady=10)
# lstbox1.bind('<<ListboxSelect>>', func1)
#
# lstbox2 = Listbox(win, listvariable=lst2tk, exportselection=False)
# lstbox2.grid(column=1, row=0, padx=10, pady=10)
# lstbox2.bind('<<ListboxSelect>>', func2)
#
# ent = Entry(win, width=30)
# ent.insert(0, "...")
# ent['state'] = 'readonly'
# ent.grid(column=0, row=1, columnspan=2)


# Задача 5
def hello():
    if gender.get() == 1:
        messagebox.showinfo("хело мир манера крутит мир", f"Мистер {ent1.get()}")
    else:
        messagebox.showinfo("хело мир манера крутит мир", f"Мисис {ent1.get()}")

ent1 = Entry(win)
ent1.grid(row=0, column=1)
ent2 = Entry(win, show="*")


fr = LabelFrame(win, text="Пол")
fr.grid(row=2, column=0, columnspan=2)

gender = IntVar()
rb1 = Radiobutton(fr, text="Мужской", variable=gender, value=1)
rb1.pack()
rb2 = Radiobutton(fr, text="Немужской", variable=gender, value=2)
rb2.pack()

cb = Checkbutton(win, text="Принять хз чо")
cb.grid(row=3, column=0)

btn = Button(win, text="Отправить", command=hello)
btn.grid(row=4, column=0, columnspan=2)



win.mainloop()