from tkinter import *
import math

class calc():
	def __init__(self):
		self.total = 0
		self.current = "" 
		self.input_value = True
		self.check_sum = False
		self.op = ""
		self.result = False

	def numberEnter(self, num):
		self.result = False
		Firstnum = screen.get()
		secondnum = str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value = False
		else:
			if secondnum == '-':
				if secondnum in Firstnum:
					return
			self.current = Firstnum + secondnum
		self.display(self.current)

	def sum_of_total(self):
		self.result = True
		self.current = float(self.current)
		if self.check_sum == True:
			self.valid_function()
		else:
			self.total = float(screen.get())

	def valid_function(self):
		if self.op == "add":
			self.total += self.current
		if self.op == "sub":
			self.total -= self.current
		if self.op == "multi":
			self.total *= self.current
		if self.op == "divide":
			self.total /= self.current
		self.input_value = True
		self.check_sum = False
		self.display(self.total)

	def operation(self, op):
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total = self.current
			self.input_value = True
		self.check_sum = True
		self.op = op
		self.result = False


	def Clear_Entry(self):
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value = True

	def all_Clear_Entry(self):
		self.Clear_Entry()
		self.total = 0
		
	def display(self, value):
		screen.delete(0, END)
		screen.insert(0, value)

	def opPM(self):
		self.result = False
		self.current = -(float(screen.get()))
		self.display(self.current)

	def squared(self):
		self.result = False
		self.current = math.sqrt(float(screen.get()))
		self.display(self.current)
		
added_value = calc()
root = Tk()
root.title("Calculator")
root.geometry("230x231")
root.resizable(0,0)
calc = Frame(root)
calc.grid()


screen = Entry(calc, text="0", bd = 2,justify= "right")
screen.grid(row=0, column=0, columnspan=5, ipadx= 45, padx = 0, ipady= 13)


backspace = Button(calc, text = "←", command= added_value.Clear_Entry, bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
backspace.grid(row= "1", column="0", pady = 3, padx= 3)
CE = Button(calc, text = "ce",command=added_value.Clear_Entry,  bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
CE.grid(row="1", column= "1", pady = 3, padx= 3)
clear = Button(calc,command= added_value.all_Clear_Entry, text = "c", bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
clear.grid(row="1", column="2", pady = 3, padx= 3)
plusminus = Button(calc, text="±", command= added_value.opPM,  bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
plusminus.grid(row="1", column= "3", pady = 3,padx= 3)
sqroot = Button(calc, command= added_value.squared,text= "√",bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
sqroot.grid(row="1", column= "4", pady = 3, padx= 3)






btn7 = Button(calc, text = "7",  bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier", command = lambda: added_value.numberEnter(7))
btn7.grid(row="2", column = "0",pady = 3,padx= 3 )
btn8 = Button(calc, text = "8",bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter(8))
btn8.grid(row="2", column = "1",pady = 3,padx= 3)
btn9 = Button(calc, text = "9",bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter(9))
btn9.grid(row="2", column = "2", pady = 3,padx= 3)
div = Button(calc,command = lambda: added_value.operation("divide"), text = "/",bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",)
div.grid(row="2", column = "3", pady= 3,padx= 3)
percentage = Button(calc, text= "%",bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
percentage.grid(row="2", column= "4", pady= 3,padx= 3)


btn4 = Button(calc, text = "4",bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter(4))
btn4.grid(row="3", column = "0",pady= 3,padx= 3)
btn5 = Button(calc, text = "5",bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter(5))
btn5.grid(row="3", column = "1",pady= 3,padx= 3)
btn6 = Button(calc, text = "6",bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter(6))
btn6.grid(row="3", column = "2",pady= 3,padx= 3)
mult = Button(calc,command = lambda: added_value.operation("multi"), text = "x",bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
mult.grid(row="3", column = "3",pady= 3,padx= 3)
reciprocal = Button(calc, text = "1/x",bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
reciprocal.grid(row="3", column = "4",pady= 3,padx= 3)


btn1 = Button(calc, text = "1",bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter(1))
btn1.grid(row="4", column = "0",pady= 3,padx= 3)
btn2 = Button(calc, text = "2",bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter(2))
btn2.grid(row="4", column = "1",pady= 3,padx= 3)
btn3 = Button(calc, text = "3",bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter(3))
btn3.grid(row="4", column = "2",pady= 3,padx= 3)
minus = Button(calc,command = lambda: added_value.operation("sub"), text = "-",bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
minus.grid(row="4", column = "3",pady= 3,padx= 3)
equals = Button(calc,command = added_value.sum_of_total, text = "=",bg = "#fcfffe", width = 3, height= 3, borderwidth= 1, relief = "ridge", font = "courier")
equals.grid(row="4", column = "4",pady= 3,padx= 3, rowspan = 2)



btn0 = Button(calc, text = "0",bg = "#dae3f7", width = 8, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter(0))
btn0.grid(row=5, column= 0, pady= 3,padx= 4, columnspan= 2)
dot = Button(calc, text = ".",bg = "#dae3f7", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier",command = lambda: added_value.numberEnter("."))
dot.grid(row="5", column = "2",pady= 3,padx= 3)
plus = Button(calc, command = lambda: added_value.operation("add"),text = "+", bg = "#fcfffe", width = 3, height= 1, borderwidth= 1, relief = "ridge", font = "courier")
plus.grid(row="5", column = "3", pady = 4, padx= 3)




root.mainloop()

