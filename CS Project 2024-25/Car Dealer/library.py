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
    splashscreen.configure(bg='gray15')

    
    Label(splashscreen, text='CarDeals', font='Impact 30', fg='white', bg='gray15').pack()

    #Add image
    image1 = PhotoImage(file="ban.png")
    label = Label(splashscreen, image=image1, relief = 'raise').pack()
    
    Label(splashscreen, text="Version 1.0", font='Timesnewroman 15 ',relief=RAISED).place(x=570, y=70)
    pgbar = ttk.Progressbar(splashscreen, orient='horizontal', length=600, mode='determinate')
    Label(splashscreen, text="Designed By:Ashish Singh", font='arial 10', fg='black',relief=SUNKEN).place(x=550, y=300)
    Label(splashscreen, text="Car Deals", font='arial 10', bg='gray15', fg='white',bd=10,relief=SUNKEN).place(x=675, y=340)
    pgbar.place(x=70, y=360)
    pgbar['maximum'] = 100
    
    txt=Label(splashscreen,text='0%',relief=GROOVE,bg='gray15',fg='white')#, bg='#345', fg='#fff')
    txt.place(x=650, y=360)
    
    for i in range(101):
        time.sleep(0.04)
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
        self.root.iconbitmap("caricon.ico")
        self.root.title("CAR DEALS")
        self.root.maxsize(width=1550,height=1080)
        self.root.minsize(width=1550,height=1080)
        self.root.geometry("1550x1080+0+0")     #Fixing window size according to monitor resolution
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
        ga='gray11'
        ge='gray20'
        w='white'
        c="courier new cyr"
             
        lblTitle=Label(self.root,text="CarDeals",bg=ga,fg="gold",bd=8,relief=FLAT,\
            font=("impact",40),padx=6,pady=16)
        lblTitle.pack(side=TOP,fill=X)

        self.lbb=Label(self.root,bg=ga)
        self.lbb.place(x=10,y=16, width=370, height=60)
        self.ig=PhotoImage(file='car.png')
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
        
        self.lb1_hr = Label(self.root, text='12', font=(c, 20, 'bold'), bg=ga, fg='white')
        self.lb1_hr.place(x=1050, y=25, width=40, height=30)
        
        self.lb2_hr = Label(self.root, text=':', font=(c, 20, 'bold'), bg=ga, fg='white')
        self.lb2_hr.place(x=1090, y=25, width=20, height=30)
        
        self.lb3_hr = Label(self.root, text='05', font=(c, 20, 'bold'), bg=ga, fg='white')
        self.lb3_hr.place(x=1125, y=25, width=40, height=30)
        
        self.lb4_hr = Label(self.root, text=':', font=(c, 20, 'bold'), bg=ga, fg='white')
        self.lb4_hr.place(x=1160, y=25, width=20, height=30)
        
        self.lb5_hr = Label(self.root, text='37', font=(c, 20, 'bold'), bg=ga, fg='white')
        self.lb5_hr.place(x=1190, y=25, width=40, height=30)
       
        self.lb7_hr = Label(self.root, text='AM', font=(c, 17, 'bold'), bg=ga, fg='white')
        self.lb7_hr.place(x=1230, y=25, width=40, height=30)
     
        clock()
    
       
        frame=Frame(self.root,bd=0,relief=FLAT,padx=30,bg=ga)
        frame.place(x=0,y=90,width=1550,height=400)
        

        #=============================== DataFrame Left ================================================#
        DataFrameLeft=LabelFrame(frame,text="CAR Membership Info",bg=ge,fg='gold',bd=1,padx=5,pady=5,relief="raised", highlightthickness=0,font=(c,18,"bold"))
        DataFrameLeft.place(x=-20,y=0,width=850,height=375)

        lblMember=Label(DataFrameLeft,bg=ge,fg=w,text="Fuel Type",font=(c,13,"bold"),padx=2,pady=3)
        lblMember.grid(row=0,column=0,sticky=W)
        cmbMember=ttk.Combobox(DataFrameLeft,textvariable=self.Member,font=(c,13,"bold"),width=20,state="readonly")
        cmbMember["value"]=("Diesel","Petrol","Electic")
        cmbMember.current(0)
        cmbMember.grid(row=0,column=1,sticky=W)

        lblPRN_No=Label(DataFrameLeft,bg=ge,fg=w,text="Plate  No.",font=(c,13,"bold"),padx=2,pady=3)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft, textvariable=self.PRN_No,font=(c,13),width=20)
        txtPRN_No.grid(row=1,column=1,sticky=W)

        lblMemberID=Label(DataFrameLeft,bg=ge,fg=w,text="Aadhar card  ID",font=(c,12,"bold"),padx=2,pady=3)
        lblMemberID.grid(row=2,column=0,sticky=W)
        txtMemberID=Entry(DataFrameLeft, textvariable=self.MemberID,font=(c,13),width=10)
        txtMemberID.grid(row=2,column=1,sticky=W)
        
        lblFirstName=Label(DataFrameLeft,bg=ge,fg=w,text="First Name",font=(c,12,"bold"),padx=2,pady=3)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft, textvariable=self.FirstName,font=(c,13),width=29)
        txtFirstName.grid(row=3,column=1,sticky=W)

        lblLastName=Label(DataFrameLeft,bg=ge,fg=w,text="Last Name",font=(c,12,"bold"),padx=2,pady=3)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft, textvariable=self.LastName,font=(c,13),width=29)
        txtLastName.grid(row=4,column=1,sticky=W)
        
        lblAddress=Label(DataFrameLeft,bg=ge,fg=w,text="Address",font=(c,12,"bold"),padx=2,pady=3)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft, textvariable=self.Address,font=(c,13),width=29)
        txtAddress.grid(row=5,column=1,sticky=W)
        
        lblPincode=Label(DataFrameLeft,bg=ge,fg=w,text="PIN Code",font=(c,12,"bold"),padx=2,pady=3)
        lblPincode.grid(row=6,column=0,sticky=W)
        txtPincode=Entry(DataFrameLeft, textvariable=self.Pincode,font=(c,13),width=8)
        txtPincode.grid(row=6,column=1,sticky=W)\

        lblMobile=Label(DataFrameLeft,bg=ge,fg=w,text="Mobile No.",font=(c,12,"bold"),padx=2,pady=3)
        lblMobile.grid(row=7,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft, textvariable=self.Mobile,font=(c,13),width=12)
        txtMobile.grid(row=7,column=1,sticky=W)
        
        lblBookID=Label(DataFrameLeft,bg=ge,fg=w,text="Car ID",font=(c,12,"bold"),padx=20,pady=3)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft, textvariable=self.BookID,font=(c,13),width=12)
        txtBookID.grid(row=0,column=3,sticky=W)

        lblBookTitle=Label(DataFrameLeft,bg=ge,fg=w,text="Car Model",font=(c,12,"bold"),padx=20,pady=3)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft, textvariable=self.BookTitle,font=(c,13),width=25)
        txtBookTitle.grid(row=1,column=3,sticky=W)
        
        lblAuthor=Label(DataFrameLeft,bg=ge,fg=w,text="Company",font=(c,12,"bold"),padx=20,pady=3)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft, textvariable=self.Author,font=(c,13),width=25)
        txtAuthor.grid(row=2,column=3,sticky=W)
        
        lblBorrowedOn=Label(DataFrameLeft,bg=ge,fg=w,text="Delivery Date",font=(c,12,"bold"),padx=20,pady=3)
        lblBorrowedOn.grid(row=3,column=2,sticky=W)
        txtBorrowedOn=Entry(DataFrameLeft, textvariable=self.BorrowedOn,font=(c,13),width=15)
        txtBorrowedOn.grid(row=3,column=3,sticky=W)

        lblBorrowedFor=Label(DataFrameLeft,bg=ge,fg=w,text="GST(%)",font=(c,12,"bold"),padx=20,pady=3)
        lblBorrowedFor.grid(row=4,column=2,sticky=W)
        txtBorrowedFor=Entry(DataFrameLeft, textvariable=self.BorrowedFor,font=(c,13),width=15)
        txtBorrowedFor.grid(row=4,column=3,sticky=W)
        
        lblDueDate=Label(DataFrameLeft,bg=ge,fg=w,text="Payment Date",font=(c,12,"bold"),padx=20,pady=3)
        lblDueDate.grid(row=5,column=2,sticky=W)
        txtDueDate=Entry(DataFrameLeft,textvariable=self.DueDate,font=(c,13),width=15)
        txtDueDate.grid(row=5,column=3,sticky=W)

        lblReturnDate=Label(DataFrameLeft,bg=ge,fg=w,text="Token Amount",font=(c,12,"bold"),padx=20,pady=3)
        lblReturnDate.grid(row=6,column=2,sticky=W)
        txtReturnDate=Entry(DataFrameLeft, textvariable=self.ReturnDate,font=(c,13),width=15)
        txtReturnDate.grid(row=6,column=3,sticky=W)
        
        lblDelayDay=Label(DataFrameLeft,bg=ge,fg=w,text="Customisation",font=(c,12,"bold"),padx=20,pady=3)
        lblDelayDay.grid(row=7,column=2,sticky=W)
        txtDelayDay=Entry(DataFrameLeft, textvariable=self.DelayDay,font=(c,13),width=15)
        txtDelayDay.grid(row=7,column=3,sticky=W)
        
        lblLateCharge=Label(DataFrameLeft,bg=ge,fg=w,text="Amount Charged as Fine",font=(c,12,"bold"),padx=20,pady=3)
        lblLateCharge.grid(row=8,column=2,sticky=W)
        txtLateCharge=Entry(DataFrameLeft,textvariable=self.LateCharge,font=(c,13),width=15)
        txtLateCharge.grid(row=8,column=3,sticky=W)        

        lblFinalAmount=Label(DataFrameLeft,bg=ge,fg=w,text="Final Amount",font=(c,15,"bold"),padx=20,pady=3)
        lblFinalAmount.grid(row=9,column=2,sticky=W)
        txtFinalAmount=Entry(DataFrameLeft,textvariable=self.FinalAmount,font=(c,15,"bold"),width=15,fg="green3")
        txtFinalAmount.grid(row=9,column=3,sticky=W)
        
        #=============================== DataFrame Right ================================================#
        DataFrameRight=LabelFrame(frame,text="Car Details",bg=ge,fg='gold',bd=1,relief="raised", highlightthickness=0,font=(c,18,"bold"))
        DataFrameRight.place(x=850,y=5,width=630, height=370)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=28,height=16,padx=2,pady=4,bd=0)
        self.txtBox.grid(row=0,column=3)
        
        ScrollBar2=Scrollbar(DataFrameRight)
        ScrollBar2.grid(row=0,column=5,stick="NS")
        ScrollBar2.config(command=self.txtBox.yview)

        ScrollBar1=Scrollbar(DataFrameRight)
        ScrollBar1.grid(row=0,column=1,stick="NS")

        lstBooks=["Mazda MX-5","Porsche 911","Alpine A110","Porsche 718 Boxster/Cayman's Travel","BMW M3/M4", "McLaren 720S","Toyota GR Supra","Ford Mustang",\
            "Ford Mustang G series","Nissan GT-R","Nissan GT-R 20","Nissan A50","Ford F90","Audi Q8",\
                "Audi Q9","Audi TT","Corvette  P30","BMW M3"]         #Book List created

        def SelectBook(event=""):                       #To add selected book from Book List to the controls in Left Frame
            val=str(lstBox.get(lstBox.curselection()))
            if(val=="Mazda MX-5"):
                self.BookID.set("BKID101")
                self.BookTitle.set("Mazda MX-5")
                self.Author.set(" British sports cars")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("15000.00$")
            elif(val=="Porsche 911"):
                self.BookID.set("BKID102")
                self.BookTitle.set("Porsche 911")
                self.Author.set("Porsche")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("25000.00$")
            elif(val=="Alpine A110"):
                self.BookID.set("BKID103")
                self.BookTitle.set("Alpine A110")
                self.Author.set("Alpine")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500$.00")
                self.DelayDay.set("No")
                self.FinalAmount.set("20000$.00")
            elif(val=="Porsche 718 Boxster/Cayman's Travel"):
                self.BookID.set("BKID104")
                self.BookTitle.set("Porsche 718 Boxster/Cayman's Travel Novel")
                self.Author.set("Porsche")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("20000.00$")
            elif(val=="BMW M3/M4"):
                self.BookID.set("BKID105")
                self.BookTitle.set("BMW M3/M4 Novel")
                self.Author.set("BMW")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("25000.00$")

            elif(val=="McLaren 720S"):
                self.BookID.set("BKID106")
                self.BookTitle.set("McLaren 720S")
                self.Author.set("McLaren")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("240000.00$")

            elif(val=="Toyota GR Supra"):
                self.BookID.set("BKID107")
                self.BookTitle.set("Toyota GR Supra")
                self.Author.set("Toyota")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("260000.00$")

            elif(val=="Ford Mustang"):
                self.BookID.set("BKID108")
                self.BookTitle.set("Ford Mustang")
                self.Author.set("Ford")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("210000.00$")

            elif(val=="Ford Mustang G series"):
                self.BookID.set("BKID109")
                self.BookTitle.set("Ford Mustang G series")
                self.Author.set("Ford")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("210000.00$")

            elif(val=="Nissan GT-R"):
                self.BookID.set("BKID110")
                self.BookTitle.set("Nissan GT-R")
                self.Author.set("Nissan")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("270000.00$")

            elif(val=="Nissan GT-R 20"):
                self.BookID.set("BKID111")
                self.BookTitle.set("Nissan GT-R 20")
                self.Author.set("Nissan")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("270000.00$")

            elif(val=="Nissan A50"):
                self.BookID.set("BKID112")
                self.BookTitle.set("Nissan A50")
                self.Author.set("Nissan")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("280000.00$")

            elif(val=="Ford F90"):
                self.BookID.set("BKID113")
                self.BookTitle.set("Ford F90")
                self.Author.set("Ford")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("280000.00$")

            elif(val=="Audi Q8"):
                self.BookID.set("BKID113")
                self.BookTitle.set("Audi Q8")
                self.Author.set("Audi")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("290000.00$")

            elif(val=="Audi Q9"):
                self.BookID.set("BKID113")
                self.BookTitle.set("Audi Q9")
                self.Author.set("Audi")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("290000.00$")

            elif(val=="Audi TT"):
                self.BookID.set("BKID113")
                self.BookTitle.set("Audi TT ")
                self.Author.set("Audi")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("300000.00$")

            elif(val=="Corvette  P30"):
                self.BookID.set("BKID113")
                self.BookTitle.set("Corvette  P30")
                self.Author.set("Corvette")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("300000.00$")

            elif(val=="BMW M3"):
                self.BookID.set("BKID113")
                self.BookTitle.set("BMW M3")
                self.Author.set("BMW")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BorrowedOn.set(d1)
                self.DueDate.set(d3)
                self.BorrowedFor.set(15)
                self.LateCharge.set("500.00$")
                self.DelayDay.set("No")
                self.FinalAmount.set("310000.00$")
            else:
                pass
        
        lstBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        lstBox.bind("<<ListboxSelect>>",SelectBook)
        lstBox.grid(row=0,column=2,padx=4)
        ScrollBar1.config(command=lstBox.yview) 

        
        for books in lstBooks:              #To add all books from list to the List Control
            lstBox.insert(END,books)

        #====================================== Button Frames ==========================================#
        FrameButton=Frame(self.root,bd=5,relief=FLAT,padx=20,bg=ge)
        FrameButton.place(x=0,y=490,width=1550,height=50)

        btnAddData=Button(FrameButton,command=self.add_data,text="BUY",font=(c,20,"bold"),width=15,bg='gold',fg="white",relief=FLAT,bd=5)
        btnAddData.grid(row=0,column=0,padx=5)

        btnShowData=Button(FrameButton,command=self.show_data,text="SHOW ORDER",font=("arial",12,"bold"),width=15,bg=ga,fg="white",relief=FLAT,bd=5)
        btnShowData.grid(row=0,column=1,padx=5)

        btnUpdateData=Button(FrameButton,command=self.update_data,text="UPDATE ORDER",font=("arial",12,"bold"),width=15,bg=ga,fg="white",relief=FLAT,bd=5)
        btnUpdateData.grid(row=0,column=2,padx=5)
        
        btnDeleteData=Button(FrameButton,command=self.delete_data,text="DELETE ORDER",font=("arial",12,"bold"),width=15,bg=ga,fg="white",relief=FLAT,bd=5)
        btnDeleteData.grid(row=0,column=3,padx=5)

        btnResetData=Button(FrameButton,command=self.reset_data,text="RESET ORDER",font=("arial",12,"bold"),width=15,bg=ga,fg="white",relief=FLAT,bd=5)
        btnResetData.grid(row=0,column=4,padx=5)

        btnExitData=Button(FrameButton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=15,bg='red2',fg="white",relief=FLAT,bd=5)
        btnExitData.grid(row=0,column=5,padx=5)

        #====================================== Information Frames ======================================#
        
        FrameDetails=Frame(self.root,bd=0,relief=FLAT,padx=20,bg=ge)
        FrameDetails.place(x=-25,y=540,width=1550,height=250)
       
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
        self.Library_Table.heading("BookID",text="Car ID")
        self.Library_Table.heading("BookTitle",text="Car Model")
        self.Library_Table.heading("Author",text="Company")
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
        self.Library_Table.column("PRN_No",width=100)
        self.Library_Table.column("MemberID",width=100)
        self.Library_Table.column("FirstName",width=100)
        self.Library_Table.column("LastName",width=100)
        self.Library_Table.column("Address",width=100)
        self.Library_Table.column("Pincode",width=75)
        self.Library_Table.column("Mobile",width=100)
        self.Library_Table.column("BookID",width=100)
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
        messagebox.showinfo("Success","Order has been created successfully.")
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
        messagebox.showinfo("Success","Order has been updated successfully.")
    
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
    
    def show_data(self):#To show data in right-side List Box
        self.txtBox.insert(END,"Fuel Type:\t\t"+self.Member.get()+"\n")
        self.txtBox.insert(END,"Plate  No.:\t\t"+self.PRN_No.get()+"\n")
        self.txtBox.insert(END,"Aadhar card  ID:\t\t"+self.MemberID.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.FirstName.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.LastName.get()+"\n")
        self.txtBox.insert(END,"Address:\t\t"+self.Address.get()+"\n")
        self.txtBox.insert(END,"Pincode:\t\t"+self.Pincode.get()+"\n")
        self.txtBox.insert(END,"Mobile No.:\t\t"+self.Mobile.get()+"\n")
        self.txtBox.insert(END,"Car ID:\t\t"+self.BookID.get()+"\n")
        self.txtBox.insert(END,"Car Model:\t\t"+self.BookTitle.get()+"\n")
        self.txtBox.insert(END,"Company's Name:\t\t"+self.Author.get()+"\n")
        self.txtBox.insert(END,"Delivery Date:\t\t"+self.BorrowedOn.get()+"\n")
        self.txtBox.insert(END,"GST(%):\t\t"+self.BorrowedFor.get()+"\n")
        self.txtBox.insert(END,"Payment Date:\t\t"+self.DueDate.get()+"\n")
        self.txtBox.insert(END,"Token Amount:\t\t"+self.ReturnDate.get()+"\n")
        self.txtBox.insert(END,"Customisation:\t\t"+self.DelayDay.get()+"\n")
        self.txtBox.insert(END,"Amount Charged for registration:\t\t"+self.LateCharge.get()+"\n")
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
        iExit=tkinter.messagebox.askyesno("CarDeals","Do you want to exit?")
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

            messagebox.showinfo("Success","Order has been deleted successfully.")


if __name__=="__main__":            #Infinite loop to run the program
    SplashScreen()
    root=Tk()
    root.attributes('-fullscreen', True)

    obj=LibraryManagementSystem(root)
    root.mainloop()
    
