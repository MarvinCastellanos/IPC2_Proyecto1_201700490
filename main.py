from matriz import matrizD
from nodo import punto

tablero=matrizD()

cont=1
while True:
    txt=str(cont)+','+str(cont)
    tablero.agregaNodo(punto(cont,cont,txt))
    cont+=1
    if cont==5:
        break

print('nodos agregados')
tablero.generaGraphviz()