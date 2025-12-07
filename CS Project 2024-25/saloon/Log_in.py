#LOGIN FORM
from tkinter import*
import tkinter.messagebox                               # for messagebox
import os                                               # for stringvariable 
from tkinter import ttk                                 # for combobox
import random                                           # for reference
import time
import datetime

def main():
    root = Tk()
    app = Window_1(root)


class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('750x550')
        self.master.config(bg = 'tan')
        self.Frame = Frame(self.master, bg = 'tan')
        self.Frame.pack()


        self.Username = StringVar()                             # x = StringVar()  Holds a string; default value is " "
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = 'Login Form', font = ('algerian',55,'underline'), bg = 'tan', fg = 'red')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)
        
        self.Login_Frame_1 = LabelFrame(self.Frame, width = 1350, height = 150, relief = 'ridge', bg = 'mistyrose', bd = 13, text='Login', fg = 'darkblue',
                                        font = ('lucida calligraphy',25,'bold'))
        self.Login_Frame_1.grid(row = 1, column =0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width = 1000, height = 150, relief = 'ridge',bg = 'powderblue', bd = 15, text='Events', fg = 'darkblue',
                                        font = ('lucida calligraphy',25,'bold'))
        self.Login_Frame_2.grid(row = 2, column = 0)


        #===================================================LABEL and ENTRIES=======================================================================
        self.Label_Username = Label(self.Login_Frame_1, text = 'Username', font = ('lucida handwriting',20,'bold'), bg = 'mistyrose', fg = 'black', bd = 20)
        self.Label_Username.grid(row = 0, column = 0)
        self.text_Username = Entry(self.Login_Frame_1, font = ('lucida handwriting',20,'bold'), fg="red",textvariable = self.Username)
        self.text_Username.grid(row = 0, column = 1, padx = 50)
        self.text_Username.focus()
        
        self.Label_Password = Label(self.Login_Frame_1, text = 'Password', font = ('lucida handwriting',20,'bold'), bg = 'mistyrose', fg = 'black', bd = 20)
        self.Label_Password.grid(row = 1, column = 0)
        self.text_Password = Entry(self.Login_Frame_1, font = ('lucida handwriting',20,'bold'), show = '~', fg="green", textvariable = self.Password)
        self.text_Password.grid(row = 1, column = 1) 
        
        
        #=============================================================BUTTONS=======================================================================
        self.btnLogin = Button(self.Login_Frame_2, text = 'Login', fg = 'green', width = 10, font = ('lucida calligraphy',19,'bold'), command = self.Login)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2, text = 'Reset', fg = 'black', width = 10, font = ('lucida calligraphy',19,'bold'), command = self.Reset)
        self.btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2, text = 'Exit', fg = 'red', width = 10, font = ('lucida calligraphy',19,'bold'), command = self.Exit)
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
        filename = 'saloon.py'
        os.system(filename)
        os.system('notepad'+filename)


if __name__ == '__main__':                                    # https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
    main()                                              


