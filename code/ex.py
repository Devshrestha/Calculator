import tkinter as gui
from tkinter import ttk

prev=[]
root = gui.Tk()
root.title("Calculator")
frame=ttk.Frame(root).grid()

for row in range(4):
	root.columnconfigure(row,pad=3)

for column in range(5):
	root.rowconfigure(column,pad=3)


display=ttk.Entry(text='0',font=('Comic Sans MS',20))
display.grid(row=0, columnspan=6)

seven=ttk.Button(text="7",command=lambda:getdata(7))
seven.grid(row=1,column=0)

eighth=ttk.Button(text="8",command=lambda:getdata(8))
eighth.grid(row=1,column=1)

nine=ttk.Button(text="9",command=lambda:getdata(9))
nine.grid(row=1,column=2)

four=ttk.Button(text="4",command=lambda:getdata(4))
four.grid(row=2,column=0)

five=ttk.Button(text="5",command=lambda:getdata(5))
five.grid(row=2,column=1)

six=ttk.Button(text="6",command=lambda:getdata(6))
six.grid(row=2,column=2)

one=ttk.Button(text="1",command=lambda:getdata(1))
one.grid(row=3,column=0)

two=ttk.Button(text="2",command=lambda:getdata(2))
two.grid(row=3,column=1)

three=ttk.Button(text="3",command=lambda:getdata(3))
three.grid(row=3,column=2)

def getdata(x):
    
    display.

root.mainloop()