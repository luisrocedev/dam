import sqlite3
import matplotlib.pyplot as plt

# Conectar a la base de datos
conexion = sqlite3.connect('registros.db')
conexion.text_factory = lambda x: str(x, 'utf-8', 'replace')
cursor = conexion.cursor()

# Ejecutar consulta SQL
cursor.execute('''
    SELECT
    COUNT(anio) as año,
    anio
    FROM logs
    GROUP BY anio
    ;
''')

filas = cursor.fetchall()

# Inicializar listas para etiquetas y datos
etiquetas = []
datos = []

for fila in filas:
    etiquetas.append(fila[1])  # Años
    datos.append(fila[0])      # Cantidad por año

# Crear gráfico de barras
plt.bar(etiquetas, datos)

# Etiquetas y título del gráfico
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.title('Cantidad de registros por año')

# Guardar gráfico
plt.savefig('barras_bigdata.png')

# Cerrar el gráfico
plt.close()
