from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import NewRegistration as new_r
import ViewRegistration as view_r
import delete as ded

#---------------------Main Window----------------

window1 = Tk()
window1.title('Welcome')

window1.geometry('1260x630')
window1.config()

#---------------------Importing Images------------------

image1 = ImageTk.PhotoImage(Image.open("bg.png"))#
imagenew_reg = ImageTk.PhotoImage(Image.open("new.png"))
imageview_reg = ImageTk.PhotoImage(Image.open("view.png"))
delimage = ImageTk.PhotoImage(Image.open("delete.png"))
titleimage = ImageTk.PhotoImage(Image.open("hospitalname (2).jpg"))#
iconimage = ImageTk.PhotoImage(Image.open("icon.png"))#
cancelimage = ImageTk.PhotoImage(Image.open("button.png"))#

#----------------------Labels (window1)----------------------------


image1_label = Label(window1, image=image1)
image1_label.place(x=0, y=0)
welcome_label = Label(window1, image=titleimage)
welcome_label.place(x=400, y=20)


#---------------------Label Frame------------------------

labelframe=LabelFrame(window1,bg='white',width=350,height=500,borderwidth=10, relief="groove")
#labelframe.pack(padx=100,pady=100)
labelframe.place(x=480,y=150)
#---------------------Label(labelframe)-----------------

icon_label = Label(labelframe, image=iconimage)
icon_label.place(x=100,y=10)

#----------------------Buttons----------------------------

register = Button(labelframe, text='New Appointment',bd=0,image=imagenew_reg,command=new_r.Newregist) #command=new_r.Newregist, command=view_r.Viewregist, command=window1.destroy
register.place(x=25,y=200)
view = Button(labelframe, text='View Appointment',bd=0,image=imageview_reg,command=view_r.Viewregist)
view.place(x=25, y=270)
delete=Button(labelframe, text='delete Appointment',bd=0,image=delimage,command=ded.Viewregist)
delete.place(x=25, y=340)
close = Button(labelframe, image=cancelimage,bd=0,command=window1.destroy)
close.place(x=100, y=420)


window1.mainloop()




        



