import os

ruta = "/var/www/html/proyecto"

for directorio_raiz, subcarpetas, archivos in os.walk(ruta):
    for archivo in archivos:
        ruta_completa = os.path.join(directorio_raiz, archivo)
        print(ruta_completa)
