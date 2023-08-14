import os
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
        opcm = input("\nIngrese una opción : ")
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
    print("\nCreando Función\n")
    

def ProcesarArchivo():
    print("\nCreando Función\n")

def EscribirArchivo():
    print("\nCreando Función\n")

def DatosEstudiante():
    print("\nCreando Función\n")

def GenerarGrafica():
    print("\nCreando Función\n")

def IniciarSistema():
    print("\nCreando Función\n")
    





menuprincipal()