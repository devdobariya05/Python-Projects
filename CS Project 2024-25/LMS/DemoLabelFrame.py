from tkinter import *

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap("aa.ico")
        self.root.title("Library Management System")
        #self.root.maxsize(width=1550,height=1080)
        #self.root.minsize(width=550,height=580)
        self.root.geometry("1550x1080+0+0")

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
