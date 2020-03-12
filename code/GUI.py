from main import operators
import tkinter as gui
from tkinter import ttk
index=0
def run():
    gui.mainloop()
        
def getdata(x):
    index+=1
    a=index
    display.insert(a,x)

if __name__ == "__main__":


    op = operators()
    root = gui.Tk()
    root.title("Calculator")
    frame=ttk.Frame(root).grid()
    display=ttk.Entry(font=('Comic Sans MS',20))
    getdata(0)
    display.grid(row=0, columnspan=6)

    #printing numbers
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

    run()


    