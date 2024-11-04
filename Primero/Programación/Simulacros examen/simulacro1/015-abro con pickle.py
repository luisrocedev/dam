import pickle

class Cliente:                                                                      # Defino una clase de cliente
    def __init__(self,nuevoid,nuevonombre,nuevosapellidos,nuevoemail):
        self.identificador = nuevoid
        self.nombre = nuevonombre
        self.apellidos = nuevosapellidos
        self.email = nuevoemail

class Productos:                                                                    # Defino una clase de producto
    def __init__(self,nuevoid,nuevonombre,nuevadescripcion,nuevoprecio):
        self.identificador = nuevoid
        self.nombre = nuevonombre
        self.descripcion = nuevadescripcion
        self.precio = nuevoprecio

clientes = []                                                                       # Creo una lista vacia que es donde voy a guardar a los clientes
productos = []                                                                      # Creo una lista vacia que es donde voy a guardar a los productos

print("Programa de Consola")                                                        # imprimo mensaje de bienvenida
print("v0.1 por Jose Vicente Carratala")                                            # Imprimo el autor

while True:                                                                         # Entro en un bucle infinito
    print("########################")                                               # Imprimo un separador visual
    print("Selecciona entidad")                                                     # Invito a seleccionar una entida
    print("1.-Clientes")
    print("2.-Productos")

    entidad = input("Indica la opcion seleccionada:")                               # Atrapo el valor de la entidad

    print("Selecciona operacion")                                                   # Ahora muestro el menu de operaciones
    print("1.-Insertar un nuevo registro")
    print("2.-Listar registros")
    print("3.-Actualizar registro")
    print("4.-Eliminar registro")
    print("5.-Guardar")
    print("6.-Cargar")

    opcion = input("Selecciona una de estas operaciones:")                          # Atrapo la opción del usuario

    if opcion == "1":                                                               # Empezamos insertando un registro
        print("Insertamos un nuevo registro")                                       # Imprimo un mensaje
        identificador = input("Introduce el id del nuevo cliente: ")                  # Introduzco los datos que pido para la clase
        nombre = input("Introduce el nombre del nuevo cliente: ")
        apellidos = input("Introduce los apellidos del nuevo cliente: ")
        email = input("Introduce el email del nuevo cliente: ")
        clientes.append(Cliente(identificador,nombre,apellidos,email))              # Añado la instancia a la lista de clientes
        
    elif opcion == "2":                                                             # Si la opcion es la de listar
        print("Listamos los registros")                                             # Pongo un print
        contador = 0
        for cliente in clientes:                                                    # Para cada uno de los clientes en la lista de clientes
            print("------------------")                                             # Pongo un separador
            print("Id de Python:"+str(contador))
            print("id: "+cliente.identificador)                                     # Imprimo cada una de las caracteristicas
            print("nombre: "+cliente.nombre)
            print("apellidos: "+cliente.apellidos)
            print("email: "+cliente.email)
            contador+= 1
    elif opcion == "3":
        print("Actualizamos los registros")
        idlista = input("Selecciona el elemento de la lista de Python que quieres actualizar:")
        identificador = input("Introduce el id del cliente modificado: ")                  # Introduzco los datos que pido para la clase
        nombre = input("Introduce el nombre del cliente modificado: ")
        apellidos = input("Introduce los apellidos del cliente modificado: ")
        email = input("Introduce el email del cliente modificado ")
        clientes[int(idlista)].identificador = identificador
        clientes[int(idlista)].nombre = nombre
        clientes[int(idlista)].apellidos = apellidos
        clientes[int(idlista)].email = email
    elif opcion == "4":
        print("Eliminamos registros")
        idlista = input("Selecciona el elemento de la lista de Python que quieres eliminar:")
        clientes.pop(int(idlista))
    elif opcion == "5":
        archivo = open("clientes.dat",'wb')
        pickle.dump(clientes,archivo)
        archivo.close()
    elif opcion == "6":
        archivo = open("clientes.dat",'rb')
        clientes = pickle.load(archivo)
        archivo.close()











