#LOGIN FORM
from tkinter import*
import tkinter.messagebox                               # for messagebox
import os                                               # for stringvariable 
from tkinter import ttk                                 # for combobox
import random                                           # for reference
import time
import datetime
#from PIL import Image,ImageTk


def main():
    root = Tk()
    app = Window_1(root)

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1380x700+0+0')
        self.master.config(bg = 'grey')
        self.Frame = Frame(self.master, bg = 'grey')
        self.Frame.pack()
        

        self.Username = StringVar()                             # x = StringVar()  Holds a string; default value is " "
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = 'Login Form', font = ('maiandra GD',55,'bold'), bg = 'grey', fg = 'cyan')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)

        self.Login_Frame_1 = LabelFrame(self.Frame, width = 1350, height = 150, relief = 'ridge', bg = 'grey', bd = 15, text='Login', fg = 'pink',
                                        font = ('maiandra GD',20,'bold'))
        self.Login_Frame_1.grid(row = 1, column =0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width = 1000, height = 150, relief = 'ridge',bg = 'grey', bd = 15, text='Events', fg = 'pink',
                                        font = ('maiandra GD',20,'bold'))
        self.Login_Frame_2.grid(row = 2, column = 0)

        
        


        #===================================================LABEL and ENTRIES=======================================================================
        self.Label_Username = Label(self.Login_Frame_1, text = 'Username', font = ('Lucida Handwriting',20,'bold'), bg = 'grey', fg = 'yellow', bd = 20)
        self.Label_Username.grid(row = 0, column = 0)
        self.text_Username = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), textvariable = self.Username)
        self.text_Username.grid(row = 0, column = 1, padx = 50)
        self.text_Username.focus()
        
        self.Label_Password = Label(self.Login_Frame_1, text = 'Password', font = ('Lucida Handwriting',20,'bold'), bg = 'grey', fg = 'Orange', bd = 20)
        self.Label_Password.grid(row = 1, column = 0)
        self.text_Password = Entry(self.Login_Frame_1, font = ('arial',20,'bold'),fg='blue',bg='white', show = "~", textvariable = self.Password)
        self.text_Password.grid(row = 1, column = 1) 
        
        
        #=============================================================BUTTONS=======================================================================
        self.btnLogin = Button(self.Login_Frame_2, text = 'Login', fg = 'blue',bg='white', width = 10, font = ('airia',15,'bold'),relief=RAISED,bd=7, command = self.Login)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2, text = 'Reset', fg = 'purple',bg='white', width = 10, font = ('airia',15,'bold'),relief=RAISED,bd=7, command = self.Reset)
        self.btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2, text = 'Exit', fg = 'darkblue',bg='white', width = 10, font = ('airia',15,'bold'),relief=RAISED,bd=7, command = self.Exit)
        self.btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)


        #======================================================Code for Login Button==================================================================
    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u == str('root') and p == str(12345)):
            tkinter.messagebox.askyesno("Login Successfully","Thanks : For using Login Form.")
            self.master.destroy()
            self.__library__()            
        else:
            tkinter.messagebox.askyesno("Login","Error : Wrong Password")
            self.Username.set("")
            self.Password.set("")
            self.text_Username.focus()
            

        
        #======================================================Code for Reset Button==================================================================
    def Reset(self):
         self.Username.set("")
         self.Password.set("")
         self.text_Username.focus()


        #======================================================Code for Exit Button==================================================================

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()   
            
    def __library__(self):
        filename = 'FrontPage.py'
        os.system(filename)
        os.system('notepad'+filename)


if __name__ == '__main__':                                    # https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
    main()                                              


