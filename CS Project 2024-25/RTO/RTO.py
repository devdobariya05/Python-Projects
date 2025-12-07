import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
import datetime as dt
import time
from subprocess import call


def SplashScreen():
    splashscreen = Tk()
    splashscreen.overrideredirect(1)  
    splashscreen.geometry(
        f"800x400+{(splashscreen.winfo_screenwidth() - 800) // 2}+{(splashscreen.winfo_screenheight() - 400) // 2}")
    splashscreen.configure(bg='blue',bd=10)

    Label(splashscreen, text='RTO MANAGEMENT SYSTEM', font='impact 50', fg='navy', bg='grey',bd=10).pack()
    
    Label(splashscreen, text="Version 1.0", font='timesnewroman 15 ', bg='grey', fg='navy',bd=10).place(x=600, y=70)
    pgbar = ttk.Progressbar(splashscreen, orient='horizontal', length=650, mode='indeterminate')
    Label(splashscreen, text="Directed By: Divya Shukla", font='consolas 10', bg='grey', fg='navy',bd=10).place(x=570, y=340)
    pgbar.place(x=50, y=150)
    pgbar['maximum'] = 100
    
    txt=Label(splashscreen,text='0%',bg='steelblue3',fg='black')
    txt.place(x=750, y=151)
    
    for i in range(101):
        time.sleep(0.020)
        pgbar['value'] = i
        pgbar.update()
        txt['text']=pgbar['value'],'%'
        
    splashscreen.destroy()

    splashscreen.mainloop()

mydb=sql.connect(host="localhost",user="root",password="12345")
mycur=mydb.cursor()
mycur.execute("create database if not exists myRTO")
mycur.execute("use myRTO")
mycur.execute('Create table if not exists details(rto varchar(30), Reg_No varchar(20),  \
FirstName varchar(30), LastName varchar(30),Gender varchar(30), Address varchar(50), \
Pincode varchar(30), Mobile varchar(30), AdharID varchar(30), \
Education varchar(30), dob varchar(30), Category varchar(30), Email varchar(30), Date varchar(30),\
City varchar(30), State varchar(30))')

class RTOManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("RTO Management System")
        self.root.geometry("1550x1080+0+0")     
        #=============================== Variable Details ================================================#
        self.rto=StringVar()
        self.Reg_No=StringVar()
        self.FirstName=StringVar()
        self.LastName=StringVar()
        self.Gender=StringVar()
        self.Address=StringVar()
        self.Pincode=StringVar()
        self.Mobile=StringVar()
        self.AdharID=StringVar()
        self.Education=StringVar() 
        self.dob=StringVar()
        self.Category=StringVar()
        self.Email=StringVar()
        self.Date=StringVar()
        self.City=StringVar()
        self.State=StringVar()

             
        lblTitle=Label(self.root,text=" RTO OFFICE MANAGEMENT SYSTEM",bg="lightyellow",fg="darkblue",bd=5,relief=RIDGE,\
            font=("Arial Rounded MT Bold",40,"bold"),padx=2,pady=2)
        lblTitle.pack(side=TOP,fill=X)

        self.lbb=Label(self.root,bg='lightyellow')
        self.lbb.place(x=8,y=6, width=65, height=65)
        
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
        
        self.lb1_hr = Label(self.root, text='12', font=('Arial Rounded MT Bold', 10, 'bold'), bg='lightyellow', fg='darkblue')
        self.lb1_hr.place(x=1200, y=25, width=40, height=40)
        
        self.lb2_hr = Label(self.root, text=':', font=('Arial Rounded MT Bold', 10, 'bold'), bg='lightyellow', fg='darkblue')
        self.lb2_hr.place(x=1240, y=25, width=20, height=40)
        
        self.lb3_hr = Label(self.root, text='05', font=('Arial Rounded MT Bold', 10, 'bold'), bg='lightyellow', fg='darkblue')
        self.lb3_hr.place(x=1260, y=25, width=40, height=40)
        
        self.lb4_hr = Label(self.root, text=':', font=('Arial Rounded MT Bold', 10, 'bold'), bg='lightyellow', fg='darkblue')
        self.lb4_hr.place(x=1300, y=25, width=20, height=40)
        
        self.lb5_hr = Label(self.root, text='37', font=('Arial Rounded MT Bold', 10, 'bold'), bg='lightyellow', fg='darkblue')
        self.lb5_hr.place(x=1320, y=25, width=40, height=40)
       
        self.lb7_hr = Label(self.root, text='AM', font=('Arial Rounded MT Bold', 10, 'bold'), bg='lightyellow', fg='darkblue')
        self.lb7_hr.place(x=1360, y=25, width=40, height=40)
     
        clock()
    
       
        frame=Frame(self.root,bd=5,relief=RIDGE,padx=30,bg="lightyellow")
        frame.place(x=0,y=90,width=1550,height=800)
        

        #=============================== DataFrame Left ================================================#
        DataFrameLeft=LabelFrame(frame,text="RTO MANAGEMENT SYSTEM",bg="lightyellow",fg="darkblue",bd=5,relief=RIDGE,font=("times new roman",16,"bold"))
        DataFrameLeft.place(x=0,y=300,width=1300,height=300)

        lblrto=Label(DataFrameLeft,bg="lightyellow",text="RTO CODE",font=("Arial Rounded MT Bold",15,"bold"),padx=14,pady=3)
        lblrto.grid(row=0,column=0,sticky=W)
        txtrto=Entry(DataFrameLeft, textvariable=self.rto,font=("Arial Rounded MT Bold",13),width=29)
        txtrto.grid(row=0,column=1,sticky=W)
  

        lblReg_No=Label(DataFrameLeft,bg="lightyellow",text="REGISTRATION No.",font=("Arial Rounded MT Bold",15,"bold"),padx=14,pady=3)
        lblReg_No.grid(row=1,column=0,sticky=W)
        txtReg_No=Entry(DataFrameLeft, textvariable=self.Reg_No,font=("times new roman",13),width=29)
        txtReg_No.grid(row=1,column=1,sticky=W)

    
        
        lblFirstName=Label(DataFrameLeft,bg="lightyellow",text="FIRST NAME",font=("Arial Rounded MT Bold",15,"bold"),padx=14,pady=3)
        lblFirstName.grid(row=2,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft, textvariable=self.FirstName,font=("times new roman",13),width=29)
        txtFirstName.grid(row=2,column=1,sticky=W)

        lblLastName=Label(DataFrameLeft,bg="lightyellow",text="LAST NAME",font=("Arial Rounded MT Bold",15,"bold"),padx=14,pady=3)
        lblLastName.grid(row=3,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft, textvariable=self.LastName,font=("times new roman",13),width=29)
        txtLastName.grid(row=3,column=1,sticky=W)

        lblGender=Label(DataFrameLeft,bg="lightyellow",text="GENDER",font=("Arial Rounded MT Bold",15,"bold"),padx=14,pady=3)
        lblGender.grid(row=4,column=0,sticky=W)
        cmbGender=ttk.Combobox(DataFrameLeft,textvariable=self.Gender,font=("times new roman",13,"bold"),width=20,state="readonly")
        cmbGender["value"]=("MALE","FEMALE","OTHER")
        cmbGender.current(0)
        cmbGender.grid(row=4,column=1,sticky=W)

        lblAddress=Label(DataFrameLeft,bg="lightyellow",text="ADDRESS",font=("Arial Rounded MT Bold",15,"bold"),padx=14,pady=3)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft, textvariable=self.Address,font=("times new roman",13),width=29)
        txtAddress.grid(row=5,column=1,sticky=W)
        
        lblPincode=Label(DataFrameLeft,bg="lightyellow",text="PIN CODE",font=("Arial Rounded MT Bold",15,"bold"),padx=14,pady=3)
        lblPincode.grid(row=6,column=0,sticky=W)
        txtPincode=Entry(DataFrameLeft, textvariable=self.Pincode,font=("times new roman",13),width=29)
        txtPincode.grid(row=6,column=1,sticky=W)\

        lblMobile=Label(DataFrameLeft,bg="lightyellow",text="MOBILE NO",font=("Arial Rounded MT Bold",15,"bold"),padx=14,pady=3)
        lblMobile.grid(row=7,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft, textvariable=self.Mobile,font=("times new roman",13),width=29)
        txtMobile.grid(row=7,column=1,sticky=W)
        
        lblAdharID=Label(DataFrameLeft,bg="lightyellow",text="AADHAR NO.",font=("Arial Rounded MT Bold",15,"bold"),padx=50,pady=3)
        lblAdharID.grid(row=0,column=2,sticky=W)
        txtAdharID=Entry(DataFrameLeft, textvariable=self.AdharID,font=("times new roman",13),width=29)
        txtAdharID.grid(row=0,column=3,sticky=W)

        lblEducation=Label(DataFrameLeft,bg="lightyellow",text="EDUCATION QUALIFICATION",font=("Arial Rounded MT Bold",15,"bold"),padx=50,pady=3)
        lblEducation.grid(row=1,column=2,sticky=W)
        txtEducation=Entry(DataFrameLeft, textvariable=self.Education,font=("times new roman",13),width=29)
        txtEducation.grid(row=1,column=3,sticky=W)
        
        lbldob=Label(DataFrameLeft,bg="lightyellow",text="DATE OF BIRTH",font=("Arial Rounded MT Bold",15,"bold"),padx=50,pady=3)
        lbldob.grid(row=2,column=2,sticky=W)
        txtdob=Entry(DataFrameLeft, textvariable=self.dob,font=("times new roman",13),width=29)
        txtdob.grid(row=2,column=3,sticky=W)
        
        lblCategory=Label(DataFrameLeft,bg="lightyellow",text="CATEGORY",font=("Arial Rounded MT Bold",15,"bold"),padx=50,pady=3)
        lblCategory.grid(row=3,column=2,sticky=W)
        txtCategory=Entry(DataFrameLeft, textvariable=self.Category,font=("times new roman",13),width=29)
        txtCategory.grid(row=3,column=3,sticky=W)

        lblEmail=Label(DataFrameLeft,bg="lightyellow",text="EMAIL ID",font=("Arial Rounded MT Bold",15,"bold"),padx=50,pady=3)
        lblEmail.grid(row=4,column=2,sticky=W)
        txtEmail=Entry(DataFrameLeft, textvariable=self.Email,font=("times new roman",13),width=29)
        txtEmail.grid(row=4,column=3,sticky=W)
        
        lblDate=Label(DataFrameLeft,bg="lightyellow",text="DATE",font=("Arial Rounded MT Bold",15,"bold"),padx=50,pady=3)
        lblDate.grid(row=5,column=2,sticky=W)
        txtDate=Entry(DataFrameLeft,textvariable=self.Date,font=("times new roman",13),width=29)
        txtDate.grid(row=5,column=3,sticky=W)

        lblCity=Label(DataFrameLeft,bg="lightyellow",text="CITY",font=("Arial Rounded MT Bold",15,"bold"),padx=50,pady=3)
        lblCity.grid(row=6,column=2,sticky=W)
        txtCity=Entry(DataFrameLeft, textvariable=self.City,font=("times new roman",13),width=29)
        txtCity.grid(row=6,column=3,sticky=W)
        
        lblState=Label(DataFrameLeft,bg="lightyellow",text="STATE",font=("Arial Rounded MT Bold",15,"bold"),padx=50,pady=3)
        lblState.grid(row=7,column=2,sticky=W)
        txtState=Entry(DataFrameLeft, textvariable=self.State,font=("times new roman",13),width=29)
        txtState.grid(row=7,column=3,sticky=W)
        
        # ====================Button Frames ==========================================#
        FrameButton=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="lightyellow")
        FrameButton.place(x=0,y=330,width=1550,height=50)

        btnAddData=Button(FrameButton,command=self.add_data,text="ADD",font=("arial",13,"bold"),width=18,bg="lightyellow",fg="black",relief=GROOVE,bd=5)
        btnAddData.grid(row=0,column=0,padx=12)

        btnShowData=Button(FrameButton,command=self.show_data,text="SHOW",font=("arial",13,"bold"),width=18,bg="lightyellow",fg="black",relief=RAISED,bd=5)
        btnShowData.grid(row=0,column=1,padx=12)

        btnUpdateData=Button(FrameButton,command=self.update_data,text="UPDATE",font=("arial",13,"bold"),width=18,bg="lightyellow",fg="black",relief=GROOVE,bd=5)
        btnUpdateData.grid(row=0,column=2,padx=12)

        btnDeleteData=Button(FrameButton,command=self.delete_data,text="DELETE",font=("arial",13,"bold"),width=18,bg="lightyellow",fg="black",relief=RAISED,bd=5)
        btnDeleteData.grid(row=0,column=3,padx=12)

        btnResetData=Button(FrameButton,command=self.reset_data,text="RESET ",font=("arial",13,"bold"),width=18,bg="lightyellow",fg="black",relief=GROOVE,bd=5)
        btnResetData.grid(row=0,column=4,padx=12)

        btnExitData=Button(FrameButton,command=self.iExit,text="EXIT ",font=("arial",13,"bold"),width=18,bg="lightyellow",fg="black",relief=RAISED,bd=5)
        btnExitData.grid(row=0,column=5,padx=10)

        #====================================== Information Frames ======================================#
        
        FrameDetails=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="lightyellow")
        FrameDetails.place(x=0,y=100,width=1500,height=220)
       
        xScroll=ttk.Scrollbar(FrameDetails,orient=HORIZONTAL)
        yScroll=ttk.Scrollbar(FrameDetails,orient=VERTICAL)

        self.RTO_Table=ttk.Treeview(FrameDetails,column=("rto","Reg_No","FirstName","LastName","Gender","Address","Pincode","Mobile",\
            "AdharID","Education","dob","Category","Email","Date","City","State"),\
                x=xScroll.set,y=yScroll.set)         
        xScroll.pack(side=BOTTOM,fill=X)               
        yScroll.pack(side=RIGHT,fill=Y)                

        xScroll.config(command=self.RTO_Table.xview)   
        yScroll.config(command=self.RTO_Table.yview)
        
        self.RTO_Table.heading("rto",text="CODE")     
        self.RTO_Table.heading("Reg_No",text="Registration No")
        self.RTO_Table.heading("FirstName",text="First Name")
        self.RTO_Table.heading("LastName",text="Last Name")
        self.RTO_Table.heading("Gender",text="Gender")
        self.RTO_Table.heading("Address",text="Address") 
        self.RTO_Table.heading("Pincode",text="Pincode")
        self.RTO_Table.heading("Mobile",text="Mobile No.")
        self.RTO_Table.heading("AdharID",text="Aadhar No")
        self.RTO_Table.heading("Education",text="Education")
        self.RTO_Table.heading("dob",text="dob")
        self.RTO_Table.heading("Category",text="category")
        self.RTO_Table.heading("Email",text="Email")
        self.RTO_Table.heading("Date",text="Date")
        self.RTO_Table.heading("City",text="City")
        self.RTO_Table.heading("State",text="State")
        
        self.RTO_Table["show"]="headings"
        self.RTO_Table.pack(fill=BOTH,expand=1)

        self.RTO_Table.column("rto",width=20)                  
        self.RTO_Table.column("Reg_No",width=20)
        self.RTO_Table.column("FirstName",width=50)
        self.RTO_Table.column("LastName",width=50)
        self.RTO_Table.column("Gender",width=30)
        self.RTO_Table.column("Address",width=50)
        self.RTO_Table.column("Pincode",width=30)
        self.RTO_Table.column("Mobile",width=30)
        self.RTO_Table.column("AdharID",width=30)
        self.RTO_Table.column("Education",width=30)
        self.RTO_Table.column("dob",width=20)
        self.RTO_Table.column("Category",width=30)
        self.RTO_Table.column("Email",width=30)
        self.RTO_Table.column("Date",width=20)
        self.RTO_Table.column("City",width=20)
        self.RTO_Table.column("State",width=20)


        self.fetch_data()     
        self.RTO_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):        
        mydb=sql.connect(host="localhost",user="root",passwd="12345",database="myRTO")
        mycur=mydb.cursor()

        mycur.execute("insert into details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.rto.get(),
                                                                                                        self.Reg_No.get(),
                                                                                                        self.FirstName.get(),
                                                                                                        self.LastName.get(),
                                                                                                        self.Gender.get(),
                                                                                                        self.Address.get(),
                                                                                                        self.Pincode.get(),
                                                                                                        self.Mobile.get(),
                                                                                                        self.AdharID.get(),
                                                                                                        self.Education.get(),
                                                                                                        self.dob.get(),
                                                                                                        self.Category.get(),
                                                                                                        self.Email.get(),
                                                                                                        self.Date.get(),
                                                                                                        self.City.get(),
                                                                                                        self.State.get(),
                                                                                                        ))
        mydb.commit()
        self.fetch_data()
        messagebox.showinfo("Success","created successfully.")
        mycur.close()

    def update_data(self):         
        mydb=sql.connect(host="localhost",user="root",passwd="12345",database="myRTO")
        mycur=mydb.cursor()
        mycur.execute("update details set rto=%s,FirstName=%s,LastName=%s,Gender=%s,Address=%s,Pincode=%s,\
           Mobile=%s,AdharID=%s,Education=%s,dob=%s,Category=%s,Email=%s,Date=%s,City=%s, State=%s where Reg_No=%s;",(
                                                         self.rto.get(),
                                                         self.FirstName.get(),
                                                         self.LastName.get(),
                                                         self.Gender.get(),
                                                         self.Address.get(),
                                                         self.Pincode.get(),
                                                         self.Mobile.get(),
                                                         self.AdharID.get(),
                                                         self.Education.get(),
                                                         self.dob.get(),
                                                         self.Category.get(),
                                                         self.Email.get(),
                                                         self.Date.get(),
                                                         self.City.get(),
                                                         self.State.get(),
                                                         self.Reg_No.get()
                                                         ))
        mydb.commit()
        self.fetch_data()
        self.reset_data()
        mydb.close()
        messagebox.showinfo("Success","updated successfully.")
    
    def fetch_data(self):          
        mydb=sql.connect(host="localhost",user="root",passwd="12345",database="myRTO")
        mycur=mydb.cursor()
        mycur.execute("select * from details")
        rows=mycur.fetchall()

        if len(rows)!=0:            
            self.RTO_Table.delete(*self.RTO_Table.get_children())
            for i in rows:
                self.RTO_Table.insert("",END,values=i)
            mydb.commit()
        mydb.close()

    def get_cursor(self,event=""):          
        cursor_row=self.RTO_Table.focus()
        content=self.RTO_Table.item(cursor_row)
        row=content["values"]
        self.rto.set(row[0]),    
        self.Reg_No.set(row[1]),
        self.FirstName.set(row[2]),
        self.LastName.set(row[3]),
        self.Gender.set(row[4]),
        self.Address.set(row[5]),
        self.Pincode.set(row[6]),
        self.Mobile.set(row[7]),
        self.AdharID.set(row[8]),
        self.Education.set(row[9]),
        self.dob.set(row[10]),
        self.Category.set(row[11]),
        self.Email.set(row[12]),
        self.Date.set(row[13]),
        self.City.set(row[14]),
        self.State.set(row[15]),
    
    def show_data(self):
        self.txtBox.insert(END,"RTO code:\t\t"+self.rto.get()+"\n")
        self.txtBox.insert(END,"Registration No.:\t\t"+self.Reg_No.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.Gender.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.FirstName.get()+"\n")
        self.txtBox.insert(END,"Gender:\t\t"+self.LastName.get()+"\n")
        self.txtBox.insert(END,"Address:\t\t"+self.Address.get()+"\n")
        self.txtBox.insert(END,"Pincode:\t\t"+self.Pincode.get()+"\n")
        self.txtBox.insert(END,"Mobile No.:\t\t"+self.Mobile.get()+"\n")
        self.txtBox.insert(END,"Aadhar No:\t\t"+self.AdharID.get()+"\n")
        self.txtBox.insert(END,"Education Qualification :\t\t"+self.Education.get()+"\n")
        self.txtBox.insert(END,"Date Of Birth:\t\t"+self.dob.get()+"\n")
        self.txtBox.insert(END,"Category:\t\t"+self.Category.get()+"\n")
        self.txtBox.insert(END,"Email:\t\t"+self.Email.get()+"\n")
        self.txtBox.insert(END,"Date:\t\t"+self.Date.get()+"\n")
        self.txtBox.insert(END,"City:\t\t"+self.City.get()+"\n")
        self.txtBox.insert(END,"State:\t\t"+self.State.get()+"\n")

    def reset_data(self):               
        self.rto.set(""),    
        self.Reg_No.set(""),
        self.FirstName.set(""),
        self.LastName.set(""),
        self.Gender.set(""),
        self.Address.set(""),
        self.Pincode.set(""),
        self.Mobile.set(""),
        self.AdharID.set(""),
        self.Education.set(""),
        self.dob.set(""),
        self.Category.set(""),
        self.Email.set(""),
        self.Date.set(""),
        self.City.set(""),
        self.State.set(""),
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("RTO Management System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete_data(self):
        if self.Reg_No.get()=="" or self.rto.get()=="":
            messagebox.showerror("Error!!!","First select the Code.")
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="12345",database="myRTO")
            mycur=mydb.cursor()
            query="delete from details where Reg_No=%s"
            value=(self.Reg_No.get(),)
            mycur.execute(query,value)

            mydb.commit()
            self.fetch_data()
            messagebox.showinfo("Success","deleted successfully.")
            self.reset_data()
            mydb.close()

            


if __name__=="__main__":          
    SplashScreen()
    root=Tk()
    obj=RTOManagementSystem(root)
    root.mainloop()
