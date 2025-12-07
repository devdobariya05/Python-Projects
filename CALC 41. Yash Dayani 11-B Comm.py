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

		equation.set(" Error ") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("0")

def msg(): 
	global expression 
	expression = "" 
	equation.set("                          CREATED BY:- YASH DAYANI")

def exitProgram():
        exit()

# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="grey") 

	# set the title of GUI window 
	gui.title("Yash Dayani")

	# set the configuration of GUI window 
	gui.geometry("312x324")
	gui.resizable(0, 0)

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression .
	expression_field = Entry(gui, textvariable=equation)

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expression_field.grid(columnspan=4, ipadx=93, column=0, ipady=15, pady=2)

	equation.set('Enter Your Value') 

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button1 = Button(gui, text=' 1 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(1), height=3, width=10) 
	button1.grid(row=2, column=0, padx = 1, pady = 1) 

	button2 = Button(gui, text=' 2 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(2), height=3, width=10) 
	button2.grid(row=2, column=1, padx = 1, pady = 1) 

	button3 = Button(gui, text=' 3 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(3), height=3, width=10) 
	button3.grid(row=2, column=2, padx = 1, pady = 1) 

	button4 = Button(gui, text=' 4 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(4), height=3, width=10) 
	button4.grid(row=3, column=0, padx = 1, pady = 1) 

	button5 = Button(gui, text=' 5 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(5), height=3, width=10) 
	button5.grid(row=3, column=1, padx = 1, pady = 1) 

	button6 = Button(gui, text=' 6 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(6), height=3, width=10) 
	button6.grid(row=3, column=2, padx = 1, pady = 1) 

	button7 = Button(gui, text=' 7 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(7), height=3, width=10) 
	button7.grid(row=4, column=0, padx = 1, pady = 1) 

	button8 = Button(gui, text=' 8 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(8), height=3, width=10) 
	button8.grid(row=4, column=1, padx = 1, pady = 1) 

	button9 = Button(gui, text=' 9 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(9), height=3, width=10) 
	button9.grid(row=4, column=2, padx = 1, pady = 1) 

	button0 = Button(gui, text=' 0 ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(0), height=3, width=10) 
	button0.grid(row=5, column=1, padx = 1, pady = 1)

	pie = Button(gui, text=' π ', fg='black', bd = 0, bg = "#fff", 
					command=lambda: press(3.1415926535897932384626433832795), height=3, width=10) 
	pie.grid(row=5, column=0, padx = 1, pady = 1)

	plus = Button(gui, text=' + ', fg='black', bd = 0, bg = "#eee", 
				command=lambda: press("+"), height=3, width=10) 
	plus.grid(row=2, column=3, padx = 1, pady = 1) 

	minus = Button(gui, text=' - ', fg='black', bd = 0, bg = "#eee", 
				command=lambda: press("-"), height=3, width=10) 
	minus.grid(row=3, column=3, padx = 1, pady = 1) 

	multiply = Button(gui, text=' * ', fg='black', bd = 0, bg = "#eee", 
					command=lambda: press("*"), height=3, width=10) 
	multiply.grid(row=4, column=3, padx = 1, pady = 1) 

	divide = Button(gui, text=' / ', fg='black', bd = 0, bg = "#eee", 
					command=lambda: press("/"), height=3, width=10) 
	divide.grid(row=5, column=3, padx = 1, pady = 1) 

	equal = Button(gui, text=' = ', fg='black', bd = 0, bg = "#eee", 
				command=equalpress, height=3, width=10) 
	equal.grid(row=6, column=3, padx = 1, pady = 1) 

	clear = Button(gui, text='CE', fg='black', bd = 0, bg = "#eee", 
				command=clear, height=3, width=10) 
	clear.grid(row=6, column=1, padx = 1, pady = 1)

	point = Button(gui, text='.', fg='black', bd = 0, bg = "#fff", 
				command=lambda: press("."), height=3, width=10) 
	point.grid(row=5, column=2, padx = 1, pady = 1)

	exitProgram = Button(gui, text='OFF', fg='black', bd = 0, bg = "#eee", 
				command=exitProgram, height=3, width=10) 
	exitProgram.grid(row=6, column=2, padx = 1, pady = 1)

	popupmsg = Button(gui, text='INFO', fg='black', bd = 0, bg = "#eee", 
				command=msg, height=3, width=10) 
	popupmsg.grid(row=6, column=0, padx = 1, pady = 1)




	# start the GUI 
	gui.mainloop()
