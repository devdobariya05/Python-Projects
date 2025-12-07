from tkinter import *
from tkinter import ttk
import mysql.connector as sql
import time

class SMS:

    def __init__(self,root):
        self.root=root
        self.root.iconbitmap("aa.ico")
        self.root.title("Entry Management System")
        #self.root.maxsize(width=1550,height=1080)
        #self.root.minsize(width=550,height=580)
        self.root.geometry("1550x1080+0+0")

        #=============================== Variable Details ======================================#
        self.Member=StringVar()
        self.FirstName=StringVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        #=============================== Label  ================================================#
        lblTitle=Label(self.root,text="J. B. & KARP Vidya Sankul",bg="sky blue",fg="green",bd=5,relief=RIDGE,\
            font=("times new roman",40,"bold"),padx=2,pady=2)
        lblTitle.pack(side=TOP,fill=X)
        
        #=============================== Frame  ================================================#
        frame=Frame(self.root,bd=5,relief=RIDGE,padx=30,bg="sky blue")
        frame.place(x=0,y=90,width=1550,height=400)        

        #=============================== DataFrame Left ========================================#
        DataFrameLeft=LabelFrame(frame,text="Member Information",bg="powder blue",fg="green",bd=5,relief=RIDGE,font=("times new roman",16,"bold"))
        DataFrameLeft.place(x=0,y=5,width=750,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",13,"bold"),padx=2,pady=3)
        lblMember.grid(row=0,column=0,sticky=W)
        
        cmbMember=ttk.Combobox(DataFrameLeft,textvariable=self.Member,font=("times new roman",13,"bold"),width=15,state="readonly")
        cmbMember["value"]=("Administrator","Teacher","Student")
        cmbMember.current(0)
        cmbMember.grid(row=0,column=1,sticky=W)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblFirstName.grid(row=1,column=0,sticky=W)
        
        txtFirstName=Entry(DataFrameLeft, textvariable=self.FirstName,font=("times new roman",13),width=17)
        txtFirstName.grid(row=1,column=1,sticky=W)

        lblGender = Label(DataFrameLeft,bg="powder blue",text="Gender",font=("times new roman",13,"bold"),padx=2,pady=3)
        lblGender.grid(row=2,column=0,sticky=W)

        rd1 = Radiobutton(DataFrameLeft ,bg="powder blue",text="Male" ,padx = 5,fg="black",bd=0,width=8,font=("arial",10,'bold'),relief = 'raise',variable = self.var1, value = "Male")
        rd1.grid(row=2,column=1,sticky=W)

        rd2 = Radiobutton(DataFrameLeft ,bg="powder blue",text="Female" ,padx = 10,fg="black",bd=0,width=8,font=("arial",10,'bold'),relief = 'raise',variable = self.var1, value = "Female")
        rd2.grid(row=2,column=2,sticky=W)

        lblLanguage=Label(DataFrameLeft,bg="powder blue",text="Language",font=("times new roman",13,"bold"),padx=2,pady=3)
        lblLanguage.grid(row=3,column=0,sticky=W)

        chk1 = Checkbutton(DataFrameLeft ,bg="powder blue",text="English" ,padx = 10,fg="black",bd=0,width=8,font=("arial",10,'bold'),relief = 'raise',variable = self.var2)
        chk1.grid(row=3,column=1,sticky=W)

        chk2 = Checkbutton(DataFrameLeft ,bg="powder blue",text="Hindi" ,padx = 10,fg="black",bd=0,width=8,font=("arial",10,'bold'),relief = 'raise',variable = self.var3)
        chk2.grid(row=3,column=2,sticky=W)

        lblAddress= Label(DataFrameLeft,bg="powder blue",text="Address",font=("times new roman",13,"bold"),padx=2,pady=3) 
        lblAddress.grid(row=4,column=0,sticky=W)
        
        w=Text( DataFrameLeft, bd=0,height=5,width=25,relief=RAISED )
        w.insert(INSERT,"Edit here")
        w.grid(row=4,column=1)
        #=============================== DataFrame Right =======================================#
        DataFrameRight=LabelFrame(frame,text="Member Details",bg="powder blue",fg="green",bd=5,relief=RIDGE,font=("times new roman",16,"bold"))
        DataFrameRight.place(x=755,y=5,width=740, height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=30,height=16,padx=2,pady=4,bd=5)
        self.txtBox.grid(row=0,column=3)
       
        ScrollBar1=Scrollbar(DataFrameRight)
        ScrollBar1.grid(row=0,column=1,stick="NS")
        ScrollBar1.config(command=self.txtBox.yview)
        
        lstMembers=["Administrator","Teacher","Student"]         #Member List created

        lstBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=30,height=15,bd=5)
        lstBox.bind("<<ListboxSelect>>")#,SelectBook)
        lstBox.grid(row=0,column=0,padx=4)
        ScrollBar1.config(command=lstBox.yview)         

        for members in lstMembers:              #To add all books from list to the List Control
            lstBox.insert(END,members)
            
        ScrollBar2=Scrollbar(DataFrameRight)
        ScrollBar2.grid(row=0,column=5,stick="NS")
        ScrollBar2.config(command=self.txtBox.yview)

        #====================================== Button Frames ==================================#
        FrameButton=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=490,width=1550,height=50)

        btnAddData=Button(FrameButton,command=self.add,text="Add FLAT",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=FLAT,bd=5)
        btnAddData.grid(row=0,column=0,padx=12)

        btnShowData=Button(FrameButton,command=self.show,text="Show RAISED",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=RAISED,bd=5)
        btnShowData.grid(row=0,column=1,padx=12)

        btnUpdateData=Button(FrameButton,command=self.update,text="Update SUNKEN",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=SUNKEN,bd=5)
        btnUpdateData.grid(row=0,column=2,padx=12)

        btnDeleteData=Button(FrameButton,command=self.delete,text="Delete GROOVE",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=GROOVE,bd=5)
        btnDeleteData.grid(row=0,column=3,padx=12)

        btnResetData=Button(FrameButton,command=self.reset,text="Reset RIDGE",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=RIDGE,bd=5)
        btnResetData.grid(row=0,column=4,padx=12)

        btnExitData=Button(FrameButton,command=self.exit,text="Exit RIDGE",font=("arial",12,"bold"),width=15,bg="blue",fg="white",relief=RIDGE,bd=5)
        btnExitData.grid(row=0,column=5,padx=12)

        #====================================== Information Frames =============================#
        FrameDetails=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=540,width=1550,height=250)

        xScroll=ttk.Scrollbar(FrameDetails,orient=HORIZONTAL)
        yScroll=ttk.Scrollbar(FrameDetails,orient=VERTICAL)

        self.Table=ttk.Treeview(FrameDetails,column=("Member","FirstName","Gender","Langauge1","Langauge2","Address"),\
                x=xScroll.set,y=yScroll.set)            #Creating table to show the books borrowed information in tabular form
        xScroll.pack(side=BOTTOM,fill=X)                #Adding horizontal scrollbar to the table
        yScroll.pack(side=RIGHT,fill=Y)                 #Adding vertical scrollbar to the table

        xScroll.config(command=self.Table.xview)    #Binding scrollbar to the table
        yScroll.config(command=self.Table.yview)
        
        self.Table.heading("Member",text="Member")     #Creating heading in table for all fields
        self.Table.heading("FirstName",text="FirstName")
        self.Table.heading("Gender",text="Gender")
        self.Table.heading("Langauge1",text="Langauge1")
        self.Table.heading("Langauge2",text="Langauge2") 
        self.Table.heading("Address",text="Address")

        
        self.Table["show"]="headings"
        self.Table.pack(fill=BOTH,expand=1)

        self.Table.column("Member",width=100)                   #Fixing the width of all fields
        self.Table.column("FirstName",width=100)
        self.Table.column("Gender",width=100)
        self.Table.column("Langauge1",width=100)
        self.Table.column("Langauge2",width=100)
        self.Table.column("Address",width=100)

        #self.fetch_data()       #TO show data in the table below.
        #self.Table.bind("<ButtonRelease-1>",self.get_cursor)

        #====================================== Adding Image ===================================#
##        lbl=Label(self.root,bg="black")
##        lbl.place(x=0,y=0, width=1550, height=100)
##        self.ig=PhotoImage(file="mySchool.png")
##        lbl.config(image=self.ig)

    def add(self):
        pass
    def show(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def reset(self):
        pass
    def exit(self):
        pass
    
def connection():
    mydb=sql.connect(host="localhost",user="root",password="12345")#connection to mysql 
    mycur=mydb.cursor()
    mycur.execute("create database if not exists mySMS")
    mycur.execute("use mySMS")
    mycur.execute('Create table if not exists member(Member varchar(30), FirstName varchar(30), \
    Gender varchar(30), Language1 varchar(30), Language2 varchar(30),Address varchar(50))')
    print("Connection successfully")
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

if __name__=="__main__":
    connection()
    SplashScreen()
    root=Tk()
    obj=SMS(root)
    root.mainloop()
