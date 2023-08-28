from Nodo import Nodo
from Graph import Graph

class ListaSimple():
    id = 0
    def __init__(self):
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0

    def estaVacia(self):
        return self.nodoInicio == None
    
    def agregarFinal(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self. nodoFinal = nuevo

        else:
            self. nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo

    def imprimir(self):
        yo = self.nodoInicio
        while yo != None:
            print(yo.getDato())
            yo =  yo.getSiguiente()

    def graficar(self):
        graph = Graph()
        tmp = self.nodoInicio
        while tmp != None:
            graph.add(tmp, tmp.getSiguiente())
            tmp = tmp.getSiguiente()
        graph.generar()

    

