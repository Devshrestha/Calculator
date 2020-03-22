from main import operators
import tkinter as gui
from tkinter import ttk


class box(gui.Tk):
    
    def __init__(self):
        #op = operators()
        self.op=-1
        self.b=''
        self.a=''
        super().__init__()
        self.title("Calculator")
        self.frame=ttk.Frame(self).grid()
        self.display=ttk.Entry(text='0',font=('Comic Sans MS',20))
        self.display.grid(row=0, columnspan=6)
        
        
        self.buttons()

    def buttons(self):
        #printing numbers

        self.clc=ttk.Button(text="C",command=lambda:self.clearing())
        self.clc.grid(row=1,column=0)

        self.div=ttk.Button(text="/",command=lambda:self.operate('/'))
        self.div.grid(row=1,column=1)
        
        self.mul=ttk.Button(text="X",command=lambda:self.operate('x'))
        self.mul.grid(row=1,column=2)

        self.back=ttk.Button(text="<-",command=lambda:self.getdata(7))
        self.back.grid(row=1,column=3)

        self.seven=ttk.Button(text="7",command=lambda:self.getdata(7))
        self.seven.grid(row=2,column=0)

        self.eighth=ttk.Button(text="8",command=lambda:self.getdata(8))
        self.eighth.grid(row=2,column=1)

        self.nine=ttk.Button(text="9",command=lambda:self.getdata(9))
        self.nine.grid(row=2,column=2)

        self.sub=ttk.Button(text="-",command=lambda:self.operate('-'))
        self.sub.grid(row=2,column=3)

        self.four=ttk.Button(text="4",command=lambda:self.getdata(4))
        self.four.grid(row=3,column=0)

        self.five=ttk.Button(text="5",command=lambda:self.getdata(5))
        self.five.grid(row=3,column=1)

        self.six=ttk.Button(text="6",command=lambda:self.getdata(6))
        self.six.grid(row=3,column=2)

        self.add=ttk.Button(text="+",command=lambda:self.operate('+'))
        self.add.grid(row=3,column=3)

        self.one=ttk.Button(text="1",command=lambda:self.getdata(1))
        self.one.grid(row=4,column=0)

        self.two=ttk.Button(text="2",command=lambda:self.getdata(2))
        self.two.grid(row=4,column=1)

        self.three=ttk.Button(text="3",command=lambda:self.getdata(3))
        self.three.grid(row=4,column=2)

        self.pow=ttk.Button(text="^",command=lambda:self.operate('^'))
        self.pow.grid(row=4,column=3)

        self.equal=ttk.Button(text="=",command=lambda:self.getdata('='))
        self.equal.grid(row=5,column=3,rowspan=2,ipady=15)

        self.mod=ttk.Button(text="%",command=lambda:self.operate('%'))
        self.mod.grid(row=5,column=0)

        self.zero=ttk.Button(text="0",command=lambda:self.getdata(0))
        self.zero.grid(row=5,column=1)

        self.deci=ttk.Button(text=".",command=lambda:self.getdata('.'))
        self.deci.grid(row=5,column=2)

        self.sine=ttk.Button(text="sin",command=lambda:self.operate('sin'))
        self.sine.grid(row=6,column=0)

        self.cos=ttk.Button(text="cos",command=lambda:self.operate('cos'))
        self.cos.grid(row=6,column=1)

        self.tan=ttk.Button(text="tan",command=lambda:self.operate('tan'))
        self.tan.grid(row=6,column=2)

    def clearing(self):
        self.display.delete(0,gui.END)
        self.first=''
        self.second=''
        self.op=-1

    def calc(self,a,b,p):
        avi=['+','-',"/",'x','%']
        if p in avi:
            if p=='+':
                self.ans=comp.add(a,b)
            if p=='-':
                self.ans=comp.sub(a,b)
            if p=='x':
                self.ans=comp.multi(a,b)
            if p=='/':
                self.ans=comp.div(a,b)
            if p=='%':
                self.ans=comp.mod(a,b)

            
            self.first=self.ans
            self.second =None
            self.action=""
            self.op=3
            self.display.delete(0,gui.END)
            self.display.insert(0,self.ans)
    
    def getdata(self,x):
        if self.op == 3 and self.action =='':
            self.first=None
            self.display.delete(0,gui.END)
            self.display.insert(0,self.first)
            self.op=-1
        if x=="=":
            if self.op==-1 or self.op == 0 or self.op == 1:
                return
            if self.op == 2:
                self.calc(self.first,self.second,self.action)

        if (self.op==-1 or self.op==0) and x !='=':
            self.a+=str(x)
            self.display.delete(0,gui.END)
            check=type(self.a)
            if check==int:
                self.a=int(self.a)
            self.display.insert(0,self.a)
            try:
                self.first=float(self.a)
                check=type(self.first)
                if check==int:
                    self.first=int(self.first)

                if self.first != 0:
                    self.op = 0
            except ValueError:
                return
        if (self.op==1 or self.op == 2 )and x != '=':
            self.b+=str(x)
            self.display.delete(0,gui.END)
            self.display.insert(0,str(self.a)+self.action+str(self.b))
            try:
                self.second=float(self.b)
                check=type(self.second)
                if check==int:
                    self.second=int(self.second)
                if self.second != 0:
                    self.op = 2
            except ValueError:
                return

    def operate(self,y):
        if self.op==0:
            self.action=y
            self.op = 1
            self.display.delete(0,gui.END)
            check=type(self.first)
            if check==int:
                self.first=int(self.first)
            self.display.insert(0,str(self.first)+y)
        if self.op == 2:
            self.getdata('=')
            self.action=y




    def run(self):
        self.mainloop()
    
app=box()
comp=operators()
app.run()