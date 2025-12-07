from tkinter import *
import tkinter as tk

root = Tk()
root.title("hello")
root.minsize(width=400,height=400)
#root.geometry("1366x768")

Canvas1 = Canvas(root)
ph = PhotoImage(file='mySchool.png')
Canvas1.create_image(5,5, anchor=NW, image=ph)
Canvas1.pack(expand=True,fill=BOTH)

root.mainloop()
