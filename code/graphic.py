from main import operators
import tkinter as gui
from tkinter import ttk


class box(gui.Tk):
    
    def __init__(self):
        #op = operators()
        self.time=0
        super().__init__()
        self.title("Calculator")
        self.frame=ttk.Frame(self).grid()
        self.display=ttk.Entry(text='0',font=('Comic Sans MS',20))
        self.display.grid(row=0, columnspan=6)
        
        
        self.buttons()

    def buttons(self):
        #printing numbers
        self.seven=ttk.Button(text="7",command=lambda:self.getdata(7))
        self.seven.grid(row=1,column=0)

        self.eighth=ttk.Button(text="8",command=lambda:self.getdata(8))
        self.eighth.grid(row=1,column=1)

        self.nine=ttk.Button(text="9",command=lambda:self.getdata(9))
        self.nine.grid(row=1,column=2)

        self.four=ttk.Button(text="4",command=lambda:self.getdata(4))
        self.four.grid(row=2,column=0)

        self.five=ttk.Button(text="5",command=lambda:self.getdata(5))
        self.five.grid(row=2,column=1)

        self.six=ttk.Button(text="6",command=lambda:self.getdata(6))
        self.six.grid(row=2,column=2)

        self.one=ttk.Button(text="1",command=lambda:self.getdata(1))
        self.one.grid(row=3,column=0)

        self.two=ttk.Button(text="2",command=lambda:self.getdata(2))
        self.two.grid(row=3,column=1)

        self.three=ttk.Button(text="3",command=lambda:self.getdata(3))
        self.three.grid(row=3,column=2)


    def getdata(self,x):
        if x =='op':
            pass
        self.time=self.time+1
        a=self.display.get()
        if a==' ' or a=='0':
            a=''
        a=str(a)+str(x)
        self.display.delete(0,self.time)
        self.display.insert(0,a)
        print(a)


    def operate(self,y):
        #add code for operators
        self.getdata('op')

    def run(self):
        self.mainloop()
    
app=box()
app.run()