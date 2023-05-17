#!python3

import tkinter as tk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("560x180")

dogphoto = tk.PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto, borderwidth=3)
dog.grid(row=1, column=1)

button1 = tk.Button(window, text="Search by Name")
button1.place(x=360, y=0)

entry1 = tk.Entry(window, width=15)
entry1.place(x=460, y=3)

bigwords = tk.Label(window,text="Client Database")
bigwords.place(x=230, y=40)

Name = tk.Entry(window,text="Name")
Type = tk.Entry(window,text="Type")
Breed = tk.Entry(window,text="Breed")
Owner = tk.Entry(window,text="Owner")
Birthdate = tk.Entry(window,text="Birthdate")

Name.grid(row=2, column=1)
Type.grid(row=2, column=2)
Breed.grid(row=2, column=3)
Owner.grid(row=2, column=4)
Birthdate.grid(row=2, column=5)


window.mainloop()