from tkinter import *
from tkinter import ttk

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap("aa.ico")
        self.root.title("Library Management System")
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
        lblTitle=Label(self.root,text="J. B. & KARP Library Management System",bg="sky blue",fg="green",bd=5,relief=RIDGE,\
            font=("times new roman",40,"bold"),padx=2,pady=2)
        lblTitle.pack(side=TOP,fill=X)
        
        #=============================== Frame  ================================================#
        frame=Frame(self.root,bd=5,relief=RIDGE,padx=30,bg="sky blue")
        frame.place(x=0,y=90,width=1550,height=400)        

        #=============================== DataFrame Left ========================================#
        DataFrameLeft=LabelFrame(frame,text="J. B. & KARP Library Membership Info",bg="powder blue",fg="green",bd=5,relief=RIDGE,font=("times new roman",16,"bold"))
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
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=5,relief=RIDGE,font=("times new roman",16,"bold"))
        DataFrameRight.place(x=755,y=5,width=740, height=350)

        #====================================== Button Frames ==================================#
        FrameButton=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=490,width=1550,height=50)

        #====================================== Information Frames =============================#
        FrameDetails=Frame(self.root,bd=5,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=540,width=1550,height=250)

        #====================================== Adding Image ===================================#
##        lbl=Label(self.root,bg="black")
##        lbl.place(x=0,y=0, width=1550, height=100)
##        self.ig=PhotoImage(file="mySchool.png")
##        lbl.config(image=self.ig)


if __name__=="__main__":            
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
