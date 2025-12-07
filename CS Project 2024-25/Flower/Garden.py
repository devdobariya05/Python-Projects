
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector as sql
import datetime as dt
import time
from subprocess import call
from PIL import Image, ImageTk

def SplashScreen():
    splashscreen = Tk()
    splashscreen.overrideredirect(1)  
    splashscreen.geometry(f"900x450+{(splashscreen.winfo_screenwidth() - 900) //2}+{(splashscreen.winfo_screenheight() - 450) // 2}")
    splashscreen.configure(bd=10,relief=SUNKEN)


    image1 = PhotoImage(file="12345.png")
    label = Label(splashscreen, image=image1, relief = 'raise', bd = 5).pack()

    Label(splashscreen, text='FLOWER GARDEN MANAGEMENT SYSTEM', font='Impact 30', fg='lightblue',bd=4 , bg='black',relief=GROOVE).place(x=140,y=10)
    
    Label(splashscreen, text="Version 1.0", font='Timesnewroman 14 ', bg='black', fg='orange',bd=5,relief=RAISED).place(x=750, y=70)
    pgbar = ttk.Progressbar(splashscreen, orient='horizontal', length=700, mode='indeterminate')
    Label(splashscreen, text="Designed By: Bhargav Dobariya ", font='Algerian 12', bg='black', fg='orange',bd=10,relief=SUNKEN).place(x=580, y=280)
    Label(splashscreen, text="12th Science-B", font='arial 15', bg='black', fg='orange',bd=3,relief=SUNKEN).place(x=730, y=245)
    pgbar.place(x=70, y=370)
    pgbar['maximum'] = 100
    
    txt=Label(splashscreen,text='0%',font='calibri 12',relief=GROOVE,bg='black',fg='orange')
    txt.place(x=732, y=395)
    
    for i in range(101):
        time.sleep(0.01)
        pgbar['value'] = i
        pgbar.update()
        txt['text']=pgbar['value'],'%'
        
    splashscreen.destroy()
    

    splashscreen.mainloop()

mydb=sql.connect(host="localhost",user="root",password="12345") 
mycur=mydb.cursor()
mycur.execute("create database if not exists z")
mycur.execute("use z")
mycur.execute('Create table if not exists Flowerdetails(Member varchar(30), SR_No varchar(30), CostumerID varchar(30), \
FirstName varchar(30), LastName varchar(30), Address varchar(50), \
Pincode varchar(30), Mobile varchar(30), FlowerID varchar(30), \
FlowerName varchar(30), Supplier varchar(30), BoughtOn varchar(30), DeliverDate varchar(30),\
Status varchar(30), FlowerAge varchar(30), DeliveryCharge varchar(30), FinalAmount varchar(30))')

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

 
class ShopManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap("New Picture.ico")
        self.root.title("FLOWER GARDEN MANAGEMENT SYSTEM")
        self.root.geometry("1350x750+0+0")              
        #=============================== Variable Details ================================================#
        self.Member=StringVar()
        self.SR_No=StringVar()
        
        self.CostumerID=StringVar()
        self.FirstName=StringVar()
        self.LastName=StringVar()
        self.Address=StringVar()
        self.Pincode=StringVar()
        self.Mobile=StringVar()
        self.FlowerID=StringVar()
        self.FlowerName=StringVar()
        self.Supplier=StringVar()
        self.BoughtOn=StringVar()
         
        self.DeliverDate=StringVar()
        self.Status=StringVar()
        self.FlowerAge=StringVar()
        self.DeliveryCharge=StringVar()
        self.FinalAmount=StringVar()
             
        lblTitle=Label(self.root,text="Flower Manual",bg="black",fg="orange",bd=20,relief=RIDGE,\
            font=("times new roman",50,"bold"),padx=2,pady=2)
        lblTitle.pack(side=TOP,fill=X)

        self.lbb=Label(self.root,bg='black')
        self.lbb.place(x=23,y=23, width=73, height=73)
        self.ig=PhotoImage(file='1234.png')
        self.lbb.config(image=self.ig)
        
        def clock():
            
            M = str(time.strftime("%B"))
            Y = str(time.strftime("%Y"))
            d = str(time.strftime("%D"))
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))

            if int(h) >=12 and int(m) >=0:
                self.lb7_hr.config(text="PM")

            self.lb0_hr.config(text=d)
            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)
            self.lb9_hr.config(text=M)
            self.lb11_hr.config(text=Y)
            

            self.lb1_hr.after(200, clock)

        self.lb0_hr = Label(self.root, text='', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb0_hr.place(x=1150, y=50, width=20, height=30)

        self.lb2_hr = Label(self.root, text=':', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb2_hr.place(x=1272, y=50, width=10, height=30)

        self.lb9_hr = Label(self.root, text='', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb9_hr.place(x=1180, y=50, width=87, height=30)
        
        self.lb2_hr = Label(self.root, text=':', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb2_hr.place(x=1170, y=50, width=10, height=30)
        
        self.lb1_hr = Label(self.root, text='12', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb1_hr.place(x=1150, y=25, width=20, height=30)
        
        self.lb2_hr = Label(self.root, text=':', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb2_hr.place(x=1170, y=25, width=10, height=30)
        
        self.lb3_hr = Label(self.root, text='05', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb3_hr.place(x=1190, y=25, width=20, height=30)
        
        self.lb4_hr = Label(self.root, text=':', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb4_hr.place(x=1210, y=25, width=10, height=30)
        
        self.lb5_hr = Label(self.root, text='37', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb5_hr.place(x=1230, y=25, width=20, height=30)
       
        self.lb7_hr = Label(self.root, text='AM', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb7_hr.place(x=1260, y=25, width=40, height=30)

        self.lb11_hr = Label(self.root, text='', font=('times new roman', 15, 'bold'), bg='black', fg='pink')
        self.lb11_hr.place(x=1285, y=50, width=40, height=30)
     
        clock()
    
       
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        frame.place(x=0,y=120,width=1366,height=400)
        

        #=============================== DataFrame Left ================================================#
        DataFrameLeft=LabelFrame(frame,text="Shop Membership Info",bg="black",fg="red",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=790,height=350)

        lblMember=Label(DataFrameLeft,bg="black",fg="orange",text="Member Type",font=("times new roman",13,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        cmbMember=ttk.Combobox(DataFrameLeft,textvariable=self.Member,font=("times new roman",13,"bold"),width=20,state="readonly")
        cmbMember["value"]=("Owner","Staff","customer")
        cmbMember.current(0)
        cmbMember.grid(row=0,column=1,sticky=W)

        lblSR_No=Label(DataFrameLeft,bg="black",fg="orange",text="Sr. no.",font=("times new roman",13,"bold"),padx=2,pady=3)
        lblSR_No.grid(row=1,column=0,sticky=W)
        txtSR_No=Entry(DataFrameLeft, textvariable=self.SR_No,font=("times new roman",13),width=20)
        txtSR_No.grid(row=1,column=1,sticky=W)

        lblCostumerID=Label(DataFrameLeft,bg="black",fg="orange",text="Costumer id",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblCostumerID.grid(row=2,column=0,sticky=W)
        txtCostumerID=Entry(DataFrameLeft, textvariable=self.CostumerID,font=("times new roman",13),width=20)
        txtCostumerID.grid(row=2,column=1,sticky=W)
        
        lblFirstName=Label(DataFrameLeft,bg="black",fg="orange",text="First Name",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft, textvariable=self.FirstName,font=("times new roman",13),width=20)
        txtFirstName.grid(row=3,column=1,sticky=W)

        lblLastName=Label(DataFrameLeft,bg="black",fg="orange",text="Last Name",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft, textvariable=self.LastName,font=("times new roman",13),width=20)
        txtLastName.grid(row=4,column=1,sticky=W)
        
        lblAddress=Label(DataFrameLeft,bg="black",fg="orange",text="Address",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft, textvariable=self.Address,font=("times new roman",13),width=20)
        txtAddress.grid(row=5,column=1,sticky=W)
        
        lblPincode=Label(DataFrameLeft,bg="black",fg="orange",text="PIN Code",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblPincode.grid(row=6,column=0,sticky=W)
        txtPincode=Entry(DataFrameLeft, textvariable=self.Pincode,font=("times new roman",13),width=20)
        txtPincode.grid(row=6,column=1,sticky=W)

        lblMobile=Label(DataFrameLeft,bg="black",fg="orange",text="Mobile No.",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblMobile.grid(row=7,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft, textvariable=self.Mobile,font=("times new roman",13),width=20)
        txtMobile.grid(row=7,column=1,sticky=W)
        
        lblFlowerID=Label(DataFrameLeft,bg="black",fg="orange",text="FlowerID",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblFlowerID.grid(row=0,column=2,sticky=W)
        txtFlowerID=Entry(DataFrameLeft, textvariable=self.FlowerID,font=("times new roman",13),width=25)
        txtFlowerID.grid(row=0,column=3,sticky=W)

        lblFlowerName=Label(DataFrameLeft,bg="black",fg="orange",text="Flower Name",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblFlowerName.grid(row=1,column=2,sticky=W)
        txtFlowerName=Entry(DataFrameLeft, textvariable=self.FlowerName,font=("times new roman",13),width=25)
        txtFlowerName.grid(row=1,column=3,sticky=W)
        
        lblSupplier=Label(DataFrameLeft,bg="black",fg="orange",text="Supplier",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblSupplier.grid(row=2,column=2,sticky=W)
        txtSupplier=Entry(DataFrameLeft, textvariable=self.Supplier,font=("times new roman",13),width=25)
        txtSupplier.grid(row=2,column=3,sticky=W)
        
        lblBoughtOn=Label(DataFrameLeft,bg="black",fg="orange",text="Bought on",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblBoughtOn.grid(row=3,column=2,sticky=W)
        txtBoughtOn=Entry(DataFrameLeft, textvariable=self.BoughtOn,font=("times new roman",13),width=25)
        txtBoughtOn.grid(row=3,column=3,sticky=W)
      
        lblDeliverDate=Label(DataFrameLeft,bg="black",fg="orange",text="Deliver Date",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblDeliverDate.grid(row=4,column=2,sticky=W)
        txtDeliverDate=Entry(DataFrameLeft,textvariable=self.DeliverDate,font=("times new roman",13),width=25)
        txtDeliverDate.grid(row=4,column=3,sticky=W)

        lblStatus=Label(DataFrameLeft,bg="black",fg="orange",text="status",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblStatus.grid(row=5,column=2,sticky=W)
        txtStatus=Entry(DataFrameLeft, textvariable=self.Status,font=("times new roman",13),width=25)
        txtStatus.grid(row=5,column=3,sticky=W)
        
        lblFlowerAge=Label(DataFrameLeft,bg="black",fg="orange",text="Flower's Age [Day(s)]",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblFlowerAge.grid(row=6,column=2,sticky=W)
        txtFlowerAge=Entry(DataFrameLeft, textvariable=self.FlowerAge,font=("times new roman",13),width=25)
        txtFlowerAge.grid(row=6,column=3,sticky=W)
        
        lblDeliveryCharge=Label(DataFrameLeft,bg="black",fg="orange",text="Delivery charge",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblDeliveryCharge.grid(row=7,column=2,sticky=W)
        txtDeliveryCharge=Entry(DataFrameLeft,textvariable=self.DeliveryCharge,font=("times new roman",13),width=25)
        txtDeliveryCharge.grid(row=7,column=3,sticky=W)

        lblFinalAmount=Label(DataFrameLeft,bg="black",fg="orange",text="Final Amount",font=("times new roman",12,"bold"),padx=20,pady=3)
        lblFinalAmount.grid(row=8,column=2,sticky=W)
        txtFinalAmount=Entry(DataFrameLeft,textvariable=self.FinalAmount,font=("times new roman",13),width=25)
        txtFinalAmount.grid(row=8,column=3,sticky=W)
        
        #=============================== DataFrame Right ================================================#
        DataFrameRight=LabelFrame(frame,text="flower Details",bg="black",fg="red",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=800,y=5,width=520, height=350)


        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=27,height=15,padx=2,pady=4,bd=8)
        self.txtBox.grid(row=0,column=3)
        
        ScrollBar2=Scrollbar(DataFrameRight)
        ScrollBar2.grid(row=0,column=5,stick="NS")
        ScrollBar2.config(command=self.txtBox.yview)

        ScrollBar1=Scrollbar(DataFrameRight)
        ScrollBar1.grid(row=0,column=1,stick="NS")

        lstFlowers=["Allium","Alstroemeria","Amaryllis","Anemone","Anthurium", "Bells of Ireland","Carnation","Dahlia",\
            "Freesia","Hibiscus","Lily","Lotus","Marigolds","Orchid","Poppy","Ranunculus",\
                "Rose","Spider Mum"]         

        def SelectFlower(event=""):                       
            val=str(lstBox.get(lstBox.curselection()))
            if(val=="Allium"):
                self.FlowerID.set("BKID101")
                self.FlowerName.set("Allium Flower")
                self.Supplier.set("Holland")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)  
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("150.00")
            elif(val=="Alstroemeria"):
                self.FlowerID.set("BKID102")
                self.FlowerName.set("Alstroemeria Flower")
                self.Supplier.set("South America")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("250.00")
            elif(val=="Amaryllis"):
                self.FlowerID.set("BKID103")
                self.FlowerName.set("Amaryllis Flower")
                self.Supplier.set("Netherlands")


                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("200.00")
            elif(val=="Anemone"):
                self.FlowerID.set("BKID104")
                self.FlowerName.set("Anemone Flower")
                self.Supplier.set("Japan")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("200.00")
            elif(val=="Anthurium"):
                self.FlowerID.set("BKID105")
                self.FlowerName.set("Anthurium Flower")
                self.Supplier.set("Northern Argentina")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("250.00")

            elif(val=="Bells of Ireland"):
                self.FlowerID.set("BKID106")
                self.FlowerName.set("Bells of Ireland Flower")
                self.Supplier.set("Ireland")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("240.00")

            elif(val=="Carnation"):
                self.FlowerID.set("BKID107")
                self.FlowerName.set("Carnation Flower")
                self.Supplier.set("Italy")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3) 
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("260.00")

            elif(val=="Dahlia"):
                self.FlowerID.set("BKID108")
                self.FlowerName.set("Dahlia Flower")
                self.Supplier.set("Mexico")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("210.00")

            elif(val=="Freesia"):
                self.FlowerID.set("BKID109")
                self.FlowerName.set("Freesia Flower")
                self.Supplier.set("Kenya")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("210.00")

            elif(val=="Hibiscus"):
                self.FlowerID.set("BKID110")
                self.FlowerName.set("Hibiscus Flower")
                self.Supplier.set("Malaysia")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("270.00")

            elif(val=="Lily"):
                self.FlowerID.set("BKID111")
                self.FlowerName.set("Lily Flower")
                self.Supplier.set("Europe")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)                 
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("270.00")

            elif(val=="Lotus"):
                self.FlowerID.set("BKID112")
                self.FlowerName.set("Lotus Flower")
                self.Supplier.set("India,China")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)                 
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("280.00")

            elif(val=="Marigolds"):
                self.FlowerID.set("BKID113")
                self.FlowerName.set("Marigolds")
                self.Supplier.set("France")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)                 
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("280.00")

            elif(val=="Orchid"):
                self.FlowerID.set("BKID113")
                self.FlowerName.set("Orchid Flower")
                self.Supplier.set("Asia")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)                 
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("290.00")

            elif(val=="Poppy"):
                self.FlowerID.set("BKID113")
                self.FlowerName.set("Poppy Flower")
                self.Supplier.set("Canada")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)                 
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("290.00")

            elif(val=="Ranunculus"):
                self.FlowerID.set("BKID113")
                self.FlowerName.set("Ranunculus Flower")
                self.Supplier.set("America")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)                 
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("300.00")

            elif(val=="Rose"):
                self.FlowerID.set("BKID113")
                self.FlowerName.set("Rose Flower")
                self.Supplier.set("China")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)                 
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("300.00")

            elif(val=="Spider Mum"):
                self.FlowerID.set("BKID113")
                self.FlowerName.set("Spider Mum Flower")
                self.Supplier.set("canada")

                d1=dt.date.today()
                d2=dt.timedelta(days=15)
                d3=d1+d2
                self.BoughtOn.set(d1)
                self.DeliverDate.set(d3)                 
                self.DeliveryCharge.set("50.00")
                self.FlowerAge.set("No")
                self.FinalAmount.set("310.00")
            else:
                pass
        
        lstBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15,bd=5)
        lstBox.bind("<<ListboxSelect>>",SelectFlower)
        lstBox.grid(row=0,column=0,padx=4)
        ScrollBar1.config(command=lstBox.yview) 

        
        for Flowers in lstFlowers:              
            lstBox.insert(END,Flowers)

        #====================================== Button Frames ==========================================#
        FrameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        FrameButton.place(x=0,y=520,width=1366,height=60)

        btnAddData=Button(FrameButton,command=self.add_data,text="ADD",font=("arial",10,"bold"),width=22,bg="orange",fg="black",relief=RAISED,bd=5)
        btnAddData.grid(row=0,column=0,padx=12)

        btnShowData=Button(FrameButton,command=self.show_data,text="SHOW",font=("arial",10,"bold"),width=22,bg="orange",fg="black",relief=RAISED,bd=5)
        btnShowData.grid(row=0,column=1,padx=12)

        btnUpdateData=Button(FrameButton,command=self.update_data,text="UPDATE",font=("arial",10,"bold"),width=22,bg="orange",fg="black",relief=RAISED,bd=5)
        btnUpdateData.grid(row=0,column=2,padx=12)

        btnDeleteData=Button(FrameButton,command=self.delete_data,text="DELETE",font=("arial",10,"bold"),width=22,bg="orange",fg="black",relief=RAISED,bd=5)
        btnDeleteData.grid(row=0,column=3,padx=12)

        btnResetData=Button(FrameButton,command=self.reset_data,text="RESET",font=("arial",10,"bold"),width=22,bg="orange",fg="black",relief=RAISED,bd=5)
        btnResetData.grid(row=0,column=4,padx=12)

        btnExitData=Button(FrameButton,command=self.iExit,text="EXIT",font=("arial",10,"bold"),width=22,bg="orange",fg="black",relief=RAISED,bd=5)
        btnExitData.grid(row=0,column=5,padx=12)

        #====================================== Information Frames ======================================#
        
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        FrameDetails.place(x=0,y=580,width=1366,height=120)
       
        xScroll=ttk.Scrollbar(FrameDetails,orient=HORIZONTAL)
        yScroll=ttk.Scrollbar(FrameDetails,orient=VERTICAL)

        self.Library_Table=ttk.Treeview(FrameDetails,column=("Member","SR_No","CostumerID","FirstName","LastName","Address","Pincode","Mobile",\
            "FlowerID","FlowerName","Supplier","BoughtOn","DeliverDate","Status","FlowerAge","DeliveryCharge","FinalAmount"),\
                x=xScroll.set,y=yScroll.set)           
        xScroll.pack(side=BOTTOM,fill=X)                
        yScroll.pack(side=RIGHT,fill=Y)                 

        xScroll.config(command=self.Library_Table.xview)    
        yScroll.config(command=self.Library_Table.yview)
        
        self.Library_Table.heading("Member",text="Member Type")    
        self.Library_Table.heading("SR_No",text="SR Number")
        self.Library_Table.heading("CostumerID",text="Costumer id")
        self.Library_Table.heading("FirstName",text="First Name")
        self.Library_Table.heading("LastName",text="Last Name")
        self.Library_Table.heading("Address",text="Address") 
        self.Library_Table.heading("Pincode",text="Pincode")
        self.Library_Table.heading("Mobile",text="Mobile No.")
        self.Library_Table.heading("FlowerID",text="FlowerID")
        self.Library_Table.heading("FlowerName",text="Flower Name")
        self.Library_Table.heading("Supplier",text="Supplier")
        self.Library_Table.heading("BoughtOn",text="Borrowed On")
        self.Library_Table.heading("DeliverDate",text="Due Date")
        self.Library_Table.heading("Status",text="Return Date")
        self.Library_Table.heading("FlowerAge",text="Delay Day(s)")
        self.Library_Table.heading("DeliveryCharge",text="Late Charge")
        self.Library_Table.heading("FinalAmount",text="Final Amount")
        
        self.Library_Table["show"]="headings"
        self.Library_Table.pack(fill=BOTH,expand=1)

        self.Library_Table.column("Member",width=100)                   
        self.Library_Table.column("SR_No",width=100)
        self.Library_Table.column("CostumerID",width=100)
        self.Library_Table.column("FirstName",width=100)
        self.Library_Table.column("LastName",width=100)
        self.Library_Table.column("Address",width=100)
        self.Library_Table.column("Pincode",width=100)
        self.Library_Table.column("Mobile",width=100)
        self.Library_Table.column("FlowerID",width=100)
        self.Library_Table.column("FlowerName",width=100)
        self.Library_Table.column("Supplier",width=100)
        self.Library_Table.column("BoughtOn",width=100)
        self.Library_Table.column("DeliverDate",width=100)
        self.Library_Table.column("Status",width=100)
        self.Library_Table.column("FlowerAge",width=100)
        self.Library_Table.column("DeliveryCharge",width=100)
        self.Library_Table.column("FinalAmount",width=100)

        self.fetch_data()      
        self.Library_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):         
        mydb=sql.connect(host="localhost",user="root",passwd="12345",database="z")
        mycur=mydb.cursor()

        mycur.execute("insert into Flowerdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.Member.get(),
                                                                                                        self.SR_No.get(),
                                                                                                        self.CostumerID.get(),
                                                                                                        self.FirstName.get(),
                                                                                                        self.LastName.get(),
                                                                                                        self.Address.get(),
                                                                                                        self.Pincode.get(),
                                                                                                        self.Mobile.get(),
                                                                                                        self.FlowerID.get(),
                                                                                                        self.FlowerName.get(),
                                                                                                        self.Supplier.get(),
                                                                                                        self.BoughtOn.get(),
                                                                                                        self.DeliverDate.get(),
                                                                                                        self.Status.get(),
                                                                                                        self.FlowerAge.get(),
                                                                                                        self.DeliveryCharge.get(),
                                                                                                        self.FinalAmount.get(),
                                                                                                        ))
        mydb.commit()
        self.fetch_data()
        messagebox.showinfo("Success","Member has been created successfully.")
        mycur.close()

    def update_data(self):         
        mydb=sql.connect(host="localhost",user="root",passwd="12345",database="z")
        mycur=mydb.cursor()
        mycur.execute("update Flowerdetails set Member=%s,CostumerID=%s,FirstName=%s,LastName=%s,Address=%s,Pincode=%s,Mobile=%s,\
            FlowerID=%s,FlowerName=%s,Supplier=%s,BoughtOn=%s,DeliverDate=%s,Status=%s,FlowerAge=%s,\
            DeliveryCharge=%s,FinalAmount=%s where SR_No=%s",(
                                                         self.Member.get(),
                                                         self.CostumerID.get(),
                                                         self.FirstName.get(),
                                                         self.LastName.get(),
                                                         self.Address.get(),
                                                         self.Pincode.get(),
                                                         self.Mobile.get(),
                                                         self.FlowerID.get(),
                                                         self.FlowerName.get(),
                                                         self.Supplier.get(),
                                                         self.BoughtOn.get(),
                                                         self.DeliverDate.get(),
                                                         self.Status.get(),
                                                         self.FlowerAge.get(),
                                                         self.DeliveryCharge.get(),
                                                         self.FinalAmount.get(),
                                                         self.SR_No.get()
                                                         ))
        mydb.commit()
        self.fetch_data()
        self.reset_data()
        mydb.close()
        messagebox.showinfo("Success","Member has been updated successfully.")
    
    def fetch_data(self):           
        mydb=sql.connect(host="localhost",user="root",passwd="12345",database="z")
        mycur=mydb.cursor()
        mycur.execute("select * from Flowerdetails")
        rows=mycur.fetchall()

        if len(rows)!=0:            
            self.Library_Table.delete(*self.Library_Table.get_children())
            for i in rows:
                self.Library_Table.insert("",END,values=i)
            mydb.commit()
        mydb.close()

    def get_cursor(self,event=""):           
        cursor_row=self.Library_Table.focus()
        content=self.Library_Table.item(cursor_row)
        row=content["values"]
        self.Member.set(row[0]),   
        self.SR_No.set(row[1]),
        self.CostumerID.set(row[2]),
        self.FirstName.set(row[3]),
        self.LastName.set(row[4]),
        self.Address.set(row[5]),
        self.Pincode.set(row[6]),
        self.Mobile.set(row[7]),
        self.FlowerID.set(row[8]),
        self.FlowerName.set(row[9]),
        self.Supplier.set(row[10]),
        self.BoughtOn.set(row[11]),
        self.DeliverDate.set(row[12]),
        self.Status.set(row[13]),
        self.FlowerAge.set(row[14]),
        self.DeliveryCharge.set(row[15]),
        self.FinalAmount.set(row[16])
    
    def show_data(self):                
        self.txtBox.insert(END,"Member Type:\t\t"+self.Member.get()+"\n")
        self.txtBox.insert(END,"Sr.no.:\t\t"+self.SR_No.get()+"\n")
        self.txtBox.insert(END,"Costumer ID:\t\t"+self.CostumerID.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.FirstName.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.LastName.get()+"\n")
        self.txtBox.insert(END,"Address:\t\t"+self.Address.get()+"\n")
        self.txtBox.insert(END,"Pincode:\t\t"+self.Pincode.get()+"\n")
        self.txtBox.insert(END,"Mobile No.:\t\t"+self.Mobile.get()+"\n")
        self.txtBox.insert(END,"Flower name:\t\t"+self.FlowerID.get()+"\n")
        self.txtBox.insert(END,"Flower type:\t\t"+self.FlowerName.get()+"\n")
        self.txtBox.insert(END,"Coupen Code:\t\t"+self.Supplier.get()+"\n")
        self.txtBox.insert(END,"Brought on:\t\t"+self.BoughtOn.get()+"\n")
        self.txtBox.insert(END,"Delivery Date:\t\t"+self.DeliverDate.get()+"\n")
        self.txtBox.insert(END,"Status:\t\t"+self.Status.get()+"\n")
        self.txtBox.insert(END,"flowers age:\t\t"+self.FlowerAge.get()+"\n")
        self.txtBox.insert(END,"Delivery charge:\t\t"+self.DeliveryCharge.get()+"\n")
        self.txtBox.insert(END,"Final Amount:\t\t"+self.FinalAmount.get())

    def reset_data(self):              
        self.Member.set(""),    
        self.SR_No.set(""),
        self.CostumerID.set(""),
        self.FirstName.set(""),
        self.LastName.set(""),
        self.Address.set(""),
        self.Pincode.set(""),
        self.Mobile.set(""),
        self.FlowerID.set(""),
        self.FlowerName.set(""),
        self.Supplier.set(""),
        self.BoughtOn.set(""),
        self.DeliverDate.set(""),
        self.Status.set(""),
        self.FlowerAge.set(""),
        self.DeliveryCharge.set(""),
        self.FinalAmount.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete_data(self):
        if self.SR_No.get()=="" or self.CostumerID.get()=="":
            messagebox.showerror("Error!!!","First select the Member.")
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="12345",database="z")
            mycur=mydb.cursor()
            query="delete from Flowerdetails where SR_No=%s"
            value=(self.SR_No.get(),)
            mycur.execute(query,value)

            mydb.commit()
            self.fetch_data()
            self.reset_data()
            mydb.close()

            messagebox.showinfo("Success","Member has been deleted successfully.")


if __name__=="__main__":            
    SplashScreen()
    root=Tk()
    obj=ShopManagementSystem(root)
    
    root.mainloop()
