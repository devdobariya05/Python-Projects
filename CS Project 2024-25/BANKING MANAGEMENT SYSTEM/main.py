from tkinter import *
#from PIL import ImageTk,Image
#import pymysql
import mysql.connector as sql
from tkinter import messagebox
from createaccount import *
from DepositAmount import *
from DisplayAccount import *
from Withdraw import *
from Contact import *
from TransferAmount import *
from DeleteAccount import *
# Add your own database name and password here to reflect in the code
db="bank"
global con
global cur
con = sql.connect(host="localhost",user="root",password='12345')
cur = con.cursor()
cur.execute("create database if not exists bank")
cur.execute("use bank")
cur.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(15))")
cur.execute("create table if not exists banktrans(acno char (4),amount int(6),dot date,ttype char(1),foreign key (acno) references bank_master(acno))")
#con.commit()


root = Tk()
root.title("bank")
root.minsize(width=400,height=400)
root.geometry("1000x1000")

# Take n greater than 0.25 and less than 5
same=True
n=1.15
# Adding a background image
##background_image =Image.open("p.jfif")
##[imageSizeWidth, imageSizeHeight] = background_image.size
##
##newImageSizeWidth = int(imageSizeWidth*n)
##if same:
##    newImageSizeHeight = int(imageSizeHeight*n) 
##else:
##    newImageSizeHeight = int(imageSizeHeight/n) 
##    
##background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
##img = ImageTk.PhotoImage(background_image)
##
##Canvas1 = Canvas(root)
##
##Canvas1.create_image(300,340,image = img)      
##Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
##Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="dark blue",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="BANK OF \n K GROUP OF AGRO-INDUSTRIES ", bg='medium spring green', fg='black', font=('Perpetua Titling MT',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Create\nAccount",bg='forest green', fg='black', font=('Arial',15), command=createacc)
btn1.place(relx=0.2,rely=0.3, relwidth=0.10,relheight=0.07)
    
btn2 = Button(root,text="Display\nAccount",bg='forest green', fg='black', font=('Arial',15), command=Display)
btn2.place(relx=0.2,rely=0.4, relwidth=0.10,relheight=0.07)

btn7 = Button(root,text="Delete\nAccount",bg='forest green', fg='black', font=('Arial',15), command=Delete)
btn7.place(relx=0.2,rely=0.5, relwidth=0.10,relheight=0.07)
    
btn3 = Button(root,text="Deposit\nAmount",bg='forest green', fg='black', font=('Arial',15), command=DepositAmount)
btn3.place(relx=0.7,rely=0.3, relwidth=0.10,relheight=0.07)
    
btn4 = Button(root,text="Withdraw\nAmount",bg='forest green', fg='black', font=('Arial',15), command =Withdraw)
btn4.place(relx=0.7,rely=0.4, relwidth=0.10,relheight=0.07)

btn5 = Button(root,text="Transfer\nAmount",bg='forest green', fg='black', font=('Arial',15), command = TransferAmount)
btn5.place(relx=0.7,rely=0.5, relwidth=0.10,relheight=0.07)
    
btn6 = Button(root,text="Contact Us",bg='forest green', fg='black', font=('Arial',15), command = Us)
btn6.place(relx=0.7,rely=0.6, relwidth=0.10,relheight=0.07)

root.mainloop()
