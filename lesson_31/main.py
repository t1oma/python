from tkinter import *
root = Tk()
root.geometry("550x550")


# background - bg(фон)
# foreground - fg(главный цвет текста)
c = Canvas(root, width=500, height=500, bg='white')

# ====== Текст ===========
# c.create_text(10, 10,
#               text="Чупапи Муняня", anchor=NW,
#               font="Arial 25 italic",
#               fill="gold")


# ====== Прямоугольник ========
# c.create_rectangle(10, 10,
#                    50, 100,
#                    outline="#2d1aa2",
#                    width=5)


# ======= Окружность ========
# c.create_oval(10, 10,
#               50, 100,
#               )


# ======== многоугольник ========
# c.create_polygon(10, 100,
#                  200, 200,
#                  10, 200)


# ======== arc ========
# c.create_oval(10, 10,
#               100, 100,
#               fill="lightblue")
# c.create_arc(10, 10,
#              100, 100,
#              fill="purple",
#              start=-90,
#              extent=-90,
#              style=CHORD) # style=CHORD - сегмент
# c.create_arc(10, 10,
#              100, 100,
#              outline="magenta",
#              start=45,
#              extent=135,
#              width=8,
#              style=ARC) # дуга
# c.create_arc(10, 10,
#              100, 100,
#              fill="pink",
#              start=30, extent=-180)


# ==== line(arrow) =======
# c.create_line(10, 10,
#               250, 250,
#               arrow="both",
#               width=5,
#               arrowshape=(50, 50, 50))


# ========= dash and active ========
# c.create_rectangle(10, 10,
#                    50, 100,
#                    outline="#2d1aa2",
#                    dash="-..",
#                    activewidth=20,
#                    activefill="pink",
#                    width=5)



c.pack(anchor=CENTER, expand=True)

root.mainloop()