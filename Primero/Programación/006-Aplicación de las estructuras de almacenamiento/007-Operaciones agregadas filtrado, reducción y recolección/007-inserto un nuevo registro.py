import sqlite3

conexion = sqlite3.connect('empresa.db')

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE 
    IF NOT EXISTS clientes
    (
        Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellidos TEXT,
        email TEXT,
        direccion TEXT
    )
''')

cursor.execute('''
    INSERT INTO clientes
    VALUES (
        NULL,
        'Jose Vicente',
        'Carratalá Sanchis',
        'info@josevicentecarratala.com',
        'La calle de Jose Vicente'
    )
''')

conexion.commit()

conexion.close()
