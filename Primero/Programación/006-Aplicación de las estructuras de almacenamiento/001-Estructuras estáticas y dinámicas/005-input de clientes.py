clientes = []

clientes.append("Jose Vicente")
print(clientes)
clientes.append("Juan")
print(clientes)

while(True):
    nombre = input("Introduce el nombre de un nuevo cliente:")
    clientes.append(nombre)
    print(clientes)
