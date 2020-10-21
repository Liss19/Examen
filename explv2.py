import re
class inicio2:
    def op2(self):
        expresion= input("Escribe una cadena: ")
        print(expresion)
        numeros=""
        letras=""
        numero=re.compile('[0-9]')
        letra=re.compile('[a-zA-Z]')
        for x in range(0,len(expresion)):
            buscar=numero.search(expresion[x])
            buscar2=letra.search(expresion[x])
    
            if(buscar != None):
                numeros=numeros+expresion[x]
            if(buscar2 != None):
                letras=letras+expresion[x]

        print("Números: "+numeros)
        print("Letras: "+letras)

p1=inicio2()
p1.op2()