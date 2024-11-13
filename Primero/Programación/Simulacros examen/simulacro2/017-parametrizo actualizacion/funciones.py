import mysql.connector                                  # Importo el conector de MySQL

conexion = mysql.connector.connect(
    host="localhost",           
    user="examenprogramacion",        
    password="examenprogramacion",   
    database="examenprogramacion"    
)                                                       # Me conecto a la base de datos

def seleccionaCapitulo():
    cursor = conexion.cursor(dictionary = True)             # Creo un cursor y me aseguro de que la info me viene en JSON
    peticion = "SELECT * FROM capitulos"                    # Pido todo de capitulos
    cursor.execute(peticion)                                # Ejecuto la peticion
    filas = cursor.fetchall()                               # Saco las filas
    return filas                                            # Imprimo las filas

def insertaCapitulo(Titulo,Subtitulo,Imagen,Video,Texto):
    cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
    peticion = f"""
    INSERT INTO capitulos
    VALUES (
        NULL,
        '{Titulo}',
        '{Subtitulo}',
        '{Imagen}',
        '{Video}',
        '{Texto}'
    )"""                                                    # Inserto un nuevo capítulo
    cursor.execute(peticion)                                # Ejecuto la peticion
    filas = cursor.fetchall()                               # Saco las filas
    conexion.commit()
    return True

def eliminaCapitulo(Identificador):
    cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
    peticion = f"""
    DELETE FROM capitulos
    WHERE Identificador = {Identificador}
    """     
    cursor.execute(peticion)                                # Ejecuto la peticion
    filas = cursor.fetchall()                               # Saco las filas
    conexion.commit()
    return True

def actualizaCapitulo(Identificador,Titulo,Subtitulo,Imagen,Video,Texto):
    cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
        if Titulo != "":
        peticion = f"""
        UPDATE capitulos
        SET 
            Titulo = '{Titulo}'
            
        WHERE
        Identificador = {Identificador};
        """                                                    # Inserto un nuevo capítulo
        cursor.execute(peticion)                                # Ejecuto la peticion
        filas = cursor.fetchall()                               # Saco las filas
        print(filas)                                            # Imprimo las filas
        conexion.commit()
    if Subtitulo != "":
        peticion = f"""
        UPDATE capitulos
        SET 
            Subtitulo = '{Subtitulo}'
            
        WHERE
        Identificador = {Identificador};
        """                                                    # Inserto un nuevo capítulo
        cursor.execute(peticion)                                # Ejecuto la peticion
        filas = cursor.fetchall()                               # Saco las filas
        print(filas)                                            # Imprimo las filas
        conexion.commit()
    if Imagen != "":
        peticion = f"""
        UPDATE capitulos
        SET 
            Imagen = '{Imagen}'
            
        WHERE
        Identificador = {Identificador};
        """                                                    # Inserto un nuevo capítulo
        cursor.execute(peticion)                                # Ejecuto la peticion
        filas = cursor.fetchall()                               # Saco las filas
        print(filas)                                            # Imprimo las filas
        conexion.commit()
    if Video != "":
        peticion = f"""
        UPDATE capitulos
        SET 
            Video = '{Video}'
            
        WHERE
        Identificador = {Identificador};
        """                                                    # Inserto un nuevo capítulo
        cursor.execute(peticion)                                # Ejecuto la peticion
        filas = cursor.fetchall()                               # Saco las filas
        print(filas)                                            # Imprimo las filas
        conexion.commit()
    if Texto != "":
        peticion = f"""
        UPDATE capitulos
        SET 
            Texto = '{Texto}'
            
        WHERE
        Identificador = {Identificador};
        """                                                    # Inserto un nuevo capítulo
        cursor.execute(peticion)                                # Ejecuto la peticion
        filas = cursor.fetchall()                               # Saco las filas
        conexion.commit()
        return True

        
