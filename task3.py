#!python3

import tkinter as tk

window = tk.Tk()
window.title("Example")
window.geometry("235x130")
window.resizable(False,False)

puppy = tk.PhotoImage(file="dog.png")
puppydog = tk.Label(window, image=puppy, borderwidth=3)
puppydog.place(relx = 0.35, rely = 0.35, anchor = "center")


l1 = tk.Label(window, text="Pochacco!")
l1.place(relx = 0.65, rely = 0.35, anchor = "center")

l2 = tk.Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero", background="#aaffff")
l2.place(x=0,y=95)

window.mainloop()