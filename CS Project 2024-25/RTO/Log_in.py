#LOGIN FORM
from tkinter import*
import tkinter.messagebox                              
import os                                              
from tkinter import ttk                              
import random                                          
import time
import datetime

def main():
    root = Tk()
    app = Window_1(root)

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('700x550')
        self.master.config(bg = 'black')
        self.Frame = Frame(self.master, bg = 'lightblue')
        self.Frame.pack()

        self.Username = StringVar()                          
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = 'LOGIN FORM', font = ('times new roman',52,'bold'), bg = 'cornsilk', fg = 'navy')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)

        self.Login_Frame_1 = LabelFrame(self.Frame, width = 300, height = 100, relief = 'ridge', bg = 'lightslategrey', bd = 15, text='LOGIN', fg = 'black',
                                        font = ('arial',20,'bold'))
        self.Login_Frame_1.grid(row = 1, column =0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width = 3000, height = 100, relief = 'groove',bg = 'mistyrose4', bd = 15, text='Events', fg = 'black',
                                        font = ('arial',20,'bold'))
        self.Login_Frame_2.grid(row = 2, column = 0)


        #===================================================LABEL and ENTRIES=======================================================================
        self.Label_Username = Label(self.Login_Frame_1, text = 'Username', font = ('arial',20,'bold'), bg = 'lightslategrey', fg = 'light blue', bd = 20)
        self.Label_Username.grid(row = 0, column = 0)
        self.text_Username = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), textvariable = self.Username)
        self.text_Username.grid(row = 0, column = 1, padx = 50)
        self.text_Username.focus()
        
        self.Label_Password = Label(self.Login_Frame_1, text = 'Password', font = ('arial',20,'bold'), bg = 'lightslategrey', fg = 'light blue', bd = 20)
        self.Label_Password.grid(row = 1, column = 0)
        self.text_Password = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), show = '*', textvariable = self.Password)
        self.text_Password.grid(row = 1, column = 1) 
        
        
        #=============================================================BUTTONS=======================================================================
        self.btnLogin = Button(self.Login_Frame_2, text = 'Login', fg = 'navy blue', width = 10, font = ('airia',15,'bold'), command = self.Login)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2, text = 'Reset', fg = 'navy blue', width = 10, font = ('airia',15,'bold'), command = self.Reset)
        self.btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2, text = 'Exit', fg = 'navy blue', width = 10, font = ('airia',15,'bold'), command = self.Exit)
        self.btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)


        #======================================================Code for Login Button==================================================================
    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u == str('root') and p == str(12345)):
            tkinter.messagebox.askyesno("Login Successfully","Thanks : For using Login Form.")
            self.master.destroy()
            self.__RTO__()            
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
            
    def __RTO__(self):
        filename = 'RTO.py'
        os.system(filename)
        os.system('notepad'+filename)


if __name__ == '__main__':                                   
    main()                                              


