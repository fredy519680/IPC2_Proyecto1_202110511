import os
from Nodo import Nodo
from Graph import Graph
from LecturaXML import LecturaXML

print("hola mundo")

def menuprincipal():
    print("Menu principal: ")
    print("     1. Cargar archivo")
    print("     2. Procesar Archivo")
    print("     3. Escribir archivo de Salida")
    print("     4. Mostrar datos del estudiante")
    print("     5. Generar gráfica")
    print("     6. Iniciar Ssitema")
    print("     7. Salida")

    

    while True:
        opcm = input("\nIngrese una opción estás en el manú: ")
        if opcm.isdigit():
            opcm = int(opcm)
            if opcm == 1:
                CargarArchivo()
                break
            elif opcm == 2:
                ProcesarArchivo()
            elif opcm == 3:
                EscribirArchivo()
            elif opcm == 4:
                DatosEstudiante()
            elif opcm == 5:
                GenerarGrafica()
            elif opcm == 6:
                IniciarSistema()
            elif opcm == 7:
                print("\nGracias por utilizar nuestra aplicación\n")
                exit()
            else:
                print("\nEsa opción no es valida\n")
        else:
            print("\nEsa opción no es valida\n")

def CargarArchivo():
    print("\nHas seleccionado la opción cargar archivo:\n")
    ruta = input("Ingrese la ruta del archivo: ")

    while True:
        nombre, extension = os.path.splitext(ruta)
        if extension == ".xml":
            print("\nArchivo valido\n")
            print("Nombre: " + nombre)
            print("Extension: "+ extension)
            break
            
        else:
            print("\nArchivo Invalido\n")
            ruta = input ("\nIngrese la ruta nuevamente: ")

    Objlectura = LecturaXML(ruta)
    Objlectura.getDatos()

    

def ProcesarArchivo():
    print("\nCreando Función\n")

def EscribirArchivo():
    print("\nCreando Función\n")

def DatosEstudiante():
    print("> Fredy Alexander Esteban Pineda")
    print("> 202110511")
    print("> Introducción a la programación y computación")
    print("> Ingenieria en Ciencias y Sistemas")
    print("> 4to Semestre")

def GenerarGrafica():
    print("\nCreando Función\n")

def IniciarSistema():
    print("\nCreando Función\n")
    





menuprincipal()