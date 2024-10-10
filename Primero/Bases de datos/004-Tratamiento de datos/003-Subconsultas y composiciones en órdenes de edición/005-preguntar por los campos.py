import mysql.connector

connection = mysql.connector.connect(
    host='localhost',   
    user='miempresa',   
    password='miempresa',
    database='miempresa' 
)

cursor = connection.cursor(dictionary = True)

while True:
    print("Programa de gestión de clientes")
    print("1.-Insertar un cliente")
    print("2.-Listado de clientes")
    print("3.-...")
    opcion = input("Selecciona una opcion:")
    print("La opción que has escogido es:"+opcion)

    if opcion == "1":
        print("Vamos a insertar un cliente")
        nombre = input("Introduce un nombre:")
        apellidos = input("Introduce apellidos:")
        email = input("Introduce un email:")
        poblacion = input("Introduce una poblacion:")
        fechadenacimiento = input("Introduce una fecha de nacimiento:")
        
    elif opcion == "2":
        print("Vamos a listar los clientes")
