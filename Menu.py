from tkinter import *
from Operaciones import *
from expl import*
from explv2 import *
def ExpA():
    p1=Inicio()
    p1.inicio()
def ExpL():
    p2=inicio()
    p2.op()
def ExpLv2():
    p3=inicio2()
    p3.op2()
raiz=Tk()
raiz.title("Ventana")
raiz.geometry("500x500")
Button(raiz,text="Expresion Aritmetica", command=ExpA,font=("Agency FB",9), width=20).place(x=200,y=20)
Button(raiz,text="Expresion Lógica", command=ExpL,font=("Agency FB",9), width=20).place(x=200,y=70)
Button(raiz,text="Expresion Lógica V2", command=inicio2(),font=("Agency FB",9), width=20).place(x=200,y=130)
raiz.mainloop()