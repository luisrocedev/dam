# Windows: pip install mysql-connector-python
# Mac: pip3 install mysql-connector-python
import mysql.connector

servidor = "localhost"
usuario = "miempresa"
contrasena = "miempresa"
base_de_datos = "miempresa"

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)

peticion = "SELECT * FROM clientes;"

