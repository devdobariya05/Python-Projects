import tkinter
m = tkinter.Tk()
m.geometry('500x500')
m.title("Registration Form")
'''widgets are added here'''
m.mainloop()

from tkinter import *
root = Tk()
#Draw a Form
root.geometry('500x500')
#Add icon
root.iconbitmap('hotel.ico')
#Add title 
root.title('Hotel Management System')
#Add background colour
root.config(bg = 'navajo white')
w = Label(root, text='Ajay Tiwari.org!')
w.pack()
root.mainloop()

import tkinter as tk
r = tk.Tk()
r.geometry('500x500')
r.title('Counting Seconds')
#Add image
image1 = PhotoImage(file="staff.png")
label = Label(r, image=image1, relief = 'raise', bd = 25)
label.pack()
r.mainloop()

import tkinter as tk
r = tk.Tk()
r.geometry('500x500')
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()

from tkinter import *
master = Tk()
master.geometry('500x500')
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()

from tkinter import *
master = Tk()
master.geometry('500x500')
var1 = IntVar()
Checkbutton(master, text='CS', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='IP', variable=var2).grid(row=1, sticky=W)
mainloop()

from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='Male', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Female', variable=v, value=2).pack(anchor=W)
mainloop()

from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()

from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
    
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()

from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()

import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

# Create a label
label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["CS", "IP", "IT"])
combo_box.pack(pady=5)

# Set default value
combo_box.set("Option 1")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", on_select)
root.mainloop()

from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()

from tkinter import *
root = Tk()
root.title('Python')
top = Toplevel()
top.title('MySQL')
top.mainloop()

from tkinter import *
main = Tk()
ourMessage = 'This is our Message'
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop()

from tkinter import *
top = Tk() 
mb = Menubutton ( top, text = "Python") 
mb.grid() 
mb.menu = Menu ( mb, tearoff = 0 ) 
mb["menu"] = mb.menu 
cVar = IntVar() 
aVar = IntVar() 
mb.menu.add_checkbutton ( label ='Contact', variable = cVar ) 
mb.menu.add_checkbutton ( label = 'About', variable = aVar ) 
mb.pack() 
top.mainloop()

import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.05)  
        progress['value'] = i
        # Update the GUI
        root.update_idletasks()  
    progress.stop()

root = tk.Tk()
root.title("Progressbar Example")

# Create a progressbar widget
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# Button to start progress
start_button = tk.Button(root, text="Start Progress", command=start_progress)
start_button.pack(pady=10)
root.mainloop()

from tkinter import *
master = Tk()
w = Spinbox(master, from_=0, to=10)
w.pack()
mainloop()

from tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, 'Ajay Tiwari\nBEST WEBSITE\n')
mainloop()

from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()

from tkinter import *
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
left = Entry(m1, bd=5)
m1.add(left)
m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)
top = Scale(m2, orient=HORIZONTAL)
m2.add(top)
mainloop()

import tkinter as tk
root = tk.Tk()
root.title("Color Options in Tkinter")

# Create a button with active background and foreground colors
button = tk.Button(root, text="Click Me", activebackground="blue", activeforeground="white")
button.pack()

# Create a label with background and foreground colors
label = tk.Label(root, text="Hello, Tkinter!", bg="lightgray", fg="black")
label.pack()

# Create an Entry widget with selection colors
entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black")
entry.pack()
root.mainloop()

import tkinter as tk
root = tk.Tk()
root.title("Pack Example")

# Create three buttons
button1 = tk.Button(root, text="CS")
button2 = tk.Button(root, text="IP")
button3 = tk.Button(root, text="IT")

# Pack the buttons vertically
button1.pack()
button2.pack()
button3.pack()
root.mainloop()

import tkinter as tk
root = tk.Tk()
root.title("Grid Example")

# Create three labels
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")

# Grid the labels in a 2x2 grid
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)
root.mainloop()

import tkinter as tk
root = tk.Tk()
root.title("Place Example")

# Create a label
label = tk.Label(root, text="Label")

# Place the label at specific coordinates
label.place(x=50, y=50)
root.mainloop()

