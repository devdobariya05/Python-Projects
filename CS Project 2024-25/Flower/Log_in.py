
from tkinter import*
import tkinter.messagebox                               
import os                                               
from tkinter import ttk                             
import random                                           
import time
import datetime
from PIL import Image,ImageTk



def main():
    root = Tk()
    app = Window_1(root)

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('3840x2140+0+0')
        


        self.bg_frame = Image.open('unnamed.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.master, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        
        self.Frame = Frame(self.master,bd=7, bg='black', width=750, height=550)
        self.Frame.place(x=270, y=200)

        self.Username = StringVar()                             
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = 'Login Form', font = ('maiandra GD',55,'bold'), bd=7,bg = 'black', fg = 'Blue')
        self.Lbl_Title.place(x=110,y=90)

        self.Login_Frame_1 = LabelFrame(self.Frame,bd=7, width = 1350, height = 150, relief = 'ridge', bg = 'black',  text='Login',
                                        fg = 'white', font = ('maiandra GD',20,'bold'))

        self.Login_Frame_1.place(x=110,y=200)
        self.Login_Frame_2 = LabelFrame(self.Frame,bd=7, width = 1000, height = 150, relief = 'ridge',bg = 'black',  text='Events',
                                        fg = 'white', font = ('maiandra GD',20,'bold'))
        self.Login_Frame_2.place(x=110,y=350)
        
        

        #===================================================LABEL and ENTRIES=======================================================================
        self.Label_Username = Label(self.Login_Frame_1, text = 'Username', font = ('Lucida Handwriting',20,'bold'),bd=7, bg = 'black', fg = 'navy blue')
        self.Label_Username.grid(row = 0, column = 0)
        self.text_Username = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), textvariable = self.Username)
        self.text_Username.grid(row = 0, column = 1, padx = 50)
        self.text_Username.focus()
        
        self.Label_Password = Label(self.Login_Frame_1, text = 'Password', font = ('Lucida Handwriting',20,'bold'),bd=7,bg = 'black', fg = 'navy blue')
        self.Label_Password.grid(row = 1, column = 0)
        self.text_Password = Entry(self.Login_Frame_1, font = ('arial',20,'bold'),fg='blue',bg='white', show = "*", textvariable = self.Password)
        self.text_Password.grid(row = 1, column = 1) 
        
        
        #=============================================================BUTTONS=======================================================================
        self.btnLogin = Button(self.Login_Frame_2, text = 'Login', fg = 'blue',bg='black', width = 10, font = ('airia',15,'bold'),relief=RAISED, command = self.Login)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2, text = 'Reset', fg = 'purple',bg='black', width = 10, font = ('airia',15,'bold'),relief=RAISED, command = self.Reset)
        self.btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2, text = 'Exit', fg = 'darkblue',bg='black', width = 10, font = ('airia',15,'bold'),relief=RAISED, command = self.Exit)
        self.btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)


        #======================================================Code for Login Button==================================================================
    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u == str('root') and p == str(12345)):

            self.master.destroy()
            
            self.__Garden__()            
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
            
    def __Garden__(self):
        filename = 'Garden.py'
        os.system(filename)
        os.system('notepad'+filename)


if __name__ == '__main__':                                   
    main()                                              


