from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("500x500")

# def get_lst():
#     print(lst.curselection())
#
# spisok = ["один", "два", "три"]
# # второй способ
# spisok_tk = StringVar(value=spisok)
#
#
# lst = Listbox(win, listvariable=spisok_tk, selectmode=EXTENDED)
# lst.pack()
# lst["selectbackground"] = "pink"
# lst["selectforeground"] = "blue"
# lst["selectborderwidth"] = 5
# lst.bind("<<ListBoxSelect>>", get_lst)


# первый способ
# for elem in spisok:
#     lst.insert("end", elem)

# ===== Верхний блок =====
# frame_top = LabelFrame(root, text="Верх") # привязь к win
# frame_top.pack()
# # привязь к рамке
# Label(frame_top, width=7, height=4, bg='yellow', text="1").pack()
# Label(frame_top, width=7, height=4, bg='orange', text="2").pack()

# messagebox.showinfo(title="Инфо", message="Щас бы пельмехи")
# messagebox.showerror()
# messagebox.showwarning()


# пак(в доте который)
# btn1 = Button(win, text="Кнопка1")
# # btn1.pack(pady=5, ipadx=20)
# # btn2 = Button(win, text="Кнопка2")
# # btn2.pack()


# grid()
# btn1 = Button(win, text="Кнопка1")
# btn1.grid(column=0, row=0)
# btn2 = Button(win, text="Кнопка2")
# btn2.grid(column=1, row=0)
# btn3 = Button(win, text="Кнопка3")
# btn3.grid(column=2, row=0)
# btn4 = Button(win, text="Кнопка4")
# btn4.grid(column=0, row=1, columnspan=2, sticky=E)


# .place()
# Button(win, text="-----").place(x=100, y=10)


# .after()
# def hello():
#     print("Запрети мне носить стон айленд")
#     win.after(1000, hello)
#
# win.after(1000, hello)


# .bind()
# def action(bind_e):
#     print("print")
#
# lab = Button(win, text="Приф чд кд", bg="pink")
# lab.pack()
# lab.focus_set()
# lab.bind("<Destroy>", action)


# Переключатель
def switchState():
    if cb_val.get():
       lab["text"] = 'вкл.'
    else:
       lab["text"] = 'выкл.'

switch_on = PhotoImage(width=50, height=50)
switch_off = PhotoImage(width=50, height=50)

# to=(левая граница, верхняя граница, правая граница, нижняя граница)
switch_on.put(("green",), to=(25, 0, 50, 50))
switch_off.put(("red",), to=(0, 0, 25, 50))
cb_val = BooleanVar()
Checkbutton(win, width=50, height=25,
            image=switch_off, selectimage=switch_on,
            onvalue=True, offvalue=False, variable=cb_val,
            indicatoron=False, command=switchState).pack()
lab = Label(win, text="выкл.")
lab.pack()


win.mainloop()