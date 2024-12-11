import os
import time
from datetime import datetime
import shutil
import subprocess

try:                                                                    # Intento
    os.mkdir("/home/josevicente/backups")                               # Crear la carpeta de backups
except:                                                                 # En el caso de que de error
    print("la carpeta ya existe, continuamos...")                       # Saco un mensaje por consola

ahora = datetime.now()                                                  # Atrapo el tiempo actual
fecha = ahora.strftime("%Y-%m-%d-%H-%M-%S")                             # Lo formateo en un formato humanamente entendible
epoch = str(round(time.time()))                                         # Obtengo la era unix
fechacompuesta = fecha+"_"+epoch                                        # Creo una fecha compuesta
print(fechacompuesta)                                                   # Imprimo la fecha
os.mkdir("/home/josevicente/backups/"+fechacompuesta)                   # Creo un directorio con la fecha compuesta
origen = "/var/www/html/proyecto"
destino = "/home/josevicente/backups/"+fechacompuesta+"/programacion"
shutil.copytree(origen, destino)
os.mkdir("/home/josevicente/backups/"+fechacompuesta+"/basededatos")    # Creo un directorio con la fecha compuesta
servidor = "localhost"
usuario = "proyectoapple"
contrasena = "proyectoapple"
basededatos = "proyectoapple"

comando = [
        "mysqldump",
        f"--host={servidor}",
        f"--user={usuario}",
        f"--password={contrasena}",
        basededatos
    ]
archivo = open("/home/josevicente/backups/"+fechacompuesta+"/basededatos/exportacion.sql",'w')
subprocess.run(comando, stdout=archivo, check=True)
archivo.close()
