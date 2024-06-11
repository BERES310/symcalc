from tkinter import *
from sympy import *

import tkinter.messagebox
import matplotlib.pyplot as plt
import numpy as np
expression = ""

#symbol definition
x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
t = Symbol("t")
s = Symbol("s")

# defining operations
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        # expression = "" 
    except:
        equation.set(" error ")
        equation.set("hubba hubba zoot zoot")
        expression = ""
def solpress():
    try:
        global expression
        total = roots(eval(expression))
        equation.set(total)
        expression = "" 
    except:
        equation.set(" error ")
        equation.set("hubba hubba zoot zoot")
        expression = ""
def solx():
    try:
        global expression
        total = solveset(eval(expression), x)
        equation.set(total)
        expression = "" 
    except:       
        equation.set("hubba hubba zoot zoot")
        expression = ""
def soly():
    try:
        global expression
        total = solveset(eval(expression), y)
        equation.set(total)
        expression = "" 
    except:
        equation.set("hubba hubba zoot zoot")
        expression = ""
def solz():
    try:
        global expression
        total = solveset(eval(expression), z)
        equation.set(total)
        expression = "" 
    except:
        equation.set("hubba hubba zoot zoot")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
def btjestes(num):
    a=" "
    a=a+str(num)
    equation.set(a)
def wykresik():
    try:
        global expression
        b = eval(expression)
        tm=np.arange(-10,10,0.1)
        us=np.zeros(len(tm))

        for i in range(len(tm)):
            us[i] += b.subs(x, tm[i])
            
        plt.figure()
        plt.plot(tm, us)
        plt.title("wykresik")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    except:
        equation.set("hubba hubba zoot zoot")
        expression = " "
def integratesolx():
    try:
        global expression
        f = Function("f")(x)
        f= eval(expression)
        total=f.integrate(x)
        equation.set(total)    
    except:
        equation.set("hubba hubba zoot zoot")
        expression = " "
def integratesoly():
    try:
        global expression
        f = Function("f")(y)  
        f= eval(expression)
        total=f.integrate(y)
        equation.set(total)
    except:
        equation.set("hubba hubba zoot zoot")
        expression = " "
def integratesolz():
    try:
        global expression
        f = Function("f")(z)
        f= eval(expression)
        total=f.integrate(z)
        equation.set(total)
    except:
        equation.set("hubba hubba zoot zoot")
        expression = " "
def diffx():
    try:
        global expression
        f = Function("f")(x)
        f= eval(expression)
        total=f.diff(x)
        equation.set(total)
    except:
        equation.set("hubba hubba zoot zoot")
        expression = " "
def diffy():
    try:
        global expression
        f = Function("f")(y)
        f= eval(expression)
        total=f.diff(y)
        equation.set(total)
    except:
        equation.set("hubba hubba zoot zoot")
        expression = " "
def diffz():
    try:
        global expression
        f = Function("f")(z)
        f= eval(expression)
        total=f.diff(z)
        equation.set(total)
    except:
        equation.set("hubba hubba zoot zoot")
        expression = " "
def expanda():
    try:
        global expression
        a=expand(expression)
        equation.set(a)
    except:
        equation.set("hubba hubba zoot zoot")
        expression = " "
if __name__ == "__main__":
    gui = Tk()
    equation = StringVar()
    gui.configure(background="light blue")
    gui.resizable(width=True, height=True)
    gui.title("Symbolic calc")
 

    gui.geometry("825x700")

    equation = StringVar()
 
   
    #entry 
    txtDisplay = Entry(gui, textvariable=equation, font=('Helvetica',20,'bold'),
                   bg='black',fg='white',
                   bd=40,width=49,justify=RIGHT)
    txtDisplay.grid(row=0,column=0, columnspan=7, pady=1)
    txtDisplay.insert(0,"0")
    
    #buttons 0-10
    button1 = Button(gui, text=' 1 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(1),)
    button1.grid(row=3, column=1, pady = 3)
    button2 = Button(gui, text=' 2 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(2))
    button2.grid(row=3, column=2, pady = 3) 
    button3 = Button(gui, text=' 3 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(3))
    button3.grid(row=3, column=3, pady = 3)

    button4 = Button(gui, text=' 4 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(4))
    button4.grid(row=4, column=1, pady = 3)
 
    button5 = Button(gui, text=' 5 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(5))
    button5.grid(row=4, column=2, pady = 3)
 
    button6 = Button(gui, text=' 6 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(6))
    button6.grid(row=4, column=3, pady = 3)
 
    button7 = Button(gui, text=' 7 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(7))
    button7.grid(row=5, column=1, pady = 3)
 
    button8 = Button(gui, text=' 8 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(8))
    button8.grid(row=5, column=2, pady = 3)
 
    button9 = Button(gui, text=' 9 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(9))
    button9.grid(row=5, column=3, pady = 3)
 
    button0 = Button(gui, text=' 0 ', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                     font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(0))
    button0.grid(row=6, column=2, pady = 3)
 
   
   #buttons = - / * ^
    plus = Button(gui, text=' + ', activebackground="snow", width=6, height=1, fg='black', bg='red', 
                  font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("+"))
    plus.grid(row=2, column=4, pady = 3)
 
    minus = Button(gui, text=' - ', activebackground="snow", width=6, height=1, fg='black', bg='red', 
                   font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("-"))
    minus.grid(row=3, column=4, pady = 3)
 
    multiply = Button(gui, text=' * ', activebackground="snow", width=6, height=1, fg='black', bg='red', 
                      font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("*"))
    multiply.grid(row=4, column=4, pady = 3)
    power = Button(gui, text=' ^ ', activebackground="snow", width=6, height=1, fg='black', bg='red', font=('Helvetica',20,'bold') ,bd=4,
                    command=lambda: press("**"))
    power.grid(row=5, column=4, pady = 3)
 
    divide = Button(gui, text=' / ', activebackground="snow", width=6, height=1, fg='black', bg='red', 
                    font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("/"))
    divide.grid(row=6, column=4, pady = 3)
 
    
    # different buttons
    equal = Button(gui, text=' = ', activebackground="snow", width=6, height=1, fg='black', bg='blue', 
                   font=('Helvetica',20,'bold') ,bd=4, command=equalpress)
    equal.grid(row=1, column=4, pady = 3)
    
    clear = Button(gui, text=" Clear ", activebackground="snow", width=6, height=1, fg='black', bg='red', 
                   font=('Helvetica',20,'bold') ,bd=4, command=clear)
    clear.grid(row=6, column=3, pady = 3)
 
    Decimal= Button(gui, text='.', activebackground="snow", width=6, height=1, fg='black', bg='orange', 
                    font=('Helvetica',20,'bold') , bd=4, command=lambda: press('.'))
    Decimal.grid(row=6, column=1, pady = 3)
    
    roots = Button(gui, text=" roots ", activebackground="snow", width=6, height=1, fg='black', bg='blue', 
                   font=('Helvetica',20,'bold') ,bd=4, command=solpress)
    roots.grid(row=1, column='0', pady = 3)
    
    bracket1 = Button(gui, text=' ( ', activebackground="snow",  width=6, height=1, fg='black', bg='red', 
                      font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("("))
    bracket1.grid(row=2, column=1, pady = 3)
    
    bracket2 = Button(gui, text=' ) ', activebackground="snow", width=6, height=1, fg='black', bg='red', 
                      font=('Helvetica',20,'bold') ,bd=4, command=lambda: press(")"))
    bracket2.grid(row=2, column=2, pady = 3)
    #komplemencik
    jestes=Button(gui,text="komplemencik", activebackground="snow", fg='black', bg='yellow', 
                  font=('Helvetica',20,'bold') ,bd=4,command=lambda:btjestes("jestes piekny"))
    jestes.grid(row=13, columnspan=6, pady = 3)
    
    #symbol buttons
    zmiennax = Button(gui, text=' X ', activebackground="snow", width=6, height=1, fg='black', bg='green', 
                      font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("x"))
    zmiennax.grid(row=2, column=0, pady = 3)
   
    zmiennay =  Button(gui, text=' y ', activebackground="snow", width=6, height=1, fg='black', bg='green', 
                       font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("y"))
    zmiennay.grid(row=3, column=0, pady = 3)
   
    zmiennaz =  Button(gui, text=' z ', activebackground="snow", width=6, height=1, fg='black', bg='green', 
                       font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("z"))
    zmiennaz.grid(row=4, column=0, pady = 3)
   
    zmiennas =  Button(gui, text=' s ', activebackground="snow", width=6, height=1, fg='black', bg='green', 
                       font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("s"))
    zmiennas.grid(row=5, column=0, pady = 3)
    
    zmiennat =  Button(gui, text=' t ', activebackground="snow", width=6, height=1, fg='black', bg='green', 
                       font=('Helvetica',20,'bold') ,bd=4, command=lambda: press("t"))
    zmiennat.grid(row=6, column=0, pady = 3)
    
    # solving 
    eqx = Button(gui, text=" solve \n for x ", activebackground="snow", width=6, height=1, fg='black', bg='blue', 
                 font=('Helvetica',20,'bold') ,bd=4, command=solx)
    eqx.grid(row=1, column='1', pady = 3)
   
    eqy = Button(gui, text=" solve \n for y ", activebackground="snow", width=6, height=1, fg='black', bg='blue', 
                 font=('Helvetica',20,'bold') ,bd=4, command=soly)
    eqy.grid(row=1, column='2', pady = 3)
   
    eqz = Button(gui, text=" solve \n for z ", activebackground="snow", width=6, height=1, fg='black', bg='blue', 
                 font=('Helvetica',20,'bold') ,bd=4,  command=solz)
    eqz.grid(row=1, column='3', pady = 3) 
    
    intx = Button(gui, text=" integrate for x ", activebackground="snow", width=13, height=1, fg='black', bg='blue', 
                  font=('Helvetica',20,'bold') ,bd=4, command=integratesolx)
    intx.grid(row=1, column=5, pady = 3)
    
    inty = Button(gui, text=" integrate for y ", activebackground="snow", width=13, height=1, fg='black', bg='blue', 
                  font=('Helvetica',20,'bold') ,bd=4, command=integratesoly)
    inty.grid(row=2, column=5, pady = 3)
    
    intz = Button(gui, text=" integrate for z ", activebackground="snow", width=13, height=1, fg='black', bg='blue', 
                  font=('Helvetica',20,'bold') ,bd=4, command=integratesolz)
    intz.grid(row=3, column=5, pady = 3)
    
    differx = Button(gui, text=" differentiate for x ", activebackground="snow", width=13, height=1, fg='black', bg='blue', 
                  font=('Helvetica',20,'bold') ,bd=4, command=diffx)
    differx.grid(row=4, column=5, pady = 3)
   
    differy = Button(gui, text=" differentiate for y ", activebackground="snow", width=13, height=1, fg='black', bg='blue', 
                  font=('Helvetica',20,'bold') ,bd=4, command=diffy)
    differy.grid(row=5, column=5, pady = 3)
    
    differz = Button(gui, text=" differentiate for z ", activebackground="snow", width=13, height=1, fg='black', bg='blue', 
                  font=('Helvetica',20,'bold') ,bd=4, command=diffz)
    differz.grid(row=6, column=5, pady = 3)
    
    expa = Button(gui, text=" expand ", activebackground="snow", width=13, height=1, fg='black', bg='blue', 
                  font=('Helvetica',20,'bold') ,bd=4, command=expanda)
    expa.grid(row=7, column=5, pady = 3)
   
    #wykresik
    graph = Button(gui, text=" graph\n f(x) ", activebackground="snow", width=6, height=1, fg='black', bg='blue', 
                   font=('Helvetica',20,'bold') ,bd=4, command=wykresik)
    graph.grid(row=2, column='3', pady = 3)
   
    def Exit():
        if tkinter.messagebox.askyesno("Calculator","How stupid u must be to exit such a wonderfull app???") >0 :
            gui.destroy()
            return
    menubar = Menu(gui)
    gui.config(menu=menubar)
    file_menu = Menu(menubar)
    file_menu.add_command(
    label='Exit',
    command=Exit
    )
    menubar.add_cascade(
    label="Menu",
    menu=file_menu
    )
    gui.mainloop()