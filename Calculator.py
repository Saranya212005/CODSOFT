import tkinter

def click(value):
    current_value=entry.get()
    new_value=current_value +str(value)
    entry.delete(0,tkinter.END)
    entry.insert(0,new_value)
    
def equal():
    try:
        result=eval(entry.get())
        entry.delete(0,tkinter.END)
        entry.insert(0,str(result))
    except:
        entry.delete(0,tkinter.END)
        entry.insert(0,"ERROR")
    

def clear():
      entry.delete(0,tkinter.END)
    
gui=tkinter.Tk()
gui.config(background="white")
gui.title("Simple Calculator")

entry=tkinter.Entry(gui ,width=20,font=20)
entry.grid(row=0,column=0,columnspan=10)

button1=tkinter.Button(gui, text="1",bg='pink',command=lambda:click(1),height=3,width=7)
button1.grid(row=2,column=1)

button2=tkinter.Button(gui,text="2",bg='pink',command=lambda:click(2),height=3,width=7)
button2.grid(row=2,column=2)

button3=tkinter.Button(gui,text="3",bg='pink',command=lambda:click(3),height=3,width=7)
button3.grid(row=2,column=3)

button4=tkinter.Button(gui,text="4",bg='pink',command=lambda:click(4),height=3,width=7)
button4.grid(row=3,column=1)

button5=tkinter.Button(gui,text="5",bg='pink',command=lambda:click(5),height=3,width=7)
button5.grid(row=3,column=2)

button6=tkinter.Button(gui,text="6",bg='pink',command=lambda:click(6),height=3,width=7)
button6.grid(row=3,column=3)

button7=tkinter.Button(gui,text="7",bg='pink',command=lambda:click(7),height=3,width=7)
button7.grid(row=4,column=1)

button8=tkinter.Button(gui,text="8",bg='pink',command=lambda:click(8),height=3,width=7)
button8.grid(row=4,column=2)

button9=tkinter.Button(gui,text="9",bg='pink',command=lambda:click(9),height=3,width=7)
button9.grid(row=4,column=3)

button0=tkinter.Button(gui,text="0",bg='pink',command=lambda:click(0),height=3,width=7)
button0.grid(row=5,column=2)

plus=tkinter.Button(gui,text="+",bg='pink',command=lambda:click("+"),height=3,width=7)
plus.grid(row=2,column=4)

minus=tkinter.Button(gui,text="-",bg='pink',command=lambda:click("-"),height=3,width=7)
minus.grid(row=3,column=4)

multiply=tkinter.Button(gui,text="*",bg='pink',command=lambda:click("*"),height=3,width=7)
multiply.grid(row=4,column=4)

divide=tkinter.Button(gui,text="/",bg='pink',command=lambda:click("/"),height=3,width=7)
divide.grid(row=5,column=4)

decimal=tkinter.Button(gui,text=".",bg='pink',command=lambda:click("."),height=3,width=7)
decimal.grid(row=5,column=3)

open=tkinter.Button(gui,text="(",bg='pink',command=lambda:click("("),height=3,width=7)
open.grid(row=6,column=3)

close=tkinter.Button(gui,text=")",bg='pink',command=lambda:click(")"),height=3,width=7)
close.grid(row=6,column=4)

close=tkinter.Button(gui,text="%",bg='pink',command=lambda:click("%"),height=3,width=7)
close.grid(row=6,column=1)

clear=tkinter.Button(gui,text="Clear",bg='pink',command=clear,height=3,width=7)
clear.grid(row=6,column=2)

equal=tkinter.Button(gui,text="=",bg='pink',command=equal,height=3,width=7)
equal.grid(row=5,column=1)

gui.mainloop()
