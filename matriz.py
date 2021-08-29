from nodo import punto
from graphviz import Digraph

class matrizD:
    def __init__(self):
        self.head=punto(0,0,'0')

    def agregaNodo(self,nodo):
        x=nodo.getX()
        y=nodo.getY()
        auxX=self.head
        auxY=self.head
     
     #Recorre y crea cabeceras X
        contadorX=0
        while(True):
            if (auxX.getX()<x):
                if (auxX.getSiguiente()==None):
                    nuevo=punto(contadorX+1,0,contadorX+1)
                    auxX.setSiguiente(nuevo)
                    nuevo.setAnterior(auxX)
                    contadorX+=1
                    auxX=auxX.getSiguiente()
                    print('cabeceraX '+str(contadorX)+' Agregada')
                else:
                    auxX=auxX.getSiguiente()
                    contadorX+=1
            if (auxX.getX()==x):
                break
     #recorre nodos de columna
        while(True):
            if (auxX.getY()<y):
                if (auxX.getAbajo()==None):
                    auxX.setAbajo(nodo)
                    nodo.setArriba(auxX)
                    #print('se agrego nodo en X')
                    break
                elif (auxX.getAbajo().getY()<y):
                    auxX=auxX.getAbajo()
                else:
                    nodo.setAbajo(auxX.getAbajo())
                    nodo.setArriba(auxX)
                    auxX.getAbajo().setArriba(nodo)
                    auxX.setAbajo(nodo)
                    print('se agrego nodo en x')
                    break
            else:
                auxX=nodo

     #Recorre cabeceras Y
        contadorY=0
        while(True):
            if (auxY.getY()<y):
                if (auxY.getAbajo()==None):
                    nuevo=punto(0,contadorY+1,contadorY+1)
                    auxY.setAbajo(nuevo)
                    nuevo.setArriba(auxY)
                    contadorY+=1
                    auxY=auxY.getAbajo()
                    #print('cabeceraY '+str(contadorY)+' Agregada')
                else:
                    auxY=auxY.getAbajo()
                    contadorY+=1
            if (auxY.getY()==y):
                break

     #Recorre nodos de fila
        while(True):
            if (auxY.getX()<x):
                if (auxY.getSiguiente()==None):
                    auxY.setSiguiente(nodo)
                    nodo.setAnterior(auxX)
                    #print('nodo Y agregado')
                    break
                elif (auxY.getSiguiente().getX()<x):
                    auxY=auxY.getSiguiente()
                else:
                    nodo.setSiguiente(auxY.getSiguiente())
                    nodo.setAnterior(auxY)
                    auxY.getSiguiente().setAnterior(nodo)
                    auxY.setSiguiente(nodo)
                    break
            else:
                auxY=nodo