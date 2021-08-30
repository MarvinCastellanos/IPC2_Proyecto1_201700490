from nodoLista import puntoLista

class listaT:
    def __init__(self):
        self.head=None

    def getHead(self):
        return self.head

    def agregaTerreno(self,nodo):
        aux=self.head

        while(True):
            if self.head==None:
                self.head=nodo
                break
            elif aux.getSiguiente()==None:
                aux.setSiguiente(nodo)
                break
            else:
                aux=aux.getSiguiente()
        pass

    def buscaTerreno(self, nombre):
        aux=self.head
        
        while(True):
            if self.head==None:
                print('La lista esta vacia.')
                return 0
            elif aux.getNombre()==nombre:
                return aux.getTerreno()
            elif aux.getSiguiente()==None:
                print('El terreno no se encuentra en la lista.')
                return 0
            else:
                aux=aux.getSiguiente()