#!python3

import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("420x30")


entry1 = tk.Entry(window, width=15)
entry1.grid(row = 1, column = 1)

lable1 = tk.Label(window,text="x")
lable1.grid(row = 1, column = 2)

entry2 = tk.Entry(window, width=15)
entry2.grid(row = 1, column = 3)

button1 = tk.Button(window, text="=")
button1.grid(row = 1, column = 4)

entry3 = tk.Entry(window, width=30)
entry3.grid(row = 1, column = 5)

window.mainloop()