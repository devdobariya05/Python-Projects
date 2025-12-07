import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
import datetime as dt
import time
from subprocess import call
#from PIL import Image, ImageTk

def SplashScreen():
    splashscreen = Tk()
    splashscreen.overrideredirect(1)  # Remove Title Bar
    splashscreen.geometry(
        f"800x400+{(splashscreen.winfo_screenwidth() - 800) // 2}+{(splashscreen.winfo_screenheight() - 400) // 2}")
    splashscreen.configure(bg='light blue',bd=10,relief=RAISED)

    
    Label(splashscreen, text='LIBRARY MANAGEMENT SYSTEM', font='Impact 30', fg='maroon', bg='light blue',bd=10,relief=GROOVE).pack()

    #Add image
    image1 = PhotoImage(file="mySchool.png")
    label = Label(splashscreen, image=image1, relief = 'raise', bd = 5).pack()
    
    Label(splashscreen, text="Version 1.0", font='Timesnewroman 15 ', bg='light blue', fg='maroon',bd=10,relief=RAISED).place(x=570, y=70)
    pgbar = ttk.Progressbar(splashscreen, orient='horizontal', length=600, mode='determinate')
    Label(splashscreen, text="Designed By:Ajay Tiwari IT Solution", font='arial 10', bg='light blue', fg='maroon',bd=10,relief=SUNKEN).place(x=550, y=300)
    Label(splashscreen, text="J.B. & KARP", font='arial 10', bg='light blue', fg='maroon',bd=10,relief=SUNKEN).place(x=675, y=340)
    pgbar.place(x=70, y=360)
    pgbar['maximum'] = 100
    
    txt=Label(splashscreen,text='0%',relief=GROOVE,bg='light blue',fg='maroon')#, bg='#345', fg='#fff')
    txt.place(x=650, y=360)
    
    for i in range(101):
        time.sleep(0.001)
        pgbar['value'] = i
        pgbar.update()
        txt['text']=pgbar['value'],'%'
        
    splashscreen.destroy()

    splashscreen.mainloop()

mydb=sql.connect(host="localhost",user="root",password="12345")#connection to mysql 
mycur=mydb.cursor()
mycur.execute("create database if not exists mylibrary")
mycur.execute("use mylibrary")
mycur.execute('Create table if not exists bookdetails(Member varchar(30), PRN_No varchar(30), MemberID varchar(30), \
FirstName varchar(30), LastName varchar(30), Address varchar(50), \
Pincode varchar(30), Mobile varchar(30), BookID varchar(30), \
BookTitle varchar(30), Author varchar(30), BorrowedOn varchar(30), BorrowedFor varchar(30), DueDate varchar(30),\
ReturnDate varchar(30), DelayDay varchar(30), LateCharge varchar(30), FinalAmount varchar(30))')
'''
mycur.execute("create table if not exists appointment"
            "("
            "idno varchar(12) primary key,"
            "name char(50),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")

'''
class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap("aa.ico")
        self.root.title("Library Management System")
        self.root.maxsize(width=1550,height=1080)
        self.root.minsize(width=550,height=580)
        #self.root.geometry("1550x1080+0+0")     #Fixing window size according to monitor resolution
        #=============================== Variable Details ================================================#
        self.Member=StringVar()
        self.PRN_No=StringVar()
        self.MemberID=StringVar()
        self.FirstName=StringVar()
        self.LastName=StringVar()
        self.Address=StringVar()
        self.Pincode=StringVar()
        self.Mobile=StringVar()
        self.BookID=StringVar()
        self.BookTitle=StringVar()
        self.Author=StringVar()
        self.BorrowedOn=StringVar()
        self.BorrowedFor=StringVar()
        self.DueDate=StringVar()
        self.ReturnDate=StringVar()
        self.DelayDay=StringVar()
        self.LateCharge=StringVar()
        self.FinalAmount=StringVar()
             
        lblTitle=Label(self.root,text="J. B. & KARP Library Management System",bg="sky blue",fg="green",bd=5,relief=RIDGE,\
            font=("times new roman",40,"bold"),padx=2,pady=2)
        lblTitle.pack(side=TOP,fill=X)

        self.lbb=Label(self.root,bg='sky blue')
        self.lbb.place(x=8,y=6, width=65, height=65)
        self.ig=PhotoImage(file='library.png')
        self.lbb.config(image=self.ig)
        
        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))

            if int(h) >=12 and int(m) >=0:
                self.lb7_hr.config(text="PM")

            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)

            self.lb1_hr.after(200, clock)
        
        self.lb1_hr = Label(self.root, text='12', font=('times new roman', 20, 'bold'), bg='sky blue', fg='white')
        self.lb1_hr.place(x=1180, y=25, width=40, height=30)
        
        self.lb2_hr = Label(self.root, text=':', font=('times new roman', 20, 'bold'), bg='sky blue', fg='white')
        self.lb2_hr.place(x=1220, y=25, width=20, height=30)
        
        self.lb3_hr = Label(self.root, text='05', font=('times new roman', 20, 'bold'), bg='sky blue', fg='white')
        self.lb3_hr.place(x=1230, y=25, width=40, height=30)
        
        self.lb4_hr = Label(self.root, text=':', font=('times new roman', 20, 'bold'), bg='sky blue', fg='white')
        self.lb4_hr.place(x=1270, y=25, width=20, height=30)
        
        self.lb5_hr = Label(self.root, text='37', font=('times new roman', 20, 'bold'), bg='sky blue', fg='white')
        self.lb5_hr.place(x=1280, y=25, width=40, height=30)
       
        self.lb7_hr = Label(self.root, text='AM', font=('times new roman', 17, 'bold'), bg='sky blue', fg='white')
        self.lb7_hr.place(x=1320, y=25, width=40, height=30)
     
        clock()
  
        #=============================== DataFrame Left ================================================#
        frame=Frame(self.root,bd=5,relief=RIDGE,padx=30,bg="sky blue")
        frame.place(x=0,y=90,width=1550,height=400)
        DataFrameLeft=LabelFrame(frame,text="J. B. & KARP Library Membership Info",bg="powder blue",fg="green",bd=5,relief=RIDGE,font=("times new roman",16,"bold"))
        DataFrameLeft.place(x=0,y=5,width=700,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",13,"bold"),padx=2,pady=3)
        lblMember.grid(row=0,column=0,sticky=W)
        cmbMember=ttk.Combobox(DataFrameLeft,textvariable=self.Member,font=("times new roman",13,"bold"),width=15,state="readonly")
        cmbMember["value"]=("Administrator","Teacher","Student")
        cmbMember.current(0)
        cmbMember.grid(row=0,column=1,sticky=W)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No.",font=("times new roman",13,"bold"),padx=2,pady=3)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft, textvariable=self.PRN_No,font=("times new roman",13),width=15)
        txtPRN_No.grid(row=1,column=1,sticky=W)

        lblMemberID=Label(DataFrameLeft,bg="powder blue",text="Member ID",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblMemberID.grid(row=2,column=0,sticky=W)
        txtMemberID=Entry(DataFrameLeft, textvariable=self.MemberID,font=("times new roman",13),width=15)
        txtMemberID.grid(row=2,column=1,sticky=W)
        
        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft, textvariable=self.FirstName,font=("times new roman",13),width=15)
        txtFirstName.grid(row=3,column=1,sticky=W)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft, textvariable=self.LastName,font=("times new roman",13),width=15)
        txtLastName.grid(row=4,column=1,sticky=W)
        
        lblAddress=Label(DataFrameLeft,bg="powder blue",text="Address",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft, textvariable=self.Address,font=("times new roman",13),width=15)
        txtAddress.grid(row=5,column=1,sticky=W)
        
        lblPincode=Label(DataFrameLeft,bg="powder blue",text="PIN Code",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblPincode.grid(row=6,column=0,sticky=W)
        txtPincode=Entry(DataFrameLeft, textvariable=self.Pincode,font=("times new roman",13),width=15)
        txtPincode.grid(row=6,column=1,sticky=W)\

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile No.",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblMobile.grid(row=7,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft, textvariable=self.Mobile,font=("times new roman",13),width=15)
        txtMobile.grid(row=7,column=1,sticky=W)
        
        lblBookID=Label(DataFrameLeft,bg="powder blue",text="Book ID",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft, textvariable=self.BookID,font=("times new roman",13),width=15)
        txtBookID.grid(row=0,column=3,sticky=W)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft, textvariable=self.BookTitle,font=("times new roman",13),width=15)
        txtBookTitle.grid(row=1,column=3,sticky=W)
        
        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author's Name",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft, textvariable=self.Author,font=("times new roman",13),width=15)
        txtAuthor.grid(row=2,column=3,sticky=W)
        
        lblBorrowedOn=Label(DataFrameLeft,bg="powder blue",text="Borrowed From Date",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblBorrowedOn.grid(row=3,column=2,sticky=W)
        txtBorrowedOn=Entry(DataFrameLeft, textvariable=self.BorrowedOn,font=("times new roman",13),width=15)
        txtBorrowedOn.grid(row=3,column=3,sticky=W)

        lblBorrowedFor=Label(DataFrameLeft,bg="powder blue",text="Borrowed For (Days)",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblBorrowedFor.grid(row=4,column=2,sticky=W)
        txtBorrowedFor=Entry(DataFrameLeft, textvariable=self.BorrowedFor,font=("times new roman",13),width=15)
        txtBorrowedFor.grid(row=4,column=3,sticky=W)
        
        lblDueDate=Label(DataFrameLeft,bg="powder blue",text="Due Date",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblDueDate.grid(row=5,column=2,sticky=W)
        txtDueDate=Entry(DataFrameLeft,textvariable=self.DueDate,font=("times new roman",13),width=15)
        txtDueDate.grid(row=5,column=3,sticky=W)

        lblReturnDate=Label(DataFrameLeft,bg="powder blue",text="Actual Return Date",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblReturnDate.grid(row=6,column=2,sticky=W)
        txtReturnDate=Entry(DataFrameLeft, textvariable=self.ReturnDate,font=("times new roman",13),width=15)
        txtReturnDate.grid(row=6,column=3,sticky=W)
        
        lblDelayDay=Label(DataFrameLeft,bg="powder blue",text="No. of Delay Day(s)",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblDelayDay.grid(row=7,column=2,sticky=W)
        txtDelayDay=Entry(DataFrameLeft, textvariable=self.DelayDay,font=("times new roman",13),width=15)
        txtDelayDay.grid(row=7,column=3,sticky=W)
        
        lblLateCharge=Label(DataFrameLeft,bg="powder blue",text="Amount Charged as Fine",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblLateCharge.grid(row=8,column=2,sticky=W)
        txtLateCharge=Entry(DataFrameLeft,textvariable=self.LateCharge,font=("times new roman",13),width=15)
        txtLateCharge.grid(row=8,column=3,sticky=W)

        lblFinalAmount=Label(DataFrameLeft,bg="powder blue",text="Final Amount",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblFinalAmount.grid(row=9,column=2,sticky=W)
        txtFinalAmount=Entry(DataFrameLeft,textvariable=self.FinalAmount,font=("times new roman",13),width=15)
        txtFinalAmount.grid(row=9,column=3,sticky=W)
        
        #=============================== DataFrame Right ================================================#
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=5,relief=RIDGE,font=("times new roman",16,"bold"))
        DataFrameRight.place(x=700,y=5,width=620, height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=30,height=16,padx=2,pady=4,bd=5)
        self.txtBox.grid(row=0,column=3)
        
        ScrollBar2=Scrollbar(DataFrameRight)
        ScrollBar2.grid(row=0,column=5,stick="NS")
        ScrollBar2.config(command=self.txtBox.yview)

        ScrollBar1=Scrollbar(DataFrameRight)
        ScrollBar1.grid(row=0,column=1,stick="NS")

        lstBooks=["Panchtantra","Rangbhoomi","Godan","Gulliver's Travel","Nothing Last Forever", "Hogi Aapki Jeet","Chandrakanta","Sara Aakash",\
            "Bharat Ki Khoj","First World War","Second World War","Jungle Book","The Lord of the Rings","The Kite Runner",\
                "Meera Ke Dohe","Wings of Fire","Power of Positive Thinking","One Day Life Will Change"]         #Book List created

        def SelectBook(event=""):                       #To add selected book from Book List to the controls in Left Frame
            val=str(lstBox.get(lstBox.curselection()))
            if(val=="Panchtantra"):
                self.BookID.set("BKID101")
                self.BookTitle.set("Panchtantra Stories")
                self.Author.set("Vishnu Sharma")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("150.00")
            elif(val=="Rangbhoomi"):
                self.BookID.set("BKID102")
                self.BookTitle.set("Rangbhoomi Novel")
                self.Author.set("Munsi Premchand")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("250.00")
            elif(val=="Godan"):
                self.BookID.set("BKID103")
                self.BookTitle.set("Godan Novel")
                self.Author.set("Munsi Premchand")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("200.00")
            elif(val=="Gulliver's Travel"):
                self.BookID.set("BKID104")
                self.BookTitle.set("Gulliver's Travel Novel")
                self.Author.set("Jonathan Swift")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("200.00")
            elif(val=="Nothing Last Forever"):
                self.BookID.set("BKID105")
                self.BookTitle.set("Nothing Last Forever Novel")
                self.Author.set("Roderick Thorp")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("250.00")

            elif(val=="Hogi Aapki Jeet"):
                self.BookID.set("BKID106")
                self.BookTitle.set("Hogi Aapki Jeet Novel")
                self.Author.set("Shiv Khera")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("240.00")

            elif(val=="Chandrakanta"):
                self.BookID.set("BKID107")
                self.BookTitle.set("Chandrakanta Novel")
                self.Author.set("Devaki Nandan Khatri")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("260.00")

            elif(val=="Sara Aakash"):
                self.BookID.set("BKID108")
                self.BookTitle.set("Sara Aakash Novel")
                self.Author.set("Basu Chatterjee")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("210.00")

            elif(val=="Bharat Ki Khoj"):
                self.BookID.set("BKID109")
                self.BookTitle.set("Bharat Ki Khoj Novel")
                self.Author.set("Jawaharlal Nehru")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("210.00")

            elif(val=="First World War"):
                self.BookID.set("BKID110")
                self.BookTitle.set("First World War Novel")
                self.Author.set("John Keegan")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("270.00")

            elif(val=="Second World War"):
                self.BookID.set("BKID111")
                self.BookTitle.set("Second World War Novel")
                self.Author.set("Antony Beevor")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("270.00")

            elif(val=="Jungle Book"):
                self.BookID.set("BKID112")
                self.BookTitle.set("Jungle Book Novel")
                self.Author.set("Rudyard Kipling")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("280.00")

            elif(val=="The Lord of the Rings"):
                self.BookID.set("BKID113")
                self.BookTitle.set("The Lord of the Rings Novel")
                self.Author.set("J. R. R. Tolkien")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("280.00")

            elif(val=="The Kite Runner"):
                self.BookID.set("BKID113")
                self.BookTitle.set("The Kite Runner Novel")
                self.Author.set("Khaled Hosseini")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("290.00")

            elif(val=="Meera Ke Dohe"):
                self.BookID.set("BKID113")
                self.BookTitle.set("Meera Ke Dohe Novel")
                self.Author.set("Meera")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("290.00")

            elif(val=="Wings of Fire"):
                self.BookID.set("BKID113")
                self.BookTitle.set("Wings of Fire Novel")
                self.Author.set("A. P. J. Abdul Kalam")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("300.00")

            elif(val=="Power of Positive Thinking"):
                self.BookID.set("BKID113")
                self.BookTitle.set("Power of Positive Thinking Novel")
                self.Author.set("Norman Vincent Peale")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("300.00")

            elif(val=="One Day Life Will Change"):
                self.BookID.set("BKID113")
                self.BookTitle.set("One Day Life Will Change Novel")
                self.Author.set("Suranya Umakanthan ")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("50.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("310.00")
            else:
                pass
        
        lstBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=30,height=15,bd=5)
        lstBox.bind("<<ListboxSelect>>",SelectBook)
        lstBox.grid(row=0,column=0,padx=4)
        ScrollBar1.config(command=lstBox.yview) 

        
        for books in lstBooks:              #To add all books from list to the List Control
            lstBox.insert(END,books)

        #====================================== Button Frames ==========================================#
        FrameButton=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=490,width=1400,height=50)

        btnAddData=Button(FrameButton,command=self.add_data,text="Add FLAT",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=FLAT,bd=5)
        btnAddData.grid(row=0,column=0,padx=12)

        btnShowData=Button(FrameButton,command=self.show_data,text="Show RAISED",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=RAISED,bd=5)
        btnShowData.grid(row=0,column=1,padx=12)

        btnUpdateData=Button(FrameButton,command=self.update_data,text="Update SUNKEN",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=SUNKEN,bd=5)
        btnUpdateData.grid(row=0,column=2,padx=12)

        btnDeleteData=Button(FrameButton,command=self.delete_data,text="Delete GROOVE",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=GROOVE,bd=5)
        btnDeleteData.grid(row=0,column=3,padx=12)

        btnResetData=Button(FrameButton,command=self.reset_data,text="Reset RIDGE",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=RIDGE,bd=5)
        btnResetData.grid(row=0,column=4,padx=12)

        btnExitData=Button(FrameButton,command=self.iExit,text="Exit RIDGE",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=RIDGE,bd=5)
        btnExitData.grid(row=0,column=5,padx=12)

        #====================================== Information Frames ======================================#
        
        FrameDetails=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=540,width=1400,height=250)
       
        xScroll=ttk.Scrollbar(FrameDetails,orient=HORIZONTAL)
        yScroll=ttk.Scrollbar(FrameDetails,orient=VERTICAL)

        self.Library_Table=ttk.Treeview(FrameDetails,column=("Member","PRN_No","MemberID","FirstName","LastName","Address","Pincode","Mobile",\
            "BookID","BookTitle","Author","BorrowedOn","BorrowedFor","DueDate","ReturnDate","DelayDay","LateCharge","FinalAmount"),\
                x=xScroll.set,y=yScroll.set)            #Creating table to show the books borrowed information in tabular form
        xScroll.pack(side=BOTTOM,fill=X)                #Adding horizontal scrollbar to the table
        yScroll.pack(side=RIGHT,fill=Y)                 #Adding vertical scrollbar to the table

        xScroll.config(command=self.Library_Table.xview)    #Binding scrollbar to the table
        yScroll.config(command=self.Library_Table.yview)
        
        self.Library_Table.heading("Member",text="Member Type")     #Creating heading in table for all fields
        self.Library_Table.heading("PRN_No",text="PRN Number")
        self.Library_Table.heading("MemberID",text="Member ID")
        self.Library_Table.heading("FirstName",text="First Name")
        self.Library_Table.heading("LastName",text="Last Name")
        self.Library_Table.heading("Address",text="Address") 
        self.Library_Table.heading("Pincode",text="Pincode")
        self.Library_Table.heading("Mobile",text="Mobile No.")
        self.Library_Table.heading("BookID",text="Book ID")
        self.Library_Table.heading("BookTitle",text="Book Title")
        self.Library_Table.heading("Author",text="Author")
        self.Library_Table.heading("BorrowedOn",text="Borrowed On")
        self.Library_Table.heading("BorrowedFor",text="Borrowed For")
        self.Library_Table.heading("DueDate",text="Due Date")
        self.Library_Table.heading("ReturnDate",text="Return Date")
        self.Library_Table.heading("DelayDay",text="Delay Day(s)")
        self.Library_Table.heading("LateCharge",text="Late Charge")
        self.Library_Table.heading("FinalAmount",text="Final Amount")
        
        self.Library_Table["show"]="headings"
        self.Library_Table.pack(fill=BOTH,expand=1)

        self.Library_Table.column("Member",width=100)                   #Fixing the width of all fields
        self.Library_Table.column("PRN_No",width=50)
        self.Library_Table.column("MemberID",width=50)
        self.Library_Table.column("FirstName",width=100)
        self.Library_Table.column("LastName",width=100)
        self.Library_Table.column("Address",width=100)
        self.Library_Table.column("Pincode",width=100)
        self.Library_Table.column("Mobile",width=100)
        self.Library_Table.column("BookID",width=50)
        self.Library_Table.column("BookTitle",width=100)
        self.Library_Table.column("Author",width=100)
        self.Library_Table.column("BorrowedOn",width=100)
        self.Library_Table.column("BorrowedFor",width=100)
        self.Library_Table.column("DueDate",width=100)
        self.Library_Table.column("ReturnDate",width=100)
        self.Library_Table.column("DelayDay",width=100)
        self.Library_Table.column("LateCharge",width=100)
        self.Library_Table.column("FinalAmount",width=100)

        self.fetch_data()       #TO show data in the table below.
        self.Library_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):         #Add_Data function to save records in Library database
        mydb=sql.connect(host="localhost",user="root",passwd="12345",database="mylibrary")
        mycur=mydb.cursor()

        mycur.execute("insert into bookdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.Member.get(),
                                                                                                        self.PRN_No.get(),
                                                                                                        self.MemberID.get(),
                                                                                                        self.FirstName.get(),
                                                                                                        self.LastName.get(),
                                                                                                        self.Address.get(),
                                                                                                        self.Pincode.get(),
                                                                                                        self.Mobile.get(),
                                                                                                        self.BookID.get(),
                                                                                                        self.BookTitle.get(),
                                                                                                        self.Author.get(),
                                                                                                        self.BorrowedOn.get(),
                                                                                                        self.BorrowedFor.get(),
                                                                                                        self.DueDate.get(),
                                                                                                        self.ReturnDate.get(),
                                                                                                        self.DelayDay.get(),
                                                                                                        self.LateCharge.get(),
                                                                                                        self.FinalAmount.get(),
                                                                                                        ))
        mydb.commit()
        self.fetch_data()
        messagebox.showinfo("Success","Member has been created successfully.")
        mycur.close()

    def update_data(self):         #Update_Data function to update records in Library database
        mydb=sql.connect(host="localhost",user="root",passwd="12345",database="mylibrary")
        mycur=mydb.cursor()
        mycur.execute("update bookdetails set Member=%s,MemberID=%s,FirstName=%s,LastName=%s,Address=%s,Pincode=%s,Mobile=%s,\
            BookID=%s,BookTitle=%s,Author=%s,BorrowedOn=%s,BorrowedFor=%s,DueDate=%s,ReturnDate=%s,DelayDay=%s,\
            LateCharge=%s,FinalAmount=%s where PRN_No=%s",(
                                                         self.Member.get(),
                                                         self.MemberID.get(),
                                                         self.FirstName.get(),
                                                         self.LastName.get(),
                                                         self.Address.get(),
                                                         self.Pincode.get(),
                                                         self.Mobile.get(),
                                                         self.BookID.get(),
                                                         self.BookTitle.get(),
                                                         self.Author.get(),
                                                         self.BorrowedOn.get(),
                                                         self.BorrowedFor.get(),
                                                         self.DueDate.get(),
                                                         self.ReturnDate.get(),
                                                         self.DelayDay.get(),
                                                         self.LateCharge.get(),
                                                         self.FinalAmount.get(),
                                                         self.PRN_No.get()
                                                         ))
        mydb.commit()
        self.fetch_data()
        self.reset_data()
        mydb.close()
        messagebox.showinfo("Success","Member has been updated successfully.")
    
    def fetch_data(self):           #Function to access all records from the bookdetails table
        mydb=sql.connect(host="localhost",user="root",passwd="12345",database="mylibrary")
        mycur=mydb.cursor()
        mycur.execute("select * from bookdetails")
        rows=mycur.fetchall()

        if len(rows)!=0:            #To delete previous data from the table
            self.Library_Table.delete(*self.Library_Table.get_children())
            for i in rows:
                self.Library_Table.insert("",END,values=i)
            mydb.commit()
        mydb.close()

    def get_cursor(self,event=""):           #To focus the curosr on the table
        cursor_row=self.Library_Table.focus()
        content=self.Library_Table.item(cursor_row)
        row=content["values"]
        self.Member.set(row[0]),    #To show the values from table to their respective field in the second frame.
        self.PRN_No.set(row[1]),
        self.MemberID.set(row[2]),
        self.FirstName.set(row[3]),
        self.LastName.set(row[4]),
        self.Address.set(row[5]),
        self.Pincode.set(row[6]),
        self.Mobile.set(row[7]),
        self.BookID.set(row[8]),
        self.BookTitle.set(row[9]),
        self.Author.set(row[10]),
        self.BorrowedOn.set(row[11]),
        self.BorrowedFor.set(row[12]),
        self.DueDate.set(row[13]),
        self.ReturnDate.set(row[14]),
        self.DelayDay.set(row[15]),
        self.LateCharge.set(row[16]),
        self.FinalAmount.set(row[17])
    
    def show_data(self):                #To show data in right-side List Box
        self.txtBox.insert(END,"Member Type:\t\t"+self.Member.get()+"\n")
        self.txtBox.insert(END,"PRN No.:\t\t"+self.PRN_No.get()+"\n")
        self.txtBox.insert(END,"Member ID:\t\t"+self.MemberID.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.FirstName.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.LastName.get()+"\n")
        self.txtBox.insert(END,"Address:\t\t"+self.Address.get()+"\n")
        self.txtBox.insert(END,"Pincode:\t\t"+self.Pincode.get()+"\n")
        self.txtBox.insert(END,"Mobile No.:\t\t"+self.Mobile.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.BookID.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.BookTitle.get()+"\n")
        self.txtBox.insert(END,"Author's Name:\t\t"+self.Author.get()+"\n")
        self.txtBox.insert(END,"Borrowed Date:\t\t"+self.BorrowedOn.get()+"\n")
        self.txtBox.insert(END,"Borrowed For (Days):\t\t"+self.BorrowedFor.get()+"\n")
        self.txtBox.insert(END,"Due Date:\t\t"+self.DueDate.get()+"\n")
        self.txtBox.insert(END,"Return Date:\t\t"+self.ReturnDate.get()+"\n")
        self.txtBox.insert(END,"Delay Day(s):\t\t"+self.DelayDay.get()+"\n")
        self.txtBox.insert(END,"Late Charge:\t\t"+self.LateCharge.get()+"\n")
        self.txtBox.insert(END,"Final Amount:\t\t"+self.FinalAmount.get())

    def reset_data(self):               #To reset values of all controls
        self.Member.set(""),    
        self.PRN_No.set(""),
        self.MemberID.set(""),
        self.FirstName.set(""),
        self.LastName.set(""),
        self.Address.set(""),
        self.Pincode.set(""),
        self.Mobile.set(""),
        self.BookID.set(""),
        self.BookTitle.set(""),
        self.Author.set(""),
        self.BorrowedOn.set(""),
        self.BorrowedFor.set(""),
        self.DueDate.set(""),
        self.ReturnDate.set(""),
        self.DelayDay.set(""),
        self.LateCharge.set(""),
        self.FinalAmount.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete_data(self):
        if self.PRN_No.get()=="" or self.MemberID.get()=="":
            messagebox.showerror("Error!!!","First select the Member.")
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="12345",database="mylibrary")
            mycur=mydb.cursor()
            query="delete from bookdetails where PRN_No=%s"
            value=(self.PRN_No.get(),)
            mycur.execute(query,value)

            mydb.commit()
            self.fetch_data()
            self.reset_data()
            mydb.close()

            messagebox.showinfo("Success","Member has been deleted successfully.")


if __name__=="__main__":            #Infinite loop to run the program
    SplashScreen()
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
