from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector


#iconimage = ImageTk.PhotoImage(Image.open("icon.png"))

mydb = mysql.connector.connect(host='localhost', user='root', password='12345')
cur=mydb.cursor()
cur.execute('create database if not exists project')
cur.execute("use project")


def Newregist():
    new_r = Toplevel()
    new_r.title('Registration Page')
    new_r.geometry('1260x630')
    new_r.config()
    image1 = ImageTk.PhotoImage(Image.open("bg.png"))
    #titleimage = ImageTk.PhotoImage(Image.open("hospitalname (2).jpg"))
    back_button=ImageTk.PhotoImage(Image.open("back.png"))
    submit_button=ImageTk.PhotoImage(Image.open("submit.png"))
    image1_label = Label(new_r,image=image1)     
    #image1_label.image = image1
    image1_label.place(x=0, y=0)
    #new_label = Label(new_r, text='NEW REGISTRATION', fg='white', bg='black', bd=6, relief=RAISED, font=('ariel', 30))
    iconimage = ImageTk.PhotoImage(Image.open("icon.png"))
    #welcome_label = Label(new_r, image=titleimage)
    #welcome_label.place(x=10, y=10)

    labelframe1=LabelFrame(new_r,bg='white',width=500,height=550,borderwidth=5, relief="groove")
    labelframe1.place(x=350,y=60)
    icon_label=Label(labelframe1, image=iconimage).place(x=200,y=20)
    

    #------------------Labels---------------------------
    #icon_label = Label(labelframe1, image=iconimage).place(x=115,y=20)
    new_name = Label(labelframe1, text="First Name", bd=5, bg='white', font=('ariel', 18))
    new_name.place(x=0, y=170)
    new_last = Label(labelframe1, text="Last Name", bd=5, bg='white', font=('ariel', 18))
    new_last.place(x=0, y=220)
    new_age = Label(labelframe1, text="Age", bg='white', bd=5, font=('ariel', 18))
    new_age.place(x=0, y=270)
    new_gender = Label(labelframe1, text="Gender", bg='white', bd=5, font=('ariel', 18))
    new_gender.place(x=0, y=320)
    new_num = Label(labelframe1, text="Phone Number", bg='white', bd=5, font=('ariel', 18))
    new_num.place(x=0, y=370)
    new_app = Label(labelframe1, text="Appointment Time", bg='white', bd=5, font=('ariel', 18))
    new_app.place(x=0, y=420)

    # ------------------Entry---------------------------
    name_e = ttk.Entry(labelframe1, width=20,font=('calibre', 15, 'normal')) #, bd=6
    name_e.place(x=230, y=170)
    last_e = ttk.Entry(labelframe1, width=20,font=('calibre', 15, 'normal'))
    last_e.place(x=230, y=220)
    age_e = ttk.Entry(labelframe1, width=20,font=('calibre', 15, 'normal'))
    age_e.place(x=230, y=270)
    v = StringVar()
    gender_e = ttk.Radiobutton(labelframe1, text='Male', variable=v, value='Male')# relief,font=('ariel', 12)
    gender_e.place(x=230, y=320)
    gender_e = ttk.Radiobutton(labelframe1, text='Female', variable=v, value='Female')
    gender_e.place(x=280, y=320)
    gender_e =ttk.Radiobutton(labelframe1, text='Other', variable=v, value='Other')
    gender_e.place(x=340, y=320)
    num_e = ttk.Entry(labelframe1, width=20,font=('calibre', 15, 'normal'))
    num_e.place(x=230, y=370)
    
    time=IntVar()
    Date_combobox =ttk.Combobox(labelframe1,width=4,textvariable=time,state='readonly')
    Date_combobox['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12')
    Date_combobox.current(0)
    Date_combobox.place(x=230, y=430)

    minutes=IntVar()
    Date_combobox =ttk.Combobox(labelframe1,width=4,textvariable=minutes,state='readonly')
    Date_combobox['values'] = ('5','10','15','20','25','30','35','40','45','50','55','60')
    Date_combobox.current(0)
    Date_combobox.place(x=290, y=430)

    ampm = StringVar()
    Date_combobox =ttk.Combobox(labelframe1,width=4,textvariable=ampm,state='readonly')
    Date_combobox['values'] = ('AM', 'PM')
    Date_combobox.current(0)
    Date_combobox.place(x=350, y=430)

    def insert():
        name = name_e.get()
        last = last_e.get()
        age = age_e.get()
        gender = v.get()
        phone = num_e.get()
        hours = time.get()
        minutex = minutes.get()
        amopm = ampm.get()
        timex = str(hours) + ':' + str(minutex) + str(amopm)
        mydb = mysql.connector.connect(host='localhost', user='root', password='12345',database='project')
        cur = mydb.cursor()
        #cur.execute('create database if not exists project')
        cur.execute(
            'create table if not exists hospital(name varchar(255), last varchar(255), age varchar(255), gender varchar(255), phone varchar(255), appt varchar(255))')
        cur.execute('insert into hospital(name, last, age, gender, phone, appt) values(%s, %s, %s, %s, %s, %s)',
                          (name, last, age, gender, phone, timex))

        mydb.commit()
        messagebox.showinfo(title='Registration Complete', message='Appointment Successfully Placed')
        new_r.destroy()

    #------------------Buttons------------------
    Button(labelframe1, bg='white', image=back_button,bd=0, command=new_r.destroy).place(x=100, y=470)
    Button(labelframe1, bg='white', image=submit_button,bd=0, command=insert).place(x=300, y=470)


    new_r.mainloop()

