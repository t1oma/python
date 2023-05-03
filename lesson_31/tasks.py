from tkinter import *
root = Tk()
root.geometry("550x550")


# task 1
# c = Canvas(root, width=500, height=500, bg="lime")
# a = 0 # Хранение числа(секунд)
# def salam():
#     global a
#     root.after(1000, salam)
#     c.delete("all")
#     a += 1
#     c.create_text(250, 250, text=a, font="Arial 25")
#
# c.create_text(250, 250, text=a, font="Arial 25")
# img = PhotoImage(file="timer.png", width=5).subsample(100,100)
# c.create_image(10, 10, image=img)
# salam() # первичный вызов функции
# c.pack(anchor=CENTER, expand=True)


# task 3
c = Canvas(root, width=500, height=500, bg="white")

a = None
b = None


def lkm(event):
    global a
    a = (event.x, event.y)


def pkm(event):
    global b
    b = (event.x, event.y)


def makeline():
    if a and b:
        c.delete("all")
        c.create_line(a[0], a[-1],
                      b[0], b[-1])


anton = Button(root, text="Тыкни на миняяяя", command=makeline)
anton.pack()

c.bind("<Button-1>", lkm)
c.bind("<Button-3>", pkm)

c.pack(anchor=CENTER, expand=True)
root.mainloop()