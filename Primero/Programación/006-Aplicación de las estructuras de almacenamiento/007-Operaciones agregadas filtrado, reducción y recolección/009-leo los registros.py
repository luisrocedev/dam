import sqlite3                                                  # Importo la librería de conexióna bases de datos

conexion = sqlite3.connect('empresa.db')                        # Abro una base de datos existente o la creo si no existe

cursor = conexion.cursor()                                      # Creo un cursor dentro de la base de datos

cursor.execute('''
    CREATE TABLE 
    IF NOT EXISTS clientes
    (
        Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellidos TEXT,
        email TEXT,
        direccion TEXT
    );
''')                                                            # Ejecuto una petición de creación de tabla en el caso de que no exista

cursor.execute('''
    INSERT INTO clientes
    VALUES (
        NULL,
        'Jose Vicente',
        'Carratalá Sanchis',
        'info@josevicentecarratala.com',
        'La calle de Jose Vicente'
    );
''')                                                            # Inserto un registro nuevo

conexion.commit()                                               # Ejecuto las peticiones

cursor.execute('''
    SELECT * FROM clientes;
''')                                                            # Ejecuto una petición de seleccion

filas = cursor.fetchall()                                       # Almaceno el resultado en una lista

for fila in filas:                                              # Proceso la lista elemento a elemento
    print(fila)                                                 # Imprimo cada una de las filas

    

conexion.close()                                                # Cerramos los recursos que previamente hemos abierto




















