# Program 2
from tkinter import *
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("300x200+20+10")

btn = Button(window, text="Click to Change Color", activebackground="Yellow")
btn.place(relx=.5, rely=.5, anchor="center")

window.mainloop()