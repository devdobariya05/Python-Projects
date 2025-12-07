from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
#import pymysql
import mysql.connector as sql

# Add your own database name and password here to reflect in the code
db="bank"
mypass = "12345"

con = sql.connect(host="localhost",user="root",password='12345',database=db)
cur = con.cursor()

def s():
    
    acno = Info1.get()
    amount = Info2.get()
    dot = Info3.get()
    tt ='D'
    
    S="insert into banktrans values('{}','{}','{}','{}')".format(acno,amount,dot,tt)
    M="update bank_master set balance=balance+{} where acno={}".format(amount,acno)
    try:
        cur.execute(S)
        cur.execute(M)
        con.commit()
        messagebox.showinfo('Success',"deposited Successfully")
    except:
        messagebox.showinfo("Error","Can't Deposit Amount\ncontact developer'")
    

    print(acno)

    Info1.delete(0, END)
    root.destroy()
    
def DepositAmount(): 
    
    global Info1,Info2,Info3,Canvas1,con,cur,Table,root
    
    root = Tk()
    root.title("bank")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="dark green")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="light green",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Deposit Amount", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # accno
    lb1 = Label(labelFrame,text="Acconut No.: ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.35, relheight=0.08)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # amount
    lb2 = Label(labelFrame,text="Amount: ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.50, relheight=0.08)
        
    Info2 = Entry(labelFrame)
    Info2.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # dot
    lb3 = Label(labelFrame,text="D.O.T.: ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.65, relheight=0.08)
        
    Info3 = Entry(labelFrame)
    Info3.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=s)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
