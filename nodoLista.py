class puntoLista:
    def __init__(self,nombre,terreno):
        self.nombre=nombre
        self.terreno=terreno
        self.siguiente=None

    def setNombre(self,nombre):
        self.nombre=nombre
    
    def setSiguiente(self,nodo):
        self.siguiente=nodo
    
    def setTerreno(self,nodo):
        self.terreno=nodo
    
    def getNombre(self):
        return self.nombre
    
    def getTerreno(self):
        return self.terreno
    
    def getSiguiente(self):
        return self.siguiente