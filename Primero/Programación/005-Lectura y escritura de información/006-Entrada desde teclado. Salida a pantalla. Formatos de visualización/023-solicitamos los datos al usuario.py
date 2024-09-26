'''
    Programa CRUD completo
    v0.1 Jose Vicente Carratalá
    El objetivo de este programa es construir el CRUD completo contra MySQL
'''

print("##############")
print("Programa CRUD completo sobre clientes")
print("##############")

while True:
    
    print("Selecciona una opción")
    print("1.-Crear nuevo cliente")
    print("2.-Leer clientes existentes")
    print("3.-Actualizar cliente existente")
    print("4.-Eliminar cliente")
    print("5.-Salir del programa")

    opcion = input("Selecciona una de las opciones:")
    print("Has seleccionado la opcion:",opcion)

    if opcion == "1":
        print("Vamos a insertar un nuevo cliente")
        nombre = input("Introduce un nuevo nombre:")
        apellidos = input("Introduce los nuevos apellidos:")
        email = input("Introduce el email:")
        poblacion = input("Introduce la poblacion:")
        fechadenacimiento = input("Introduce la fecha de nacimiento:")
    elif opcion == "2":
        print("vamos a listar los clientes")
    elif opcion == "3":
        print("Vamos a actualizar a un cliente")
    elif opcion == "4":
        print("Vamos a eliminar a un cliente")
    elif opcion == "5":
        exit()
    else:
        print("Lo que has escogido no es una opción válida")
