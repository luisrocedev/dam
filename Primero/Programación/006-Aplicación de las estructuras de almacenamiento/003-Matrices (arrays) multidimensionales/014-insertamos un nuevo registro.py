'''
    Programa agenda con colecciones bidimensionales
    (c) 2024 Jose Vicente Carratalá
'''

print("Programa agenda (c) 2024 Jose Vicente Carratalá")

agenda = []

while(True):
    print("Selecciona una de las siguientes opciones")
    print("1.-Insertar un nuevo registro")
    print("2.-Listar los registros")
    selecciona_opcion = input("Selecciona una de las opciones:")

    print("La opcion que has escogido es:",selecciona_opcion)

    if(selecciona_opcion == "1"):
        print("Vamos a insertar un registro")
        nombre = input("Introduce tu nombre:")
        apellidos = input("Introduce tus apellidos:")
        email = input("Introduce tu email:")
        telefono = input("Introduce tu teléfono:")
        agenda.append([nombre,apellidos,email,telefono])
    elif(selecciona_opcion == "2"):
        print("Vamos a leer registros")
        print(agenda)


    
