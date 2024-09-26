'''
    Programa CRUD completo
    v0.1 Jose Vicente Carratalá
    El objetivo de este programa es construir el CRUD completo contra MySQL
'''
import mysql.connector

servidor = "localhost"                          # Creo una variable en la que apunto a mi servidor
usuario = "miempresa"                           # Creo una variable para definir el usuario
contrasena = "miempresa"                        # Creo una variable para definir la contraseña del usuario
base_de_datos = "miempresa"                     # Creo una variable para definiar la base de datos a la que me conecto

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)                                               # Establezco una conexión con la base de datos con los datos seleccionados


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
