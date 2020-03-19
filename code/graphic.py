from main import operators
import tkinter as gui
from tkinter import ttk


class box(gui.Tk):
    
    def __init__(self):
        #op = operators()
        self.time=0
        self.op=-1
        super().__init__()
        self.title("Calculator")
        self.frame=ttk.Frame(self).grid()
        self.display=ttk.Entry(text='0',font=('Comic Sans MS',20))
        self.display.grid(row=0, columnspan=6)
        
        
        self.buttons()

    def buttons(self):
        #printing numbers

        self.clc=ttk.Button(text="C",command=lambda:self.getdata(7))
        self.clc.grid(row=1,column=0)

        self.div=ttk.Button(text="/",command=lambda:self.operate('div'))
        self.div.grid(row=1,column=1)
        
        self.mul=ttk.Button(text="X",command=lambda:self.operate('mul'))
        self.mul.grid(row=1,column=2)

        self.back=ttk.Button(text="<-",command=lambda:self.getdata(7))
        self.back.grid(row=1,column=3)

        self.seven=ttk.Button(text="7",command=lambda:self.getdata(7))
        self.seven.grid(row=2,column=0)

        self.eighth=ttk.Button(text="8",command=lambda:self.getdata(8))
        self.eighth.grid(row=2,column=1)

        self.nine=ttk.Button(text="9",command=lambda:self.getdata(9))
        self.nine.grid(row=2,column=2)

        self.sub=ttk.Button(text="-",command=lambda:self.operate('sub'))
        self.sub.grid(row=2,column=3)

        self.four=ttk.Button(text="4",command=lambda:self.getdata(4))
        self.four.grid(row=3,column=0)

        self.five=ttk.Button(text="5",command=lambda:self.getdata(5))
        self.five.grid(row=3,column=1)

        self.six=ttk.Button(text="6",command=lambda:self.getdata(6))
        self.six.grid(row=3,column=2)

        self.add=ttk.Button(text="+",command=lambda:self.operate('add'))
        self.add.grid(row=3,column=3)

        self.one=ttk.Button(text="1",command=lambda:self.getdata(1))
        self.one.grid(row=4,column=0)

        self.two=ttk.Button(text="2",command=lambda:self.getdata(2))
        self.two.grid(row=4,column=1)

        self.three=ttk.Button(text="3",command=lambda:self.getdata(3))
        self.three.grid(row=4,column=2)

        self.equal=ttk.Button(text="=",command=lambda:self.getdata(3))
        self.equal.grid(row=4,column=3,rowspan=2,ipady=15)

        self.mod=ttk.Button(text="%",command=lambda:self.operate('mod'))
        self.mod.grid(row=5,column=0)

        self.zero=ttk.Button(text="0",command=lambda:self.getdata(0))
        self.zero.grid(row=5,column=1)

        self.deci=ttk.Button(text=".",command=lambda:self.getdata('.'))
        self.deci.grid(row=5,column=2)


    def getdata(self,x):
        if x =='op':
            pass


        self.time=self.time+1
        first=self.display.get()
        if first==' ' or first=='0':
            first=''
        first=str(first)+str(x)
        self.display.delete(0,self.time)
        self.display.insert(0,first)



    def operate(self,y):
        #add code for operators
        self.getdata(y)

    def run(self):
        self.mainloop()
    
app=box()
app.run()