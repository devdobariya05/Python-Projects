from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
#import pymysql
import mysql.connector as sql

# Add your own database name and password here to reflect in the code
db="bank"
con = sql.connect(host="localhost",user="root",password='12345',database=db)
cur = con.cursor()
 
def Us(): 
    
    global inf1,inf2,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="dark green")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="dark blue",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Developer's detailes", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # detailes
    lb1 = Label(labelFrame,text="NAME    : Mr. Krish Nariya", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1)

    lb2 = Label(labelFrame,text="CONTACT : krishnariya2003@gmail.com", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.2)

    lb3 = Label(labelFrame,text="CLASS   : 12th SCI", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.3)

    lb4 = Label(labelFrame,text="NOTE    : This Application is only developed for TRUSTED BANK OFFICIAL ONLY", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.4)
    
    #quit Button
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.85, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
