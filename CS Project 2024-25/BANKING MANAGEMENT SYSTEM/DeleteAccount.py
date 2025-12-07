from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
#import pymysql
import mysql.connector as sql

# Add your own database name and password here to reflect in the code
db="bank"
con = sql.connect(host="localhost",user="root",password='12345',database=db)
cur = con.cursor()

def d():
    
    acno = Info1.get()
    S="delete from banktrans where acno={}".format(acno)
    try:
        cur.execute(S)
        con.commit()
        messagebox.showinfo('Success',"deleted Successfully")
    except:
        messagebox.showinfo("invalid info",'check entered info')

    print(S)
    root.destroy()
    
def Delete(): 
    
    global Info1,Canvas1,con,cur,Table,root
    
    root = Tk()
    root.title("bank")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="dark green")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="light green",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Account", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # accno
    lb1 = Label(labelFrame,text="Acconut No.: ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.35, relheight=0.08)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    DELETEBtn = Button(root,text="Delete",bg='#d1ccc0', fg='black',command=d)
    DELETEBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
