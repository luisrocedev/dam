import os

ruta = "/var/www/html/proyecto"

carpetas = os.listdir(ruta)

for carpeta in carpetas:
    print(carpeta)
