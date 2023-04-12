import tkinter as tk

root = tk.Tk()
root.geometry("5000x5000")

img = tk.PhotoImage(file="tinker.png").subsample(5, 5)
label = tk.Label(image=img)
label.pack()

img2 = img.zoom(2, 1)
label2 = tk.Label(image=img2)
label2.pack()

img3 = img.subsample(2, 2)
label3 = tk.Label(image=img3)
label3.pack()


root.mainloop()