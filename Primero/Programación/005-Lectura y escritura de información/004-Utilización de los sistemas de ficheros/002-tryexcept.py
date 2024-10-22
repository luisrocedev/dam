import os

try:
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe, continuamos...")
