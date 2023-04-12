import tkinter as tk

root = tk.Tk()

def red(event):
     print("event=", event)
     print("Красный")


def orange(event):
    print("event=", event)
    print("Оранжевый")


def yellow(event):
    print("event=", event)
    print("Желтый")


def green(event):
    print("event=", event)
    print("Зеленый")


def blue(event):
    print("event=", event)
    print("Синий")


def purple(event):
    print("event=", event)
    print("Фиолетовый")


btnred = tk.Button(root)
btnred.bind("<Button-1>", red)
btnred['command'] = red
btnred['background'] = 'red'
btnred['width'] = 5
btnred.pack()

btnorange = tk.Button(root)
btnorange.bind("<Button-1>", orange)
btnorange['command'] = orange
btnorange['background'] = 'orange'
btnorange['width'] = 5
btnorange.pack()

btnyellow = tk.Button(root)
btnyellow.bind("<Button-1>", yellow)
btnyellow['command'] = yellow
btnyellow['background'] = 'yellow'
btnyellow['width'] = 5
btnyellow.pack()

btngreen = tk.Button(root)
btngreen.bind("<Button-1>", green)
btngreen['command'] = green
btngreen['background'] = 'green'
btngreen['width'] = 5
btngreen.pack()

btnblue = tk.Button(root)
btnblue.bind("<Button-1>", blue)
btnblue['command'] = blue
btnblue['background'] = 'blue'
btnblue['width'] = 5
btnblue.pack()

btnpurple = tk.Button(root)
btnpurple.bind("<Button-1>", purple)
btnpurple['command'] = purple
btnpurple['background'] = 'purple'
btnpurple['width'] = 5
btnpurple.pack()

root.mainloop()