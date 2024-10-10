import mysql.connector

connection = mysql.connector.connect(
    host='localhost',   
    user='miempresa',   
    password='miempresa',
    database='miempresa' 
)

cursor = connection.cursor(dictionary = True)

cursor.execute('''
    SELECT 
    pedidos.fecha,
    clientes.nombre,
    clientes.apellidos
    FROM `pedidos` 
    LEFT JOIN clientes
    ON pedidos.clientes_apellidos = clientes.Identificador
''')

row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()

connection.close()
