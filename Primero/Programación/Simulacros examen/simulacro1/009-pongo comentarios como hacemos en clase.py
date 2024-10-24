class Cliente:                                                                      # Defino una clase de cliente
    def __init__(self,nuevoid,nuevonombre,nuevosapellidos,nuevoemail):
        self.id = nuevoid
        self.nombre = nuevonombre
        self.apellidos = nuevosapellidos
        self.email = nuevoemail

class Productos:                                                                    # Defino una clase de producto
    def __init__(self,nuevoid,nuevonombre,nuevadescripcion,nuevoprecio):
        self.id = nuevoid
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

    opcion = input("Selecciona una de estas operaciones:")                          # Atrapo la opción del usuario

    if opcion == "1":                                                               # Empezamos insertando un registro
        print("Insertamos un nuevo registro")                                       # Imprimo un mensaje
        identificador = input("Introduce el id del nuevo cliente: ")                  # Introduzco los datos que pido para la clase
        nombre = input("Introduce el nombre del nuevo cliente: ")
        apellidos = input("Introduce los apellidos del nuevo cliente: ")
        email = input("Introduce el email del nuevo cliente: ")
        Cliente = Cliente(identificador,nombre,apellidos,email)                     # Creo una nueva instancia
        clientes.append(Cliente)                                                    # Añado la instancia a la lista de clientes
        
    elif opcion == "2":
        print("Listamos los registros")
    elif opcion == "3":
        print("Actualizamos los registros")
    elif opcion == "4":
        print("Eliminamos registros")
    











