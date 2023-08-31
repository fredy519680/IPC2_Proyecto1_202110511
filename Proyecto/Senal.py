from ListaSimple import ListaSimple
from Tiempo import Tiempo

class Senal:
    def __init__(self, nombre, timepoMaximo,amplitudMaxima):
        self.nombre = nombre
        self.tiempoMaximo = timepoMaximo
        self.amplitudMaxima = amplitudMaxima
        self.tiempos = ListaSimple()
        self.crearListaTiempo()
        self.imprimir()
        

    def getNombre(self):
        return self.nombre
    
    def getTiempoMaximo(self):
        return self.tiempoMaximo
    
    def getAmplituMaxima(self):
        return self.amplitudMaxima
    
    def crearListaTiempo(self):
        for i in range(1, int(self.tiempoMaximo)+1):
            objTiempo =  Tiempo(1, self.amplitudMaxima)
            self.tiempos.agregarFinal(objTiempo)

    def imprimir(self):
        print("____Tiempos para senal:", self.getNombre(),"______")
        tmpTiempo = self.tiempos.getInicio()
        while tmpTiempo != None:
            print(tmpTiempo.getDato().getTiempo())
            tmpTiempo = tmpTiempo.getSiguiente()
