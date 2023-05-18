#!python3

import tkinter as tk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("560x180")
window.resizable(False,False)

dogphoto = tk.PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto, borderwidth=3)
dog.grid(row=1, column=1)

button1 = tk.Button(window, text="Search by Name")
button1.place(x=360, y=0)

entry1 = tk.Entry(window, width=15)
entry1.place(x=460, y=3)

bigwords = tk.Label(window,text="Client Database")
bigwords.place(x=240, y=40)

Name = tk.Label(window,text="Name")
Type = tk.Label(window,text="Type")
Breed = tk.Label(window,text="Breed")
Owner = tk.Label(window,text="Owner")
Birthdate = tk.Label(window,text="Birthdate")

Name.grid(row=2, column=1)
Type.grid(row=2, column=2)
Breed.grid(row=2, column=3)
Owner.grid(row=2, column=4)
Birthdate.grid(row=2, column=5)

Name2 = tk.Entry(window, width=17)
Type2 = tk.Entry(window, width=17)
Breed2 = tk.Entry(window, width=17)
Owner2 = tk.Entry(window, width=17)
Birthdate2 = tk.Entry(window, width=17)

Name2.grid(row=3, column=1, padx=5, pady=2)
Type2.grid(row=3, column=2, padx=2, pady=2)
Breed2.grid(row=3, column=3, padx=2, pady=2)
Owner2.grid(row=3, column=4, padx=2, pady=2)
Birthdate2.grid(row=3, column=5, padx=2, pady=5)

save = tk.Button(window, text="Save Entry")
save.place(x=250, y=150)

previous = tk.Button(window, text="<Previous")
previous.place(x=3, y=150)

next = tk.Button(window, text="Next>")
next.place(x=510, y=150)

window.mainloop()