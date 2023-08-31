from ListaSimple import ListaSimple
from Amplitud import Amplitud

class Tiempo:
    def __init__(self, tiempo, amplitud):
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.listaAmplitudes = ListaSimple()

    
    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def LlenarListadoAmplitudes(self):
        for i in range(1, int(self.amplitud)+1):
            tmpAmplitud = Amplitud()
            self.listaAmplitudes.agregarFinal(tmpAmplitud)

    def imprimir(self):
        print("___Amplitudes para tiempo:", self.getTiempo(),"")
        objAmplitud = self.listaAmplitudes.getInicio()
        while objAmplitud != None:
            print(objAmplitud.getDato().getAmplitud())
            objAmplitud = objAmplitud.getSiguiente()