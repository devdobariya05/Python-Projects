from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
#import pymysql
import mysql.connector as sql
# Add your own database name and password here to reflect in the code
db="bank"
con = sql.connect(host="localhost",user="root",password='12345',database=db)
cur = con.cursor()

def sav():
    acno = info1.get()
    amount = info2.get()
    dot = info3.get()
    t='W'
    A = "insert into banktrans values('{}','{}','{}','{}')".format(acno,amount,dot,t)
    B ="update bank_master set balance=balance-{} where acno={}".format(amount,acno)

    try:
        cur.execute(A)
        cur.execute(B)
        con.commit()
        messagebox.showinfo('collect your money',"transection successfully done")
    except:
        messagebox.showinfo("Error","contect developer from'Contact Us'")
    
    root.destroy()

def Withdraw(): 
    
    global issueBtn,labelFrame,lb1,info1,info2,info3,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="dark green")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="light green",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Withdraw", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Account No.: : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    info1 = Entry(labelFrame)
    info1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Amount : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    info2 = Entry(labelFrame)
    info2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    # Issued Status 
    lb3 = Label(labelFrame,text="D.O.T. : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.6)
        
    info3 = Entry(labelFrame)
    info3.place(relx=0.3,rely=0.6, relwidth=0.62)
    
    #Issue Button
    issueBtn = Button(root,text="Withdraw",bg='#d1ccc0', fg='black',command=sav)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
