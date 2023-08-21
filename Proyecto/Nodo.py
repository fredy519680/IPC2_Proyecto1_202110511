class Nodobase():
    def __init__(self, id, dato):
        self.id = id
        self.dato = dato
        self.siguiente = None

    def getId(self):
        return self.id
    
    def SetId(self, indice):
        self.id = id

    def getDato(self):
        return self.dato
    
    def setDato(self, dato):
        self.dato = dato

    def setSiguiente(self):
        return self.siguiente
    
    def getSiguiente(self, siguiente):
        self.siguiente =siguiente