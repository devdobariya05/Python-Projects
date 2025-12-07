from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
#import pymysql
import mysql.connector as sql

# Add your own database name and password here to reflect in the code
db="car"
con = sql.connect(host="localhost",user="root",password='12345',database=db)

def Display():

    root = Tk()
    root.title("Bike")
    root.minsize(width=600,height=500)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#F39308")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Bike 1", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)
    y = 0.25
    
    Label(labelFrame, text="%-10s%-20s%-30s%-30s%-30s%-30s%-20s%-20s%-20s%-20s%-20s%-20s%-30s"%('C-id','f-name','L-Name','mno','g','Id','IdNo','C-Model','C-Name','Colour','C-type','F-type','C-price'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.07,rely=0.2)
    cur = con.cursor()
    getBooks = "select * from bike1"
    try:
        cur.execute(getBooks)
        data=cur.fetchall()
        con.commit()
        for i in data:
            Label(labelFrame, text="%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-10s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='RED', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
