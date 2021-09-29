import tkinter as tk
from tkinter.constants import TRUE
from typing import Collection


disVal=0
Val2=0
oprbotton=""


def enter_click(value):
    global disVal, Val2
    if value == "+":
        disVal=disVal+Val2
    if value == "*":
        disVal=disVal*Val2
    if value == "/":
        disVal=disVal/Val2
    if value == "-":
        disVal=disVal-Val2

def number_click(value):
    global disVal, Val2
    disVal=(disVal*10)+value
    str_Val.set(disVal)

def oprator_click(value):
    global disVal, Val2, oprbotton
    if value == "C":
        disVal=0
        Val2=0
    elif value == "CE":
        Val2=0
    elif value == "<□":
        disVal=(disVal-disVal%10)/10
    elif value == "+":
        Val2=disVal
        disVal=0
        oprbotton=value
    elif value == "-":
        Val2=disVal
        disVal=0
        oprbotton=value
    elif value == "*":
        Val2=disVal
        disVal=0
        oprbotton=value
    elif value == "/":
        Val2=disVal
        disVal=0
        oprbotton=value
    elif value == "x^2":
        disVal=disVal*disVal
    elif value == "=":
        enter_click(oprbotton)
    str_Val.set(disVal)

def button_click(value):
    try:
        value=int(value)
        number_click(value)
    except:
        oprator_click(value)


window = tk.Tk()
window.title("계산기")

str_Val=tk.StringVar()
str_Val.set(str(disVal))
dis=tk.Entry(window,textvariable=str_Val,justify="right")
dis.grid(column=0,row=0,columnspan=4,ipadx=80,ipady=30)

buttons=[["%","CE","C","<□"],
         ["1/x","x^2","2_root_X","/"],
         ["7","8","9","*"],
         ["4","5","6","-"],
         ["1","2","3","+"],
         ["+/-","0",".","="]]

for i,items in enumerate(buttons):
    for k,time in enumerate(items):

        try:
            color=int(time)
            color="white"
        except:
            color='gray'

        tk.Button(window,
        text=time,
        width=10,
        height=5,
        bg=color,
        command= lambda cmd=time : button_click(cmd)
        ).grid(column=k, row=i+1)


window.mainloop()