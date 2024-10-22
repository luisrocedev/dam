import os                                                                           # Importamos la librería que nos permite interactuar con el sistema operativo

try:                                                                                # Intento realizar una operacion
    os.makedirs("basededatos")                                                      # Intento crear la carpeta de base de datos
except:                                                                             # en el caso de que no pueda
    print("La carpeta de base de datos ya existe, continuamos...")                  # No des error y solo contina

print("Bienvenidos a Mi Querido Diario v0.2")                                       # imprimo un mensaje de bienvenida
while(True):                                                                        # entro en un bucle infinito
    print("Selecciona una de las siguiente opciones")                               # informo al usuario de que va a tener que elegir una opcion
    print("1.-Introducir un nuevo registro")                                        # Le informo de la opcion 1
    print("2.-Leer registros existentes")                                           # Le informo de la opcion 2 
    opcion = input("Selecciona una de las opciones anteriores:")                    # Atrapo su opción elegida y la meto en una variable
    print("La opción que has seleccionado es:",opcion)                              # Imprimo la variable por pantalla

    if opcion == "1":                                                               # Si es cierto que el usuario ha cogido la opcion 1
        print("Has elegido introducir un nuevo registro")                           # Le informo de que ha cogido la opcion 1
        archivo = open("basededatos/miqueridodiario.txt",'a')                       # Abro la base de datos en modo añadir
        fecha = input("Introduce la fecha:")                                        # Le pido la fecha
        mensaje = input("Introduce el mensaje:")                                    # Le pido el mensaje
        archivo.write(fecha+"|"+mensaje+"\n")                                       # Escribo los datos a la base de datos
        archivo.close()                                                             # Y cierro la base de datos
    elif opcion == "2":                                                             # Si es cierto que el usuario ha cogido la opcion 2
        print("Has elegido leer los registros")                                     # Le informo de la opcion que ha cogido
        archivo = open("basededatos/miqueridodiario.txt",'r')                       # Cargo la base de datos en modo lectura
        lineas = archivo.readlines()                                                # Cargo las lineas del archivo
        for linea in lineas:                                                        # Separo las lineas en lineas independientes
            print(linea)                                                            # Imprimo las lineas una a una
    else:                                                                           # En el caso de que ninguna opcion sea la correcta
        print("La opcion que has elegido no es valida")                             # Le aviso al usuario de que no ha escogido una opcion correcta

