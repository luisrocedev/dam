'''
    Programa agenda con SQLite
    (c) 2024 por Jose Vicente Carratalá
    v0.1 Empezando en clase
'''
import sqlite3

conexion = sqlite3.connect('empresa.db') 

conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()

print("############################")
print("      Programa agenda       ")
print(" por Jose Vicente Carratalá ")
print("############################")

while True:
    
    print("Menú principal")
    print("1.-Crear un nuevo registro")
    print("2.-Listado de registros")
    print("3.-Actualización de registros")
    print("4.-Eliminación de registros")

    opcion = input("Selecciona una opcion:")

    if opcion == "1":
        
        print("Vamos a insertar un registro")
        
        nombre = input("Introduce un nuevo nombre:")
        apellidos = input("Introduce nuevos apellidos:")
        email = input("Introduce un nuevo email:")
        direccion = input("Introduce una nueva direccion:")

        cursor.execute(f'''
            INSERT INTO clientes
            VALUES (
                NULL,
                "{nombre}",
                "{apellidos}",
                "{email}",
                "{direccion}"
            );
        ''')                                                            

        conexion.commit()

        print("Tu registro se ha insertado correctamente en la base de datos")
        input("Pulsa una tecla para continuar....")
        
    elif opcion == "2":
        print("Vamos a listar los registros")
        
        cursor.execute('''
            SELECT * FROM clientes;
        ''')                                                            
        filas = cursor.fetchall()

        resultado = [dict(fila) for fila in filas]
        
        for fila in resultado:                                              
            print("---------------")
            print("Nombre:",fila['nombre'])
            print("Apellidos:",fila['apellidos'])
            print("Email:",fila['email'])
            print("Direccion:",fila['direccion'])
            
        print("Listado correctamente devuelto.")
        input("Pulsa una tecla para continuar....")
        
    elif opcion == "3":
        print("Vamos a actualizar un registro")

        identificador = input("Indica el registro que quieres actualizar (id):")

        nombre = input("Introduce un nuevo nombre:")
        apellidos = input("Introduce nuevos apellidos:")
        email = input("Introduce un nuevo email:")
        direccion = input("Introduce una nueva direccion:")

        cursor.execute(f'''
            UPDATE clientes
            SET
            nombre = '{nombre}',
            apellidos = '{apellidos}',
            email = '{email}',
            direccion = '{direccion}'
            WHERE Identificador = {identificador};
        ''')                                                            

        conexion.commit()
        print("Actualización correcta.")
        input("Pulsa una tecla para continuar....")
        
    elif opcion == "4":
        print("Vamos a eliminar un registro")
        identificador = input("Indica el registro que quieres eliminar (id):")
        cursor.execute(f'''
            DELETE FROM clientes
            WHERE Identificador = {identificador};
        ''')    

        conexion.commit()
        print("Eliminación correcta.")
        input("Pulsa una tecla para continuar....")
    

conexion.close() 



