class inicio:
    def op(self):
        p = [True, True, False, False]
        q = [True, False, True, False]

        expr= "[(p->q)^p]->q"
        print("Expresión: "+expr)
        expr2= expr[7:9]
        expr3= expr[2:6]
        expr4=expr[10:13]
        pos=len(expr3)
        pos2=len(expr2)
        pos3=len(expr4)
        resultado=[0,0,0,0]
        resultado2=[0,0,0,0]
        resultadofinal=[0,0,0,0]
        if(expr3[pos-2]==">"):
    
            for x in range(0,len(p)):
                if(p[x]==True and q[x]==False):
                    resultado[x]=False
                else:
                    resultado[x]=True
            print(resultado)

        if(expr2[pos2-2]=="^"):
            for y in range(0,len(resultado)):
                if(resultado[y]==True and p[y]==True):
                    resultado2[y]=True
                else:
                    resultado2[y]=False
            print(resultado2)

        if(expr4[pos3-2]==">"):
            for z in range(0,len(p)):
                if(resultado2[z]==True and q[z]==False):
                    resultadofinal[z]=False
                else:
                    resultadofinal[z]=True
            print(resultadofinal)



    
