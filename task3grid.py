#!python3

import tkinter as tk

window = tk.Tk()
window.title("Example")
window.geometry("235x138")
window.resizable(False,False)

puppyimage = tk.PhotoImage(file="dog.png")
puppy = tk.Label(window, image=puppyimage, borderwidth=3)
puppy.grid(row=1, column=2)

l1 = tk.Label(window, text="Pochacco!")
l1.grid(row=1, column=3)

l2 = tk.Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero", background="#aaffff")
l2.grid(row=2, column=1, columnspan=4)


window.mainloop()