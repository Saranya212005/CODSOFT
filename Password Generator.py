import tkinter
import string
import random

def generator():
    lower_letters=string.ascii_lowercase
    upper_letters= string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    value=lower_letters+upper_letters+digits+symbols
    passwordLength=int(lengthbox.get())
    password=random.sample(value,passwordLength)
    passwordfield.insert(0,password)

def Clear():
    passwordfield.delete(0,tkinter.END)
    
gui=tkinter.Tk()
gui.config(bg='black')

passwordLabel=tkinter.Label(gui,text='Password Generator',font=("Times New Roman",20))
passwordLabel.grid(pady=15)

LengthLabel=tkinter.Label(gui,text='Length Of Password',font=13)
LengthLabel.grid(pady=5)

lengthbox=tkinter.Entry(gui,width=5,bd=2)
lengthbox.grid(pady=5)

generatebutton=tkinter.Button(gui,text="Generate",font=13,command=generator)
generatebutton.grid(pady=5)

passwordfield=tkinter.Entry(gui,width=30,bd=2)
passwordfield.grid(pady=5)

clearbutton=tkinter.Button(gui,text="Clear",font=13,command=Clear)
clearbutton.grid(pady=5)

gui.mainloop()
