from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("300x200")

# CheckButton
# def isChecked(a):
#     print(cb_val.get())
#     cb.deselect() # deselect() - удаление выделения, select() - установка выделения
#
# cb_val = BooleanVar() # переменная, отвечающая за хранение значения
# cb = Checkbutton(root,
#                  text='тинкер',
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False)
#
# cb.bind("<Button-3>", isChecked)
# cb.pack()


# RadioButton
# def get_rb():
#     print(rb_val.get())
#
# rb_val = IntVar()
# print(rb_val.get())
# Radiobutton(root, variable=rb_val, text="Один", value=1, command=get_rb).pack()
# Radiobutton(root, variable=rb_val, text="Два", value=2, command=get_rb).pack()
# Radiobutton(root, variable=rb_val, text="Три", value=3, command=get_rb).pack()


# ListBox
# def pupu():
#     print(lst.curselection()) # curselection - текущий выбор
#
# fdgjndfnj = ["Тортик", "Конфетки", "Пирожки"]
#
# lst = Listbox(root, selectmode=EXTENDED) # EXTENDED - мультивывод, single - один
# lst.pack()
# for elem in fdgjndfnj:
#     lst.insert("end", elem)
#
# btn = Button(root, text='Активировать', command=pupu).pack()


# Scale(Шкала)
# def get_scale(a):
#     print(scal.get())
#
#
# scal = Scale(root, from_=4, to=16,
#              orient=HORIZONTAL,
#              length=200, # длина полосы
#              width=50, # толщина полосы
#              tickinterval=2, # подписать с шагом
#              command=get_scale)
# scal.pack()


# State
# def activate():
#     if btn1['state'] == "disabled": # если кнопка выключена
#         btn1['state'] = "normal"
#     else:
#         btn1['state'] = "disabled"
# btn1 = Button(root, text="Я кнопка")
# btn1.pack()
# btn2 = Button(root, text="хелло мир манера крутит мир", command=activate)
# btn2.pack()


# задача 1
# def activate():
#     if cb_val.get() == True:
#         btn2['state'] = "normal"
#     else:
#         btn2['state'] = "disabled"
#
# cb_val = BooleanVar()
# cb = Checkbutton(root,
#                  text='тинкер',
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False,
#                  command=activate)
# cb.pack()
# btn2 = Button(root, text="хелло мир манера крутит мир", command=activate)
# btn2.pack()


# задача 2
# def get_rb():
#     if rb_val.get() == 1:
#         label['text'] = "тинкер"
#     else:
#         label['text'] = "пак"
#
# rb_val = IntVar()
# print(rb_val.get())
# label = tk.Label(text="тинкер или пак???")
# label.pack()
# Radiobutton(root, variable=rb_val, text="тинкер", value=1, command=get_rb).pack()
# Radiobutton(root, variable=rb_val, text="пак", value=2, command=get_rb).pack()


# задача 4
# def bold():
#     if val_bold.get() == True: # если отметка есть
#         lab["font"] += " bold"
#     else: # когда отметки нет
#         lab["font"] = lab["font"].replace(" bold", "")
#
#
# def italic():
#     if val_italic.get() == True: # если отметка есть
#         lab["font"] += " italic"
#     else: # когда отметки нет
#         lab["font"] = lab["font"].replace(" italic", "")
#
# def underline():
#     if val_underline.get() == True: # если отметка есть
#         lab["font"] += " underline"
#     else: # когда отметки нет
#         lab["font"] = lab["font"].replace(" underline", "")
#
# def overstrike():
#     if val_overstrike.get() == True: # если отметка есть
#         lab["font"] += " overstrike"
#     else: # когда отметки нет
#         lab["font"] = lab["font"].replace(" overstrike", "")
#
# lab = Label(root, text="Я текст", font="Arial 15")
# lab.pack()
#
# val_bold = BooleanVar() # True - есть, False - нет
# cb_bold = Checkbutton(root,
#                       text="Жирный",
#                       command=bold,
#                       variable=val_bold,
#                       onvalue=True,
#                       offvalue=False)
# cb_bold.pack()
#
# val_italic = BooleanVar()
# cb_italic = Checkbutton(root,
#                         text="Курсив",
#                         command=italic,
#                         variable=val_italic,
#                         onvalue=True,
#                         offvalue=False)
# cb_italic.pack()
# val_underline = BooleanVar()
# cb_underline = Checkbutton(root,
#                       text="Подчеркнутый",
#                       command=underline,
#                       variable=val_underline,
#                       onvalue=True,
#                       offvalue=False)
# cb_underline.pack()
# val_overstrike = BooleanVar()
# cb_overstrike = Checkbutton(root,
#                       text="Зачеркнутый",
#                       command=overstrike,
#                       variable=val_overstrike,
#                       onvalue=True,
#                       offvalue=False)
# cb_overstrike.pack()
# cb_bold.pack()


# задача 5

# mas = ['red','green',"blue",'purple','pink','gold']
# def fg(e):
#     root.config(background=mas[val.get()])
#
#
# val = IntVar()
# ck = Scale(root,from_=0,
#            to=5,
#            variable=val,
#            command=fg,
#            orient=HORIZONTAL)
# ck.pack()


# задача 6
ima = PhotoImage(file="уважение.png").subsample(3,3)
lab = Label(root,image=ima)
lab.pack()
root.mainloop()