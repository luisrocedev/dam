import mysql.connector

def conector():
    conexion = mysql.connector.connect(
                host='localhost',  
                database='programacion', 
                user='programacion',  
                password='programacion'  
            )
    return True

def dameTablas():
    

    cursor = conexion.cursor(dictionary = True)

    peticion = "SHOW TABLES"
    cursor.execute(peticion)

    registros = cursor.fetchall()

    return registros

def leerTabla():
    conexion = mysql.connector.connect(
                host='localhost',  
                database='programacion', 
                user='programacion',  
                password='programacion'  
            )

    cursor = conexion.cursor(dictionary = True)

    peticion = "SELECT * FROM clientes"
    cursor.execute(peticion)

    registros = cursor.fetchall()

    return registros
conector()
print(dameTablas())
print(leerTabla())
