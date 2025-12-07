# Python program to create a simple GUI 
# calculator using Tkinter

# import everything from tkinter module 
from tkinter import *

# globally declare the expression variable 
expression = "" 


# Function to update expressiom
# in the text entry box 
def press(num): 
	# point out the global expression variable 
	global expression 

	# concatenation of string 
	expression = expression + str(num) 

	# update the expression by using set method 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 

		global expression 

		# eval function evaluate the expression 
		# andstr function convert the result 
		# into string 
		total = str(eval(expression)) 

		equation.set(total) 

		# initialze the expression variable 
		# by empty string 
		expression = "" 

	# if error is generate then handle 
	# by the except block 
	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="light grey") 

	# set the title of GUI window 
	gui.title("Aryan Gami") 

	# set the configuration of GUI window 
	gui.geometry('365x490')

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression .
	expression_field = Entry(gui, bg='orange',font=('arial',20,'italic bold'),bd='30',justify='right',textvariable=equation)
	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expression_field.grid(row=0,columnspan=4)
	equation.set('EnterYourExpression')
	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button7 = Button(gui, text='7',font=('arial',20,'italic bold'),bg='powder blue',bd=8,padx=16,pady=16, activebackground='green',activeforeground='white',
					command=lambda: press(7), height=0, width=0)
	button7.grid(row=1, column=0) 

	button8 = Button(gui, text='8',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16,activebackground='green', activeforeground='white',
					command=lambda: press(8)) 
	button8.grid(row=1, column=1) 

	button9 = Button(gui,  text='9',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16, activebackground='green',activeforeground='white',
					command=lambda: press(9)) 
	button9.grid(row=1, column=2) 

	button4 = Button(gui,  text='4',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16, activebackground='green',activeforeground='white',
					command=lambda: press(4), height=0, width=0) 
	button4.grid(row=2, column=0) 

	button5 = Button(gui,  text='5',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16, activebackground='green',activeforeground='white',
					command=lambda: press(5), height=0, width=0) 
	button5.grid(row=2, column=1) 

	button6 = Button(gui, text='6',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16, activebackground='green',activeforeground='white',
					command=lambda: press(6), height=0, width=0) 
	button6.grid(row=2, column=2) 

	button1 = Button(gui,  text='1',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16, activebackground='green',activeforeground='white',
					command=lambda: press(1), height=0, width=0) 
	button1.grid(row=3, column=0) 

	button2 = Button(gui, text='2',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16, activebackground='green',activeforeground='white',
					command=lambda: press(2), height=0, width=0) 
	button2.grid(row=3, column=1) 

	button3 = Button(gui,  text='3',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16, activebackground='green',activeforeground='white',
					command=lambda: press(3), height=0, width=0) 
	button3.grid(row=3, column=2) 

	button0 = Button(gui, text='0',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16,  activebackground='green',activeforeground='white',
					command=lambda: press(0), height=0, width=0) 
	button0.grid(row=4, column=0) 

	plus = Button(gui, text='+',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=18,pady=16, activebackground='green',activeforeground='white',
				command=lambda: press("+"), height=0, width=3) 
	plus.grid(row=1, column=3) 

	minus = Button(gui, text='-',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=18,pady=18,activebackground='green',activeforeground='white',
				command=lambda: press("-"), height=0, width=3) 
	minus.grid(row=2, column=3) 

	multiply = Button(gui, text='x',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=18,pady=16,  activebackground='green',activeforeground='white',
					command=lambda: press("*"), height=0, width=3) 
	multiply.grid(row=3, column=3) 

	divide = Button(gui,  text='/',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=18,pady=16, activebackground='green',activeforeground='white',
					command=lambda: press("/"), height=0, width=3) 
	divide.grid(row=4, column=3) 

	equal = Button(gui, text='=',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16, activebackground='green',activeforeground='white',
				command=equalpress, height=0, width=0) 
	equal.grid(row=4, column=2) 

	clear = Button(gui, text='C',font=('arial',20,'italic bold'), bg='powder blue',bd=8,padx=16,pady=16,  activebackground='green',activeforeground='white',
				command=clear, height=0, width=0) 
	clear.grid(row=4, column='1')
	
	# start the GUI 
	gui.mainloop()
