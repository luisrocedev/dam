'''
    Programa CRUD completo
    v0.1 Jose Vicente Carratalá
    El objetivo de este programa es construir el CRUD completo contra MySQL
'''
import mysql.connector                          # Importo la librería para poder conectarme a MySQL

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
        
        print("Vamos a insertar un nuevo cliente")                          # Aviso al usuario de la operación que voy a realizar            
        nombre = input("Introduce un nuevo nombre:")                        # Le pido el nombre y lo meto en una variable
        apellidos = input("Introduce los nuevos apellidos:")                # Le pido los apellidos y los meto en una variable
        email = input("Introduce el email:")                                # Le pido el email y lo meto en una variable
        poblacion = input("Introduce la poblacion:")                        # Le pido la población y la meto en una variable
        fechadenacimiento = input("Introduce la fecha de nacimiento:")      # Le pido la fecha de nacimiento y la meto en una variable
        peticion = "INSERT INTO clientes VALUES (NULL,'"+nombre+"','"+apellidos+"','"+email+"','"+poblacion+"','"+fechadenacimiento+"');" # Preparo una petición de inserción a la base de datos
        cursor = conexion.cursor()                                          # Una petición en Python requiere un cursor
        cursor.execute(peticion)                                            # En el cursor, ejecuto la petición que he dejado preparada arriba
        conexion.commit()                                                   # Por último, proceso la petición en el servidor

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
