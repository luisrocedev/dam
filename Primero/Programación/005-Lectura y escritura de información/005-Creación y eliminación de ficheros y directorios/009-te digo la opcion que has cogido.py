import pickle

class Cliente:
    def __init__(self):
        self.nombre = None
        self.apellidos = None
        self.email = None
        self.direccion = None


print("###############################################")
print("Programa agenda v0.1 por Jose Vicente Carratala")
print("###############################################")

print("Menú de navegación")
print("1.-Introduce un registro")
print("2.-Listado de registros")

opcion = input("Selecciona una opcion:")
print("Has cogido la opcion: ",opcion)

