import re
from Pila import *
class Operacion:
    
    def prioridad(self,operador):
        if(operador=='+' or operador=='-'):
            return 1
        elif(operador=='*' or operador=='/'):
            return 2
        elif(operador=='^'):
            return 3
        elif(operador==')'):
            return 4
        return -1
    
    def separar(self,expr):
        numero=re.compile('[0-9]')
        pila=Pilas()
        pilaO=Pilas()
        for x in range(0,len(expr)):
            buscar=numero.search(expr[x])
            if(buscar!= None):
                pila.push(expr[x])    
            elif(buscar==None):
                prioridad=r.prioridad(expr[x])
                if(pilaO.isEmpty()==0):
                    if(prioridad==-1):
                        pilaO.push(expr[x])
                        pilaO.pop()
                    else:
                        pilaO.push(expr[x])
                else:
                    pos=pilaO.tam()
                    prioridad2=r.prioridad(pilaO.consultar1(pos-1))
                    if(prioridad==prioridad2):
                        pila.push(pilaO.pop())
                        pilaO.push(expr[x])
                    elif(prioridad>prioridad2):
                        if(prioridad==4):
                            while(pilaO.isEmpty() !=0):
                                pila.push(pilaO.pop())
                        else:
                            pilaO.push(expr[x])
                    elif(prioridad<prioridad2):
                        while(pilaO.isEmpty() !=0):
                                pila.push(pilaO.pop())
                        pilaO.push(expr[x])
                
        if(pilaO.tam()==1):
            pila.push(pilaO.pop())
            pila.consultar()
        else:
            pila.consultar()
        
r=Operacion()
class Inicio:
    
    def inicio(self):

        expresion="( 6 + 2 ) * 3 / 2 ^ 2 - 4"
        print("Expersion: "+expresion)
        expr=expresion.split(' ')
    
        r.separar(expr)




