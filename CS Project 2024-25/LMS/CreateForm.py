from tkinter import *

root = Tk()
#Draw a Form
root.geometry('1920x1080')
#Add icon
root.iconbitmap('hotel.ico')
#Add title near icon
root.title('Hotel Management System')
#Add background colour
root.config(bg = 'navajo white')

#Title label
label = Label(root, font = ('arial',50,'bold'), width = 1, height = 1, bg = 'navajo white', relief = 'raise', bd = 13, text="Hotel Management System")
label.pack(fill=X)

#Welcome label
label = Label(root, text="WELCOME", bg="purple", fg="white", font=('Orbitron', 25), relief = 'raise', bd = 10)
label.pack(fill=X)

blankspace = Label(root, text="\n")
blankspace.pack()

#Add image
image1 = PhotoImage(file="staff.png")
label = Label(root, image=image1, relief = 'raise', bd = 25)
label.pack()

root.mainloop()
