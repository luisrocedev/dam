import os

try:
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe, continuamos...")

print("Bienvenidos a Mi Querido Diario v0.2")
print("Selecciona una de las siguiente opciones")
print("1.-Introducir un nuevo registro")
print("2.-Leer registros existentes")

