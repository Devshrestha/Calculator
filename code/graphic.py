from actions import operators
import tkinter as gui
from tkinter import ttk
from tkinter.ttk import Style


class box(gui.Tk):
    
    def __init__(self):
        #op = operators()
        self.op=-1
        self.b=''
        self.a=''
        self.first=''
        self.second=''
        self.action=''
        super().__init__()
        self.title("Calculator")
        self.resizable(width=False, height=False)
        self.frame=ttk.Frame(self).grid()
        self.display=ttk.Entry(text='0',font=('Comic Sans MS',25),foreground='#33334d',background='#e6e6e6')
        self.display.grid(row=0, columnspan=8, sticky=gui.W + gui.E)
        self.look_special=Style()
        self.look_operators=Style()
        self.look_numbers=Style()
        self.look_numbers.theme_use('alt')
        self.look_equal=Style()
        #styling buttons
        self.look_special.configure('s.TButton',relief='flat',font=('callbri',13,'bold'),foreground='red', ipading=0,borderwidth=1,background='#ffe6e6', focusthickness=3, focuscolor='none')
        self.look_operators.configure('op.TButton',relief='flat',font=('callbri',13,'bold'),foreground='blue',ipading=0, borderwidth=1,background='#ccffff', focusthickness=3, focuscolor='none')
        self.look_numbers.configure('num.TButton',relief='flat',font=('callbri',13,'bold'),bordercolor='black',ipading=0,foreground='black',background='#e6ffff', borderwidth=1, focusthickness=1, focuscolor='none')
        self.look_equal.configure('eq.TButton',relief='flat',font=('callbri',13,'bold'),foreground='#0000b3',ipading=0, borderwidth=1,background='#99d6ff', focusthickness=3, focuscolor='none')
        ##styling buttons on hover
        self.look_numbers.map('num.TButton',foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', '#00ffff'), ('active', '#80ffff')])
        self.look_operators.map('op.TButton',foreground=[('pressed', 'blue'), ('active', 'blue')],
    background=[('pressed', '!disabled', '#00cccc'), ('active', '#4dffff')])
        self.look_special.map('s.TButton',foreground=[('pressed', 'red'), ('active', 'red')],
    background=[('pressed', '!disabled', '#ff8080'), ('active', '#ffb3b3')])
        self.look_equal.map('eq.TButton',foreground=[('pressed', 'blue'), ('active', 'blue')],
    background=[('pressed', '!disabled', '#33adff'), ('active', '#66c2ff')])
        
        self.buttons()
    
    def buttons(self):
        #printing numbers

        self.clc=ttk.Button(text="C",style='s.TButton',command=lambda:self.clearing())
        self.clc.grid(row=1,column=0,ipady=20,ipadx=8)

        self.div=ttk.Button(text="/",style='op.TButton',command=lambda:self.operate('/'))
        self.div.grid(row=1,column=1,ipady=20,ipadx=8)
        
        self.mul=ttk.Button(text="X",style='op.TButton',command=lambda:self.operate('x'))
        self.mul.grid(row=1,column=2,ipady=20,ipadx=8)

        self.back=ttk.Button(text="<-",style='s.TButton',command=lambda:self.backspace())
        self.back.grid(row=1,column=3,ipady=20,ipadx=8)

        self.seven=ttk.Button(text="7",style='num.TButton',command=lambda:self.getdata(7))
        self.seven.grid(row=2,column=0,ipady=20,ipadx=8)

        self.eighth=ttk.Button(text="8",style='num.TButton',command=lambda:self.getdata(8))
        self.eighth.grid(row=2,column=1,ipady=20,ipadx=8)

        self.nine=ttk.Button(text="9",style='num.TButton',command=lambda:self.getdata(9))
        self.nine.grid(row=2,column=2,ipady=20,ipadx=8)

        self.sub=ttk.Button(text="-",style='op.TButton',command=lambda:self.operate('-'))
        self.sub.grid(row=2,column=3,ipady=20,ipadx=8)

        self.four=ttk.Button(text="4",style='num.TButton',command=lambda:self.getdata(4))
        self.four.grid(row=3,column=0,ipady=20,ipadx=8)

        self.five=ttk.Button(text="5",style='num.TButton',command=lambda:self.getdata(5))
        self.five.grid(row=3,column=1,ipady=20,ipadx=8)

        self.six=ttk.Button(text="6",style='num.TButton',command=lambda:self.getdata(6))
        self.six.grid(row=3,column=2,ipady=20,ipadx=8)

        self.add=ttk.Button(text="+",style='op.TButton',command=lambda:self.operate('+'))
        self.add.grid(row=3,column=3,ipady=20,ipadx=8)

        self.one=ttk.Button(text="1",style='num.TButton',command=lambda:self.getdata(1))
        self.one.grid(row=4,column=0,ipady=20,ipadx=8)

        self.two=ttk.Button(text="2",style='num.TButton',command=lambda:self.getdata(2))
        self.two.grid(row=4,column=1,ipady=20,ipadx=8)

        self.three=ttk.Button(text="3",style='num.TButton',command=lambda:self.getdata(3))
        self.three.grid(row=4,column=2,ipady=20,ipadx=8)

        self.pow=ttk.Button(text="^",style='op.TButton',command=lambda:self.operate('^'))
        self.pow.grid(row=4,column=3,ipady=20,ipadx=8)

        self.equal=ttk.Button(text="=",style='eq.TButton',command=lambda:self.getdata('='))
        self.equal.grid(row=5,column=3,rowspan=2,ipady=50,ipadx=8)

        self.mod=ttk.Button(text="%",style='op.TButton',command=lambda:self.operate('%'))
        self.mod.grid(row=5,column=0,ipady=20,ipadx=8)

        self.zero=ttk.Button(text="0",style='num.TButton',command=lambda:self.getdata(0))
        self.zero.grid(row=5,column=1,ipady=20,ipadx=8)

        self.deci=ttk.Button(text=".",style='num.TButton',command=lambda:self.getdata('.'))
        self.deci.grid(row=5,column=2,ipady=20,ipadx=8)

        self.sine=ttk.Button(text="sin",style='op.TButton',command=lambda:self.trigno('sin'))
        self.sine.grid(row=6,column=0,ipady=20,ipadx=8)

        self.cos=ttk.Button(text="cos",style='op.TButton',command=lambda:self.trigno('cos'))
        self.cos.grid(row=6,column=1,ipady=20,ipadx=8)

        self.tan=ttk.Button(text="tan",style='op.TButton',command=lambda:self.trigno('tan'))
        self.tan.grid(row=6,column=2,ipady=20,ipadx=8)

    def clearing(self):
        self.display.delete(0,gui.END)
        self.first=''
        self.second=''
        self.op=-1
        self.x=''
        
    
    def backspace(self):
        if self.op == -1:
            return
        if self.op == 0:
            self.first=str(self.first)
            self.first=self.first[:-1]
            self.display.delete(0,gui.END)
            check=type(self.first)
            if check==int:
                self.first=int(self.first)
            self.display.insert(0,self.first)

    def calc_trigno(self,x,point):
        x=float(x)
        if self.t_action=='sin':
            self.ans=comp.sine(x)
        if self.t_action=='tan':
            self.ans=comp.tangent(x)
        if self.t_action=='cos':
            self.ans=comp.cosine(x)
        check = type(self.ans)
        if check == int:
          self.ans=int(self.ans)
        if point==-1:  
            self.first=self.ans
            self.second =''
            self.t_action=""
            self.op=3
        if point==0:
            self.second=self.ans
            self.t_action=''
            self.op=2
            self.getdata('=')
            
        self.display.delete(0,gui.END)
        self.display.insert(0,self.ans)

    def calc(self,a,b,p):
        print(a)
        a=float(a)
        b=float(b)
        avi=['+','-',"/",'x','%','^']
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
            if p=='^':
                self.ans=comp.power(a,b)
            
            check = type(self.ans)
            if check == int:
                self.ans=int(self.ans)
            self.first=self.ans
            self.second =''
            self.action=""
            self.op=3
            self.display.delete(0,gui.END)
            self.display.insert(0,self.ans)
    
    def getdata(self,x):
        if self.op == 3 and self.action =='':
            self.first=''
            self.display.delete(0,gui.END)
            self.display.insert(0,self.first)
            self.op=-1


        if self.op==10 and x != '=':
            try:
                self.first+=str(x)
                check=type(self.first)
                if check==int:
                    self.first=int(self.first)
                self.display.delete(0,gui.END)
                self.display.insert(0,str(self.t_action)+' '+str(self.first))
        

            except ValueError:
                print('first error')
                return

        if self.op==12 and x != '=':
            try:
                self.second+=str(x)
                check=type(self.second)
                if check==int:
                    self.second=int(self.second)
                self.display.delete(0,gui.END)
                self.display.insert(0,str(self.first)+str(self.action)+str(self.t_action)+' '+str(self.second))
        

            except ValueError:
                print('first error')
                return

        if x=="=":
            if self.op==-1 or self.op == 0 or self.op == 1:
                return
            if self.op == 2:
                self.calc(self.first,self.second,self.action)
            if self.op==10:
                self.calc_trigno(self.first,-1)
            if self.op==12:
                self.calc_trigno(self.second,0)

        if (self.op==-1 or self.op==0) and x !='=':
 
            try:
                self.first+=str(x)
                check=type(self.first)
                if check==int:
                    self.first=int(self.first)
                self.display.delete(0,gui.END)
                self.display.insert(0,self.first)
                print(self.first)
                if self.first != 0:
                    self.op = 0
            except ValueError:
                print('first error')
                return
        if (self.op==1 or self.op == 2 )and x != '=':
            try:
                self.second+=str(x)
                check=type(self.second)
                if check==int:
                    self.second=int(self.second)

                self.display.delete(0,gui.END)
                self.display.insert(0,str(self.first)+self.action+str(self.second))

                if self.second != 0:
                    self.op = 2
            except ValueError:
                print('second error')
                return

    def operate(self,y):
        if self.op==-1:
            if y=='-' or y =='+':
                self.sign=y
                self.action=''
                self.op=0
        
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
        if self.op==3:
            self.action=y
            self.op=1
            self.display.delete(0,gui.END)
            check=type(self.first)
            if check==int:
                self.first=int(self.first)
            self.display.insert(0,str(self.first)+y)

    def trigno(self,t):
        if self.op == -1:
            self.op=10
            self.t_action=t
            self.display.delete(0,gui.END)
            self.display.insert(0,self.t_action)
        if self.op == 1 :
            self.op=12
            self.t_action=t
            self.display.delete(0,gui.END)
            self.display.insert(0,self.first+self.action+self.t_action)


    def run(self):
        self.mainloop()
    
app=box()
comp=operators()
app.run()