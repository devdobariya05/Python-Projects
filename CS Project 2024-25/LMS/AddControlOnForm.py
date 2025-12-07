from tkinter import *

root = Tk()
#Draw a Form
root.geometry('1920x1080')
#Add icon
root.iconbitmap('hotel.ico')
#Add title near icon
root.title('Hotel Management System')
#Add background colour
root.config(bg = 'purple')

#Title label
label = Label(root, font = ('arial',50,'bold'), width = 1, height = 1, bg="purple", fg="white", relief = 'raise', bd = 13, text="Hotel Management System")
label.pack(fill=X)

#Welcome label
label = Label(root, text="WELCOME", bg="purple", fg="white", font=('Orbitron', 25), relief = 'raise', bd = 10)
label.pack(fill=X)

blankspace = Label(root, text="\n")
blankspace.pack()

#Add image
image1 = PhotoImage(file="staff.png")
label = Label(root, image=image1, relief = 'raise', bd = 5)
label.pack()

labelFrame = Frame(root, bg = 'navajo white', relief = 'ridge', bd = 10,)
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

#ID
lb1 = Label(labelFrame,text="Customer ID : ", bg='purple', fg='white',relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
bookInfo1 = Entry(labelFrame)
bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

#Name
lb2 = Label(labelFrame,text="Name : ", bg='purple', fg='white', relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
bookInfo2 = Entry(labelFrame)
bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
#Address
lb3 = Label(labelFrame,text="Address : ", bg='purple', fg='white', relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
bookInfo3 = Entry(labelFrame)
bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
#Contact No.
lb4 = Label(labelFrame,text="Contact No. : ", bg='purple', fg='white', relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
bookInfo4 = Entry(labelFrame)
bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
#Submit Button
SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black')
SubmitBtn.place(relx=0.4,rely=0.70, relwidth=0.18,relheight=0.08)

#Quit Button    
quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black')
quitBtn.place(relx=0.6,rely=0.70, relwidth=0.18,relheight=0.08)

root.mainloop()
