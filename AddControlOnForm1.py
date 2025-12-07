from tkinter import *

import tkinter as tk
from tkinter import ttk
import time

root = Tk()

#Draw a Form
root.geometry('1920x1080')

#Add icon
root.iconbitmap('hotel.ico')

#Add title near icon
root.title('Student Management System')

#Add background colour
root.config(bg = 'purple')

#Title label
label = Label(root, font = ('arial',50,'bold'), width = 1, height = 1, bg="purple", fg="white", relief = 'raise', bd = 13, text="Student Management System")
label.pack(fill=X)

#Welcome label
label = Label(root, text="Registration Form", bg="purple", fg="white", font=('Orbitron', 25), relief = 'raise', bd = 10)
label.pack(fill=X)

blankspace = Label(root, text="\n")
blankspace.pack()

#Add image
image1 = PhotoImage(file="staff.png")
label = Label(root, image=image1, relief = 'raise', bd = 5)
label.pack()

labelFrame = Frame(root, bg = 'navajo white', relief = 'ridge', bd = 10,)
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.5)

#Student Name
lb1 = Label(labelFrame,text="Student Name : ", bg='purple', fg='white',relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb1.place(x=50,y=10)#(relx=0.05,rely=0.05, relheight=0.08)
        
bookInfo1 = Entry(labelFrame)
bookInfo1.place(x=365,y=10, relwidth=0.62, relheight=0.08)#(relx=0.3,rely=0.05, relwidth=0.62, relheight=0.08)

#Gender
lb2 = Label(labelFrame,text="Gender : ", bg='purple', fg='white', relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb2.place(x=50,y=60)#(relx=0.05,rely=0.35, relheight=0.08)

var = IntVar()        
Radiobutton(labelFrame,text="Male",bg = 'navajo white',padx= 5, variable= var, value=1).place(x=365,y=60)
Radiobutton(labelFrame,text="Female",bg = 'navajo white',padx= 20, variable= var, value=2).place(x=465,y=60)

#Language
lb3 = Label(labelFrame,text="Language : ", bg='purple', fg='white', relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb3.place(x=50,y=110)#(relx=0.05,rely=0.50, relheight=0.08)
        
var1=IntVar()
Checkbutton(labelFrame,text="Python",bg = 'navajo white',variable=var1).place(x=365,y=110)
var2=IntVar()
Checkbutton(labelFrame,text="Java",bg = 'navajo white',variable=var2).place(x=480,y=110)

#Country
lb4=Label(labelFrame,text="Country : ", bg='purple', fg='white', relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))#text="Country",width=20,font=("bold",10))
lb4.place(x=50,y=160)

list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']
c=StringVar()
droplist=OptionMenu(labelFrame,c, *list_of_country)
droplist.config(bg = 'navajo white',width=15)
c.set('Select your Country')
droplist.place(x=365,y=160)
        
#Submit Button
def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.01)#(0.05)    
        progress['value'] = i
        # Update the GUI
        labelFrame.update_idletasks()  
    progress.stop()

# Create a progressbar widget
progress = ttk.Progressbar(labelFrame, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=195)

# Button to start progress
start_button = Button(labelFrame, text="SUBMIT", command=start_progress)
start_button.place(relx=0.4,rely=0.70, relwidth=0.18,relheight=0.08)#.pack(pady=10)

#SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black')
#SubmitBtn.place(relx=0.4,rely=0.70, relwidth=0.18,relheight=0.08)

#Quit Button    
quitBtn = Button(labelFrame,text="Quit",bg='#f7f1e3', fg='black')
quitBtn.place(relx=0.6,rely=0.70, relwidth=0.18,relheight=0.08)

root.mainloop()
