#!python3

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Example")
window.geometry("300x130")

puppy = tk.PhotoImage(file="dog.png")
puppydog = tk.Label(window, image=puppy, borderwidth=3)
puppydog.place(relx = 0.4, rely = 0.35, anchor = "center")


l1 = tk.Label(window, text="Pochacco!")
l1.place(relx = 0.6, rely = 0.35, anchor = "center")

l2 = Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero", background="#aaffff")
l2.pack()
l2.place(x=0,y=95)

window.mainloop()