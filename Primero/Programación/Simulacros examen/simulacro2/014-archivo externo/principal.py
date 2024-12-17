from funciones import *

while True:
    print("Escoge una opcion")
    print("1.-Listar los registros")
    print("2.-Insertar un registro")
    print("3.-Eliminar un registro")
    print("4.-Actualizar un registro")
    print("5.-Cerrar el programa")
    opcion = input("Escoge una opcion:")

    if opcion == "1":
        print(seleccionaCapitulo())
    elif opcion == "2":
        print(insertaCapitulo())
    elif opcion == "3":
        print(eliminaCapitulo())
    elif opcion == "4":
        print(actualizaCapitulo())
    elif opcion == "5":
        conexion.close()
        break

print("El programa ha finalizado")

        
