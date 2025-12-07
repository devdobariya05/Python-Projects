from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
#import pymysql
import mysql.connector as sql

def save():
    
    acno= Info1.get()
    name= Info2.get()
    city= Info3.get()
    mobileno= Info4.get()
    balance= Info5.get()
    
    
    insert="INSERT INTO bank_master(acno,name,city,mobileno,balance) VALUES ({},'{}','{}','{}','{}')".format(acno,name,city,mobileno,balance)
    try:
        cur.execute(insert)
        con.commit()
        messagebox.showinfo('Success',"Account Created successfully")
    except:
        messagebox.showinfo("Error","Can't Create Account\nContact Developer ")
    
    root.destroy()
    
def createacc(): 
    
    global Info1,Info2,Info3,Info4,Info5,Canvas1,con,cur,Table,root
    
    root = Tk()
    root.title("K Group of Agro-industries")
    root.minsize(width=400,height=400)
    root.geometry("600x500")        
    # Add your own database name and password here to reflect in the code
    db="bank"
    mypass = "12345"
    con = sql.connect(host="localhost",user="root",password='12345',database=db)
    cur = con.cursor()

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="dark green")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="light green",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Create Account", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Account No.
    lb1 = Label(labelFrame,text="Account No.: ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Name
    lb2 = Label(labelFrame,text="Name: ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    Info2 = Entry(labelFrame)
    Info2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # City
    lb3 = Label(labelFrame,text="City: ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    Info3 = Entry(labelFrame)
    Info3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Ph.No.
    lb4 = Label(labelFrame,text="Ph.No.: ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    Info4 = Entry(labelFrame)
    Info4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    # Balance
    lb5 = Label(labelFrame,text="Balance: ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)
        
    Info5 = Entry(labelFrame)
    Info5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)
    
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=save)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
